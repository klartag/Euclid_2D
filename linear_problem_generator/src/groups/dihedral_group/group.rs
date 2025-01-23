use itertools::Itertools;

use super::{super::group_action::GroupAction, element::DihedralGroupElement};

/// A group that acts on a set of elements like the symmetries
/// of the vertices on a regular polygon.
pub(crate) struct DihedralGroup {
    /// The amount of elements we are acting on.
    side_count: usize,

    /// A cached set of all possible symmetries.
    all_elements: Vec<DihedralGroupElement>,
}

impl DihedralGroup {
    pub(crate) fn new(side_count: usize) -> Self {
        Self {
            side_count,
            all_elements: [false, true]
                .into_iter()
                .cartesian_product(0..side_count)
                .map(|x| x.into())
                .collect(),
        }
    }
}

impl GroupAction for DihedralGroup {
    fn group_size(&self) -> usize {
        2 * self.side_count
    }

    #[cfg(test)]
    fn domain_size(&self) -> usize {
        self.side_count
    }

    fn apply(&self, element_index: usize, domain_index: usize) -> usize {
        let element = self.all_elements[element_index];

        if element.reflection {
            (element.rotation + self.side_count - domain_index) % self.side_count
        } else {
            (element.rotation + domain_index) % self.side_count
        }
    }
}
