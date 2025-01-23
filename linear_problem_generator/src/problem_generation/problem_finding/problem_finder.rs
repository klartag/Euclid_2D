use std::collections::HashMap;

use smallvec::smallvec;

use itertools::Itertools;
use rand::rngs::ThreadRng;

use crate::{
    embeddings::{embedding::Embedding, geo_float::GeoFloat, CheckApply, TryEmbed},
    geometry::{
        construction::Construction, construction_type::ConstructionType, diagram::Diagram,
        geo_type::GeoType, predicate::Predicate, predicate_type::PredicateType, problem::Problem,
    },
    problem_generation::REQUIRED_EMBEDDING_COUNT,
};

/// The maximum amount of times to attempt embedding a construction before giving up.
pub(crate) const MAX_EMBED_ATTEMPTS: usize = 2;

/// A struct that knows how to look for geometry problems in diagrams.
pub struct ProblemFinder {
    /// The types of geometry problems we should look for.
    predicate_types: Vec<PredicateType>,
}

impl ProblemFinder {
    pub fn new(predicate_types: Vec<PredicateType>) -> Self {
        Self { predicate_types }
    }

    /// Looks for geometry problems in a given diagram.
    pub fn find_problems<F: GeoFloat>(
        &self,
        diagram: &Diagram,
        embedding: &Embedding<F>,
    ) -> Vec<Problem>
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        self.predicate_types
            .iter()
            .map(|predicate_type| {
                predicate_type
                    .find_all(diagram, &embedding)
                    .into_iter()
                    .map(|predicate_arguments| Predicate::new(*predicate_type, predicate_arguments))
            })
            .flatten()
            .map(|predicate| Problem {
                diagram: diagram.clone(),
                predicate,
            })
            .filter(|problem| self.double_check_problem::<F>(problem))
            .map(|problem| self.minimize_diagram_statement(&problem))
            .filter(|problem| self.is_two_dimensional(&problem.diagram))
            .filter(|problem| self.double_check_problem::<F>(problem))
            .filter(|problem| self.uses_nondeterministic_constructions_nontrivially::<F>(problem))
            .map(|problem| self.generalize_diagram::<F>(problem))
            .map(|problem| self.simplify_problem_statment(problem))
            .flatten()
            .map(|problem| self.minimize_diagram_statement(&problem))
            .filter(|problem| self.uses_nondeterministic_constructions_nontrivially::<F>(problem))
            .filter(|problem| self.is_two_dimensional(&problem.diagram))
            .collect()
    }

    /// Checks whether a diagram is not trivially contained inside a single line.
    pub(crate) fn is_two_dimensional(&self, diagram: &Diagram) -> bool {
        // TODO: Although this is a pretty good heuristic, there might exist two-dimensional problems
        // without circles that contain at most one line. (e.g. problems that contain mostly midpoints).
        // This function should be replaced with a different function that generates an embedding and checks
        // whether all points in the embedding are collinear.
        let contains_two_lines = diagram
            .geo_type_to_indices
            .get(&GeoType::Line)
            .map(|v| v.len())
            .unwrap_or_default()
            > 1;
        let contains_circle = diagram
            .geo_type_to_indices
            .get(&GeoType::Circle)
            .map(|v| v.len())
            .unwrap_or_default()
            > 0;

        contains_two_lines || contains_circle
    }

    /// Checks whether the nondeterministic constructions are:
    /// *   All used.
    /// *   All used as parameters of other constructions in the problem
    ///     (and not the last construction in the problem statement).
    /// *   All used in the most generalized way they can be used.
    pub(crate) fn uses_nondeterministic_constructions_nontrivially<F: GeoFloat>(
        &self,
        problem: &Problem,
    ) -> bool
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        let nondeterministic_constructions = problem.diagram.nondeterministic_constructions();

        let used_constructions = problem.used_constructions();

        if !nondeterministic_constructions
            .iter()
            .all(|construction| used_constructions.contains(construction))
        {
            return false;
        }

        if nondeterministic_constructions
            .iter()
            .any(|construction| problem.diagram.is_leaf(*construction))
        {
            return false;
        }

        let mut diagram_clone = problem.diagram.clone();

        for (construction_index, construction) in problem
            .diagram
            .constructions
            .iter()
            .enumerate()
            .filter(|(_, construction)| {
                construction
                    .arguments
                    .iter()
                    .any(|parameter| nondeterministic_constructions.contains(parameter))
            })
        {
            for mut trivialized_construction in problem.diagram.generalizations(construction) {
                if self.is_generalization_valid::<F>(
                    &mut diagram_clone,
                    &problem.predicate,
                    construction_index,
                    &mut trivialized_construction,
                ) {
                    return false;
                }
            }
        }

        return true;
    }

    /// Generalizes the diagram as much as possible, while still keeping the problem correct.
    pub(crate) fn generalize_diagram<F: GeoFloat>(&self, problem: Problem) -> Problem
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        let mut diagram = problem.diagram.clone();

        loop {
            let mut diagram_clone = diagram.clone();

            if let Some((construction_index, generalized_construction)) = diagram
                .constructions
                .iter()
                .enumerate()
                .filter_map(|(construction_index, construction)| {
                    let generalizations = diagram.generalizations(construction);
                    if let Some(generalization) = generalizations
                        .into_iter()
                        .filter_map(|mut generalization| {
                            self.is_generalization_valid::<F>(
                                &mut diagram_clone,
                                &problem.predicate,
                                construction_index,
                                &mut generalization,
                            )
                            .then_some(generalization)
                        })
                        .next()
                    {
                        return Some((construction_index, generalization));
                    }

                    return None;
                })
                .next()
            {
                diagram.constructions[construction_index] = generalized_construction;
            } else {
                break;
            }
        }

        Problem {
            diagram,
            predicate: problem.predicate,
        }
    }

    /// Checks whether a generalization of a problem is still correct.
    ///
    /// diagram:                    The diagram who we are attempting to generalize.
    ///                             A mutable reference to the diagram is used to quickly
    ///                             swap a construction with its generalized version.
    /// predicate:                  The predicate to be checked after generalizing.
    /// index:                      The index of the construction in the `diagram` to generalize.
    /// generalized_construction:   The Construction to put in place of `diagram.constructions[index]`.
    fn is_generalization_valid<F: GeoFloat>(
        &self,
        diagram: &mut Diagram,
        predicate: &Predicate,
        index: usize,
        generalized_construction: &mut Construction,
    ) -> bool
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        std::mem::swap(generalized_construction, &mut diagram.constructions[index]);

        let is_trivialization_valid = diagram
            .embed::<F>(MAX_EMBED_ATTEMPTS)
            .map(|embedding| {
                predicate._type.applies(
                    &predicate
                        .arguments
                        .iter()
                        .map(|index| embedding[*index])
                        .collect::<Vec<_>>(),
                )
            })
            .unwrap_or(false);

        std::mem::swap(generalized_construction, &mut diagram.constructions[index]);
        is_trivialization_valid
    }

    /// Makes sure a problem is correct by generating a bunch of diagrams
    /// and checking that the predicate is correct in each of them.
    fn double_check_problem<F: GeoFloat>(&self, problem: &Problem) -> bool
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        (0..REQUIRED_EMBEDDING_COUNT).all(|_| {
            let Ok(embedding) = problem.diagram.embed(MAX_EMBED_ATTEMPTS) else {
                return false;
            };
            problem.predicate._type.applies(
                &problem
                    .predicate
                    .arguments
                    .iter()
                    .map(|i| embedding[*i])
                    .collect::<Vec<_>>(),
            )
        })
    }

    /// Removes constructions from a diagram that are not needed to formulate the problem's predicate.
    pub(crate) fn minimize_diagram_statement(&self, problem: &Problem) -> Problem {
        let used_constructions = problem
            .used_constructions()
            .into_iter()
            .sorted()
            .collect_vec();

        let reverse_used_constructions = used_constructions
            .iter()
            .enumerate()
            .map(|(i, j)| (j, i))
            .collect::<HashMap<_, _>>();

        let mut new_diagram = Diagram::new();

        for i in 0..used_constructions.len() {
            let construction = &problem.diagram.constructions[used_constructions[i]];
            let arguments = construction
                .arguments
                .iter()
                .map(|i| reverse_used_constructions[i])
                .collect_vec();
            let new_construction = new_diagram.construct(construction._type, &arguments);
            new_diagram.push(new_construction);
        }

        let new_predicate = Predicate {
            _type: problem.predicate._type,
            arguments: problem
                .predicate
                .arguments
                .iter()
                .map(|i| reverse_used_constructions[i])
                .collect::<_>(),
        };

        Problem {
            diagram: new_diagram,
            predicate: new_predicate,
        }
    }

    /// If a problem's predicate contains a nondeterministic construction, it sometimes makes sense
    /// to split the problem into two smaller problems.
    ///
    /// For example:
    /// If the predicate is "Prove that A, B, C are collinear",
    /// but the point `C` is constructed as `An arbitrary point on line l`,
    /// then it would be nicer to separate the problem into problems with the predicates
    /// `A is on l` and `B is on l`.
    ///
    /// This method does similar things for the Collinear, Concurrent, and Concyclic predicates.
    pub(crate) fn simplify_problem_statment(&self, problem: Problem) -> Vec<Problem> {
        match problem.predicate._type {
            PredicateType::Collinear
                if let Some(argument) = problem
                    .predicate
                    .arguments
                    .iter()
                    .filter(|argument| {
                        problem.diagram.constructions[**argument]._type
                            == ConstructionType::PointOnLine
                            && problem.diagram.is_leaf(**argument)
                    })
                    .next() =>
            {
                let line = problem.diagram.constructions[*argument].arguments[0];
                problem
                    .predicate
                    .arguments
                    .iter()
                    .filter(|arg| *arg != argument)
                    .map(|arg| Problem {
                        diagram: problem.diagram.clone(),
                        predicate: Predicate::new(PredicateType::InLine, smallvec![*arg, line]),
                    })
                    .collect()
            }
            PredicateType::Concurrent
                if let Some(argument) = problem
                    .predicate
                    .arguments
                    .iter()
                    .filter(|argument| {
                        problem.diagram.constructions[**argument]._type
                            == ConstructionType::LineOnPoint
                            && problem.diagram.is_leaf(**argument)
                    })
                    .next() =>
            {
                let point = problem.diagram.constructions[*argument].arguments[0];
                problem
                    .predicate
                    .arguments
                    .iter()
                    .filter(|arg| *arg != argument)
                    .map(|arg| Problem {
                        diagram: problem.diagram.clone(),
                        predicate: Predicate::new(PredicateType::InLine, smallvec![point, *arg]),
                    })
                    .collect()
            }
            PredicateType::Concyclic
                if let Some(argument) = problem
                    .predicate
                    .arguments
                    .iter()
                    .filter(|argument| {
                        problem.diagram.constructions[**argument]._type
                            == ConstructionType::PointOnCircle
                            && problem.diagram.is_leaf(**argument)
                    })
                    .next() =>
            {
                let circle = problem.diagram.constructions[*argument].arguments[0];
                problem
                    .predicate
                    .arguments
                    .iter()
                    .filter(|arg| *arg != argument)
                    .map(|arg| Problem {
                        diagram: problem.diagram.clone(),
                        predicate: Predicate::new(PredicateType::InCircle, smallvec![*arg, circle]),
                    })
                    .collect()
            }
            _ => vec![problem],
        }
    }
}
