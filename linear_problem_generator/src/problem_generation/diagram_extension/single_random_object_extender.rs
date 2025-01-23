use std::collections::HashSet;

use itertools::Itertools;
use rand::{distributions::weighted::WeightedIndex, rngs::ThreadRng, seq::SliceRandom, thread_rng};
use rand_distr::Distribution;

use crate::{
    embeddings::{embedded_diagram::EmbeddedDiagram, geo_float::GeoFloat, TryEmbed},
    geometry::{construction::Construction, construction_type::ConstructionType},
};

use super::diagram_extender::DiagramExtender;

/// A [`DiagramExtender`] that adds a single random object to the diagram.
#[derive(Default)]
pub struct SingleRandomObjectExtender {}

impl DiagramExtender for SingleRandomObjectExtender {
    fn extend_diagram<F: GeoFloat>(&self, embedded_diagram: &mut EmbeddedDiagram<F>)
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        let Some(construction_type) = self.choose_construction_type() else {
            unreachable!()
        };

        if let Some(new_construction) =
            self.generate_construction(&embedded_diagram, construction_type)
        {
            embedded_diagram.try_push(new_construction);
        }
    }
}

impl SingleRandomObjectExtender {
    /// Generates a random instance of a given ConstructionType.
    ///
    /// diagram:            The diagram whose constructions we will use as arguments.
    /// embeddings:         A list of embeddings of `diagram`.
    /// construction_type:  The ConstructionType we want to use to create a construction.
    fn generate_construction<F: GeoFloat>(
        &self,
        embedded_diagram: &EmbeddedDiagram<F>,
        construction_type: ConstructionType,
    ) -> Option<Construction>
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        construction_type
            .signature()
            .iter()
            .map(|geo_type| {
                let mut construction_indices = embedded_diagram
                    .diagram()
                    .geo_type_to_indices
                    .get(geo_type)
                    .into_iter()
                    .flatten()
                    .collect::<Vec<_>>();

                construction_indices.shuffle(&mut thread_rng());

                construction_indices
            })
            .multi_cartesian_product()
            .filter(|signature_instance| {
                signature_instance.iter().collect::<HashSet<_>>().len() == signature_instance.len()
            })
            .map(|arguments| {
                embedded_diagram.diagram().construct(
                    construction_type,
                    &arguments.into_iter().copied().collect::<Vec<_>>(),
                )
            })
            .filter(|new_construction| {
                embedded_diagram
                    .embeddings()
                    .iter()
                    .filter(|embedding| {
                        embedded_diagram
                            .diagram()
                            .try_embed_construction(new_construction, embedding)
                            .is_ok()
                    })
                    .take(2)
                    .count()
                    == 2
            })
            .next()
    }

    /// Picks a random ConstructionType, taking [`Self::construction_type_probability_weights`]
    /// into account for the distribution.
    fn choose_construction_type(&self) -> Option<ConstructionType> {
        let choices = [
            ConstructionType::Line,
            ConstructionType::LineIntersection,
            ConstructionType::Circumcircle,
            ConstructionType::CircleCircleOtherIntersection,
            ConstructionType::LineCircleOtherIntersection,
            ConstructionType::InternalBisector,
            ConstructionType::ExternalBisector,
            ConstructionType::Midpoint,
            ConstructionType::Parallel,
            ConstructionType::Center,
            ConstructionType::Projection,
        ];

        let weights = choices
            .iter()
            .map(|construction_type| self.construction_type_probability_weights(*construction_type))
            .collect::<Vec<_>>();

        let Ok(distribution) = WeightedIndex::new(weights) else {
            return None;
        };

        return Some(choices[distribution.sample(&mut thread_rng())]);
    }

    /// Weights telling the ProblemGenerator the distribution with which it should pick a given ConstructionType.
    fn construction_type_probability_weights(&self, construction_type: ConstructionType) -> u32 {
        match construction_type {
            ConstructionType::CircleCircleOtherIntersection
            | ConstructionType::LineCircleOtherIntersection => 80,

            ConstructionType::Line
            | ConstructionType::LineIntersection
            | ConstructionType::Circumcircle => 40,

            ConstructionType::Projection
            | ConstructionType::Midpoint
            | ConstructionType::InternalBisector
            | ConstructionType::ExternalBisector => 20,
            ConstructionType::Parallel => 20,
            ConstructionType::Center => 20,

            ConstructionType::LineCircleIntersection
            | ConstructionType::CircleIntersection
            | ConstructionType::CircleFromCenterAndRadius
            | ConstructionType::Tangent
            | ConstructionType::OtherTangent
            | ConstructionType::NewPoint
            | ConstructionType::NewLine
            | ConstructionType::NewCircle
            | ConstructionType::PointOnLine
            | ConstructionType::PointOnCircle
            | ConstructionType::LineOnPoint
            | ConstructionType::CircleFromCenter
            | ConstructionType::CollinearPoint => 0,
        }
    }
}
