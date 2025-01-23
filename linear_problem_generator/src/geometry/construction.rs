use super::geo_type::GeoType;

use super::construction_type::ConstructionType;
use serde::{Deserialize, Serialize};
use smallvec::SmallVec;

/// An instance of a [`ConstructionType`] in a [`crate::Diagram`].
#[derive(Clone, Debug, Serialize, Deserialize)]
pub(crate) struct Construction {
    /// The ConstructionType this construction uses.
    pub(crate) _type: ConstructionType,
    /// The indices of arguments (in [`Diagram.constructions`] containing)
    /// were used to construct this.
    pub(crate) arguments: SmallVec<[usize; 3]>,
}

impl Construction {
    pub(crate) fn geo_type(&self) -> GeoType {
        self._type.geo_type()
    }

    pub(crate) fn is_identical(&self, other: &Construction) -> bool {
        self._type == other._type
            && self
                ._type
                .symmetry()
                .is_in_symmetry(&self.arguments, &other.arguments)
    }
}
