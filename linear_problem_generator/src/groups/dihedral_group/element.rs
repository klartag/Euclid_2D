/// Represents a symmetry of an N-sided regular polygon. (for some N)
///
/// If the element has both a reflection and a non-trivial rotation,
/// the element acts as if the reflection is applied *first*.
#[derive(Default, PartialEq, Eq, Clone, Copy, Debug)]
pub(crate) struct DihedralGroupElement {
    /// Whether the symmetry includes a reflection
    pub(crate) reflection: bool,
    /// The amount of clockwise rotation in the symmetry.
    pub(crate) rotation: usize,
}

impl From<(bool, usize)> for DihedralGroupElement {
    fn from(value: (bool, usize)) -> Self {
        Self {
            reflection: value.0,
            rotation: value.1,
        }
    }
}

impl From<(usize, bool)> for DihedralGroupElement {
    fn from(value: (usize, bool)) -> Self {
        Self {
            reflection: value.1,
            rotation: value.0,
        }
    }
}
