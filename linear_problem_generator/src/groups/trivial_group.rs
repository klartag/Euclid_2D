use super::group_action::GroupAction;

/// A group that contains only the trivial element.
#[derive(Default)]
pub(crate) struct TrivialGroup {}

impl GroupAction for TrivialGroup {
    fn group_size(&self) -> usize {
        1
    }

    #[cfg(test)]
    fn domain_size(&self) -> usize {
        0
    }

    fn apply(&self, _element_index: usize, domain_index: usize) -> usize {
        domain_index
    }
}
