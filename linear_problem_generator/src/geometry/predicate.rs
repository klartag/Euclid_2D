use serde::{Deserialize, Serialize};
use smallvec::SmallVec;

use super::predicate_type::PredicateType;
use crate::consts::MAX_ARGS;

/// An instance of a [`PredicateType`] in a [`crate::Diagram`].
#[derive(Debug, Clone, Serialize, Deserialize)]
pub(crate) struct Predicate {
    /// The PredicateType this predicate represents.
    pub(crate) _type: PredicateType,
    /// The indices of arguments (of constructions in the [`Diagram`] this predicate exists in)
    /// were used to construct this predicate.
    pub(crate) arguments: SmallVec<[usize; MAX_ARGS]>,
}

impl Predicate {
    pub(crate) fn new(predicate: PredicateType, arguments: SmallVec<[usize; MAX_ARGS]>) -> Self {
        Self {
            _type: predicate,
            arguments,
        }
    }
}
