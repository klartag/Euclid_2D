/// Describes the action of a group that applies on a set.
pub trait GroupAction {
    /// The number of elements in the group.
    fn group_size(&self) -> usize;

    /// The size of the set the action applies on.
    #[cfg(test)]
    fn domain_size(&self) -> usize;

    /// When applying the [`element_index`]-th group element
    /// (assumes the elements are ordered in some deterministic fashion),
    /// Returns the index of the acted on set that the [`domain_index`]-th element in the set moves to.
    ///
    /// E.g, if the 10-th group element applies the permutation (0 -> 2 -> 3 -> 4 -> 0; 1 -> 1)
    /// in the set {0, 1, 2, 3, 4},
    /// then calling this method with arguments (10, 3) will return 4, and calling (10, 4) will return 0.
    fn apply(&self, element_index: usize, domain_index: usize) -> usize;
}
