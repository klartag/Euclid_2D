use std::{
    collections::HashMap,
    hash::{Hash, Hasher},
};

use itertools::Itertools;
use rand::{thread_rng, RngCore};
use rustc_hash::FxHasher;
use serde::{Deserialize, Serialize};
use smallvec::SmallVec;

use crate::{
    embeddings::{
        embedded_objects::embedded_object::{EmbeddedObject, EmbeddingError},
        embedding::Embedding,
        geo_float::GeoFloat,
        TryEmbed,
    },
    naming::naming_scheme::NamingScheme,
};

use super::{construction::Construction, construction_type::ConstructionType, geo_type::GeoType};

/// A configuration of constructions.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Diagram {
    /// The [`Construction`]s contained in the diagram.
    pub(crate) constructions: Vec<Construction>,
    /// A mapping from each `GeoType` to the indices in [`Self::constructions`] that contain constructions of that [`GeoType`].
    pub(crate) geo_type_to_indices: HashMap<GeoType, Vec<usize>>,
}

impl Diagram {
    pub(crate) fn new() -> Self {
        Self {
            constructions: Default::default(),
            geo_type_to_indices: Default::default(),
        }
    }

    /// Generates names for all the constructions in the diagram.
    pub(crate) fn get_names<N: NamingScheme>(&self, naming_scheme: &mut N) -> Vec<String> {
        naming_scheme.reset();

        self.constructions
            .iter()
            .map(|construction| naming_scheme.next_name(construction.geo_type()))
            .collect()
    }

    /// Formats the Diagram in a way that can be read by the proof generator.
    ///
    /// names:  The names of the Constructions in `Self::constructions`.
    pub(crate) fn to_string(&self, names: &[String]) -> String {
        let mut problem_statement_lines = Vec::<String>::new();

        problem_statement_lines.push("Assumptions:".into());

        let point_names = (0..self.constructions.len())
            .filter(|index| self.constructions[*index].geo_type() == GeoType::Point)
            .map(|index| &names[index])
            .collect_vec();

        let line_names = (0..self.constructions.len())
            .filter(|index| self.constructions[*index].geo_type() == GeoType::Line)
            .map(|index| &names[index])
            .collect_vec();

        let circle_names = (0..self.constructions.len())
            .filter(|index| self.constructions[*index].geo_type() == GeoType::Circle)
            .map(|index| &names[index])
            .collect_vec();

        let all_point_names = point_names.iter().join(", ");
        let all_line_names = line_names.iter().join(", ");
        let all_circle_names = circle_names.iter().join(", ");

        if point_names.len() > 0 {
            problem_statement_lines.push(all_point_names.clone() + ": Point");
        }

        if line_names.len() > 0 {
            problem_statement_lines.push(all_line_names.clone() + ": Line");
        }

        if circle_names.len() > 0 {
            problem_statement_lines.push(all_circle_names.clone() + ": Circle");
        }

        if point_names.len() > 1 {
            problem_statement_lines.push(format!("distinct({})", all_point_names));
        }

        if line_names.len() > 1 {
            problem_statement_lines.push(format!("distinct({})", all_line_names));
        }

        if circle_names.len() > 1 {
            problem_statement_lines.push(format!("distinct({})", all_circle_names));
        }

        // Part 2: Adding predicates defining/constructing each construction.
        for (index, construction) in self.constructions.iter().enumerate() {
            let construction_name = names[index].as_str();
            let argument_names = construction
                .arguments
                .iter()
                .map(|i| names[*i].as_str())
                .collect_vec();
            if let Some(assupmtion_line) = construction
                ._type
                .to_string(construction_name, &argument_names)
            {
                problem_statement_lines.push(assupmtion_line);
            }
        }

        problem_statement_lines.join("\n")
    }

    /// Adds a new [`Construction`] to the Diagram.
    /// (updates [`Self::geo_type_to_indices`] accordingly)
    pub(crate) fn push(&mut self, construction: Construction) {
        let geo_type = construction.geo_type();

        self.constructions.push(construction);

        self.geo_type_to_indices
            .entry(geo_type)
            .or_default()
            .push(self.constructions.len() - 1);
    }

