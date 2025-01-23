use itertools::Itertools;

use super::group_action::GroupAction;

/// The group that acts with all possible permutations over N objects.
pub(crate) struct SymmetricGroup<const N: usize> {
    /// A cached list of all N! permutations.
    all_permutations: Vec<[usize; N]>,
}

impl<const N: usize> SymmetricGroup<N> {
    pub(crate) fn new() -> Self {
        Self {
            all_permutations: (0..N)
                .permutations(N)
                .map(|permutation| permutation.as_slice().try_into().unwrap())
                .collect_vec(),
        }
    }
}

impl<const N: usize> GroupAction for SymmetricGroup<N> {
    fn group_size(&self) -> usize {
        self.all_permutations.len()
    }

    #[cfg(test)]
    fn domain_size(&self) -> usize {
        N
    }

    fn apply(&self, element_index: usize, domain_index: usize) -> usize {
        self.all_permutations[element_index][domain_index]
    }
}
