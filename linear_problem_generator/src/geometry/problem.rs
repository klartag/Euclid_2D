use std::collections::{HashMap, HashSet};

use itertools::Itertools;
use serde::{Deserialize, Serialize};

use crate::naming::{geogebra_naming::GeoGebraNaming, naming_scheme::NamingScheme};

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
}