    /// Builds a new construction whose arguments belong to the current diagram.
    ///
    /// construction_type:   Which ConstructionType to build the construction with.
    /// arguments:      The indices of constructions in the diagram to use as arguments.
    pub(crate) fn construct<U: AsRef<[usize]>>(
        &self,
        construction_type: ConstructionType,
        arguments: U,
    ) -> Construction {
        let sig = construction_type.signature();
        let arguments = arguments.as_ref();
        assert!(
            arguments.iter().all(|arg| *arg < self.constructions.len()),
            "Tried to build {construction_type:?} with signature {arguments:?},
    but the diagram has only {:?} elements.",
            self.constructions.len()
        );

        assert_eq!(
            arguments.len(),
            sig.len(),
            "Tried to build {construction_type:?} with signature {:?}, when the correct signature is {:?}.",
            arguments
                .iter()
                .map(|arg| self.constructions[*arg].geo_type()),
            construction_type.signature()
        );

        for (arg, sig_type) in arguments.iter().zip(sig.iter().cloned()) {
            assert_eq!(
                self.constructions[*arg].geo_type(),
                sig_type,
                "Tried to build {construction_type:?} with signature {:?}, when the correct signature is {:?}.",
                arguments.iter().map(|arg| self.constructions[*arg].geo_type()),
                construction_type.signature()
            );
        }

        let min_args: SmallVec<[usize; 3]> = construction_type
            .symmetry()
            .all_permutations(&arguments)
            .iter()
            .min_by_key(|permutated_arguments| {
                let mut hash = FxHasher::default();
                for argument in permutated_arguments.iter() {
                    argument.hash(&mut hash);
                }
                hash.finish()
            })
            .unwrap()
            .iter()
            .copied()
            .collect();

        Construction {
            _type: construction_type,
            arguments: min_args,
        }
    }

    /// Returns alternatives to a Construction that generalize it,
    /// in such a way that its degrees of freedom are increased.
    ///
    /// Examples:
    /// *   The construction `project point A into line l` could be generalized
    ///     to `take an arbitrary point on line l`.
    /// *   The construction `draw a line going through points A and B` could be generalized
    ///     to `take an arbitrary line through A`,
    ///     or to `take an arbitrary line through B`.
    pub(crate) fn generalizations(&self, construction: &Construction) -> Vec<Construction> {
        match construction._type {
            ConstructionType::NewPoint
            | ConstructionType::NewLine
            | ConstructionType::NewCircle => {
                vec![]
            }

            ConstructionType::PointOnLine
            | ConstructionType::PointOnCircle
            | ConstructionType::Center
            | ConstructionType::CollinearPoint => {
                vec![self.construct(ConstructionType::NewPoint, &[])]
            }

            ConstructionType::Midpoint => {
                vec![self.construct(ConstructionType::CollinearPoint, &construction.arguments)]
            }

            ConstructionType::LineOnPoint => vec![self.construct(ConstructionType::NewLine, &[])],

            ConstructionType::CircleFromCenter => {
                vec![self.construct(ConstructionType::NewCircle, &[])]
            }

            ConstructionType::Line => {
                vec![
                    self.construct(ConstructionType::LineOnPoint, &[construction.arguments[0]]),
                    self.construct(ConstructionType::LineOnPoint, &[construction.arguments[1]]),
                ]
            }
            ConstructionType::LineIntersection => {
                vec![
                    self.construct(ConstructionType::PointOnLine, &[construction.arguments[0]]),
                    self.construct(ConstructionType::PointOnLine, &[construction.arguments[1]]),
                ]
            }
            ConstructionType::Circumcircle => {
                vec![self.construct(ConstructionType::NewCircle, &[])]
            } // TODO: Make this a more specific trivialization
            ConstructionType::Projection => {
                vec![self.construct(ConstructionType::PointOnLine, &[construction.arguments[1]])]
            }
            ConstructionType::LineCircleIntersection => {
                vec![
                    self.construct(ConstructionType::PointOnLine, &[construction.arguments[0]]),
                    self.construct(
                        ConstructionType::PointOnCircle,
                        &[construction.arguments[1]],
                    ),
                ]
            }
            ConstructionType::LineCircleOtherIntersection => {
                vec![
                    self.construct(ConstructionType::PointOnLine, &[construction.arguments[1]]),
                    self.construct(
                        ConstructionType::PointOnCircle,
                        &[construction.arguments[2]],
                    ),
                ]
            }
            ConstructionType::CircleIntersection => {
                vec![
                    self.construct(
                        ConstructionType::PointOnCircle,
                        &[construction.arguments[0]],
                    ),
                    self.construct(
                        ConstructionType::PointOnCircle,
                        &[construction.arguments[1]],
                    ),
                ]
            }
            ConstructionType::CircleCircleOtherIntersection => {
                vec![
                    self.construct(
                        ConstructionType::PointOnCircle,
                        &[construction.arguments[1]],
                    ),
                    self.construct(
                        ConstructionType::PointOnCircle,
                        &[construction.arguments[2]],
                    ),
                ]
            }
            ConstructionType::CircleFromCenterAndRadius => {
                vec![self.construct(
                    ConstructionType::CircleFromCenter,
                    &[construction.arguments[0]],
                )]
            }
            ConstructionType::InternalBisector | ConstructionType::ExternalBisector => {
                vec![self.construct(ConstructionType::LineOnPoint, &[construction.arguments[1]])]
            }
            ConstructionType::Parallel => {
                vec![
                    self.construct(ConstructionType::LineOnPoint, &[construction.arguments[1]]),
                    // TODO: There is a trivialization missing here.
                ]
            }
            ConstructionType::Tangent | ConstructionType::OtherTangent => {
                vec![
                    self.construct(ConstructionType::LineOnPoint, &[construction.arguments[0]]),
                    // TODO: There is a trivialization missing here.
                ]
            }
        }
    }

