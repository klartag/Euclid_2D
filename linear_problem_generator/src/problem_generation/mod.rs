pub(crate) mod diagram_extension;
pub(crate) mod problem_finding;

/// The number of simultanious embeddings the ProblemGenerator should hold when searching for a problem.
pub(crate) const REQUIRED_EMBEDDING_COUNT: usize = 32;

pub use diagram_extension::{
    diagram_extender::DiagramExtender, heuristical_extender::HeuristicalExtender,
    repeat_extender::RepeatExtender, single_random_object_extender::SingleRandomObjectExtender,
    symmetrical_extender::SymmetricalExtender,
};

pub use problem_finding::problem_finder::ProblemFinder;
