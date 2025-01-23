use std::{collections::{HashMap, HashSet}, hash::{DefaultHasher, Hash, Hasher}, u64};

use itertools::Itertools;
use rand::{rngs::StdRng, RngCore, SeedableRng};
use serde::{Deserialize, Serialize};
use smallvec::SmallVec;

use crate::{embeddings::{embedded_objects::{embedded_object::EmbeddedObject, embedded_point}, predicates_simple::{hash_circle, hash_line, hash_point}, EmbeddedDiagram}, geometry::{construction::Construction, construction_type::ConstructionType, PredicateType}, groups::symmetric_group::SymmetricGroup, naming::{geogebra_naming::GeoGebraNaming, naming_scheme::NamingScheme}, problem_generation::{SingleRandomObjectExtender, SymmetricalExtender}};

use super::{diagram::Diagram, predicate::Predicate};

/// An instance of a geometry problem.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Problem {
    /// The constructions required to state the problem
    pub(crate) diagram: Diagram,
    /// The predicate that the problem asks you to prove
    pub(crate) predicate: Predicate,
}

impl Problem {
    /// Returns all constructions in a diagram that are needed to formulate the problem's predicate.
    pub(crate) fn used_constructions(&self) -> HashSet<usize> {
        let mut used_constructions = HashSet::<usize>::new();
        let mut pending = Vec::<usize>::new();

        self.predicate.arguments.iter().for_each(|arg| {
            pending.push(*arg);
        });

        while let Some(arg) = pending.pop() {
            used_constructions.insert(arg);

            self.diagram.constructions[arg]
                .arguments
                .iter()
                .for_each(|arg| {
                    pending.push(*arg);
                });
        }

        used_constructions
    }

    /// Formats the problem as a string,
    /// in one of two formats, depending on the `should_serialize` parameter.
    ///
    /// If `should_serialize` is False, formats in the `.jl` format readable by the Proof Generator.
    /// If `should_serialize` is True, serializes the Problem into a `.json` file.
    ///
    pub fn to_string(&self, should_serialize: bool) -> String {
        if should_serialize {
            serde_json::to_string_pretty(&self).unwrap()
        } else {
            self.format_for_proof_generator(&mut GeoGebraNaming::default())
        }
    }

    /// Formats a problem in a form that can be read by the proof generator.
    ///
    /// naming_scheme:  The [`NamingScheme`] with which to generate names for the diagram's constructions.
    pub(crate) fn format_for_proof_generator<N: NamingScheme>(
        &self,
        naming_scheme: &mut N,
    ) -> String {
        let names = self.diagram.get_names(naming_scheme);
        let diagram_string = self.diagram.to_string(&names);

        let argument_names = self
            .predicate
            .arguments
            .iter()
            .map(|argument| names[*argument].clone())
            .collect_vec();

        let target_predicate_string = self.predicate._type.to_string(&argument_names);

        format!(
            "{}\n\
            \n\
            Need to prove:\n\
            {}\n\
            \n\
            Proof:\n",
            diagram_string, target_predicate_string
        )
    }

    /// Checks whether there is a homeomorphism between two problem statements.
    pub fn is_homeomorphic_to(&self, problem: &Problem) -> bool {
        let nondeterministic_constructions_0 = self.diagram.nondeterministic_constructions();
        let nondeterministic_constructions_1 = problem.diagram.nondeterministic_constructions();

        nondeterministic_constructions_1
            .iter()
            .permutations(nondeterministic_constructions_1.len())
            .any(|nondeterministic_constructions_1| {
                let mut homeomorphism = nondeterministic_constructions_0
                    .iter()
                    .zip(nondeterministic_constructions_1)
                    .collect::<HashMap<_, _>>();

                let deterministic_constructions_0 = self.diagram.deterministic_constructions();
                let deterministic_constructions_1 = problem.diagram.deterministic_constructions();

                let found_homeomorphism =
                    deterministic_constructions_0.iter().all(|construction_0| {
                        if let Some(construction_1) =
                            deterministic_constructions_1
                                .iter()
                                .find(|&construction_1| {
                                    let construction_0 =
                                        &self.diagram.constructions[*construction_0];
                                    let construction_1 =
                                        &problem.diagram.constructions[*construction_1];

                                    if construction_0._type != construction_1._type {
                                        false
                                    } else if let Some(mapped_arguments) = construction_0
                                        .arguments
                                        .iter()
                                        .map(|arg| homeomorphism.get(&arg).copied().copied())
                                        .collect::<Option<Vec<usize>>>()
                                    {
                                        construction_0._type.symmetry().is_in_symmetry(
                                            &mapped_arguments,
                                            construction_1.arguments.as_slice(),
                                        )
                                    } else {
                                        false
                                    }
                                })
                        {
                            homeomorphism.insert(construction_0, construction_1);
                            true
                        } else {
                            false
                        }
                    });

                found_homeomorphism
                    && self.predicate._type == problem.predicate._type
                    && self
                        .predicate
                        .arguments
                        .iter()
                        .zip(problem.predicate.arguments.iter())
                        .all(|(i0, i1)| homeomorphism.get(i0) == Some(&&i1))
            })
    }

    pub fn hash(&self) -> u64 {
        let mut rng: Box<dyn RngCore> = Box::new(StdRng::from_seed([0; 32]));

        let mut embedded_diagram = EmbeddedDiagram::<f64>::new(self.diagram.clone(), &mut rng);
        
        let target_construction = match self.predicate._type {
            PredicateType::Collinear => Construction {
                _type: ConstructionType::Line,
                arguments: [self.predicate.arguments[0], self.predicate.arguments[1]].into_iter().collect::<SmallVec<_>>(),
            },
            PredicateType::Concyclic => Construction {
                _type: ConstructionType::Circumcircle,
                arguments: [self.predicate.arguments[0], self.predicate.arguments[1], self.predicate.arguments[2]].into_iter().collect::<SmallVec<_>>(),
            },
            PredicateType::Concurrent => Construction {
                _type: ConstructionType::LineIntersection,
                arguments: [self.predicate.arguments[0], self.predicate.arguments[1]].into_iter().collect::<SmallVec<_>>(),
            },
            _ => { return 0; }
        };

        embedded_diagram.try_push(target_construction.clone(), &mut rng);
        let Some(embedded_target_construction_index) = embedded_diagram.try_find(&target_construction, &mut rng) else {
            return 0;
        };

        let extender = SymmetricalExtender::new(
            SingleRandomObjectExtender::default(),
            vec![0, 1, 2], Box::new(SymmetricGroup::<3>::new())
        );

        
        let target_hashes = (0..6)
            .map(|symmetry_index| extender.try_push_symmetry(&mut embedded_diagram, embedded_target_construction_index, symmetry_index, &mut rng))
            .collect_vec()
            .into_iter()
            .map(|object_index| {
                if let Some(object_index) = object_index {
                    let embedded_target_object = embedded_diagram.embeddings()[0].iter().skip(object_index).next().unwrap();

                    let mut state = DefaultHasher::new();
            
                    match embedded_target_object {
                        EmbeddedObject::Point(embedded_point) => hash_point(embedded_point.clone()).hash(&mut state),
                        EmbeddedObject::Line(embedded_line) => hash_line(embedded_line.clone()).hash(&mut state),
                        EmbeddedObject::Circle(embedded_circle) => hash_circle(embedded_circle.clone()).hash(&mut state),
                    };
                    state.finish()
                }
                else {
                    0
                }
            })
            .collect_vec();

        return target_hashes.into_iter().min().unwrap();
    }
}