    /// Tries to embed the diagram into `F^2`.
    ///
    /// attempt_count:  The amount of times the method should attempt to embed the diagram
    ///                 before giving up.
    pub(crate) fn embed<F: GeoFloat>(
        &self,
        attempt_count: usize,
        rng: &mut Box<dyn RngCore>
    ) -> Result<Embedding<F>, EmbeddingError>
    where
        ConstructionType: TryEmbed<F, Box<dyn RngCore>>,
    {
        (0..attempt_count)
            .filter_map(|_| {
                let mut embeds = Embedding::<F>::new();

                for construction in &self.constructions {
                    match self.try_embed_construction::<F>(construction, &embeds, rng) {
                        Ok(embedded_obj) => embeds.push(embedded_obj),
                        Err(_) => break,
                    }
                }

                (embeds.len() == self.constructions.len()).then_some(Ok(embeds))
            })
            .next()
            .unwrap_or(Err(EmbeddingError::Undefined))
    }

    /// Attempts to add a single [`Construction`] into an embedding.
    ///
    /// partial_embedding:  A list of embeddings belonging to the current diagram.
    ///                     The list might *not be complete*, in the sense that
    ///                     it is possible that only part of `Self::constructions` are embedded.
    ///                     Even if the list is incomplete (which it will be most of the time
    ///                     this method is called), the indices of constructions in this parameter
    ///                     will match the indices of the constructions they represent in `Self::constructions`.
    pub(crate) fn try_embed_construction<F: GeoFloat>(
        &self,
        construction: &Construction,
        partial_embedding: &Embedding<F>,
        rng: &mut Box<dyn RngCore>
    ) -> Result<EmbeddedObject<F>, EmbeddingError>
    where
        ConstructionType: TryEmbed<F, Box<dyn RngCore>>,
    {
        assert!(
            !construction
                .arguments
                .iter()
                .max()
                .is_some_and(|&max| max >= partial_embedding.len()),
            "Not all arguments required for this construction to be created have an embedding."
        );

        let argument_embeddings = construction
            .arguments
            .iter()
            .map(|&argument| partial_embedding[argument].clone())
            .collect_vec();

        construction
            ._type
            .try_build(&argument_embeddings, rng)
    }

    /// Returns the list of indices of constructions in the diagram whose constructions are deterministic.
    /// (see [`ConstructionType::is_deterministic`] for more details)
    pub(crate) fn deterministic_constructions(&self) -> Vec<usize> {
        self.constructions
            .iter()
            .enumerate()
            .filter(|(_, construction)| construction._type.is_deterministic())
            .map(|(index, _)| index)
            .collect::<Vec<_>>()
    }

    /// Returns the list of indices of constructions in the diagram whose constructions are non-deterministic.
    /// (see [`ConstructionType::is_deterministic`] for more details)
    pub(crate) fn nondeterministic_constructions(&self) -> Vec<usize> {
        self.constructions
            .iter()
            .enumerate()
            .filter(|(_, construction)| !construction._type.is_deterministic())
            .map(|(index, _)| index)
            .collect::<Vec<_>>()
    }

    /// Checks whether a construction is not used as an argument in the creation of any other constructions.
    /// (i.e, whether it is a leaf in the graph representing the constructions in the diagram)
    pub(crate) fn is_leaf(&self, index: usize) -> bool {
        !self
            .constructions
            .iter()
            .any(|construction| construction.arguments.contains(&index))
    }
}
