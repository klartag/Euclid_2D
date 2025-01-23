use itertools::Itertools;

/// Types of symmetries that apply in signatures of [`super::construction_type::ConstructionType`]s and [`super::predicate_type::PredicateType`]s.
#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug)]
pub(crate) enum Symmetry {
    /// When it does not matter in what order arguments appear
    All,
    /// When the order of arguments is allowed to be reversed
    Reverse,
    /// When the last two arguments are allowed to be swapped
    SwapLast01,
    /// When the first two and second two can be swapped, and also swapped with each other.
    TwoPairSwap,
    /// When arguments cannot be reordered
    None,
}

impl Symmetry {
    /// Returns all permutations of the given set of objects allowed by the symmetry.
    pub(crate) fn all_permutations<T: Copy>(&self, args: &[T]) -> Vec<Vec<T>> {
        match self {
            Symmetry::All => args.iter().copied().permutations(args.len()).collect_vec(),
            Symmetry::Reverse => {
                vec![
                    args.iter().copied().collect_vec(),
                    args.iter().copied().rev().collect_vec(),
                ]
            }
            Symmetry::None => vec![args.iter().copied().collect_vec()],
            Symmetry::SwapLast01 => vec![
                args.iter().copied().collect_vec(),
                args[..args.len() - 2]
                    .into_iter()
                    .chain([&args[args.len() - 1], &args[args.len() - 2]])
                    .copied()
                    .collect(),
            ],
            Symmetry::TwoPairSwap => {
                let tail = args[4..].iter().copied().collect::<Vec<_>>();

                vec![
                    vec![args[0], args[1], args[2], args[3]],
                    vec![args[0], args[1], args[3], args[2]],
                    vec![args[1], args[0], args[2], args[3]],
                    vec![args[1], args[0], args[3], args[2]],
                    vec![args[2], args[3], args[0], args[1]],
                    vec![args[2], args[3], args[1], args[0]],
                    vec![args[3], args[2], args[0], args[1]],
                    vec![args[3], args[2], args[1], args[0]],
                ]
                .into_iter()
                .map(|head| head.into_iter().chain(tail.clone()).collect_vec())
                .collect_vec()
            }
        }
    }

    /// Returns whether two sets of arguments are the same up to the symmetry depicted by [`self`].
    pub(crate) fn is_in_symmetry<T: PartialEq + Copy>(&self, args_0: &[T], args_1: &[T]) -> bool {
        self.all_permutations(args_0)
            .into_iter()
            .any(|args_0| args_0.iter().zip(args_1).all(|(i, j)| i == j))
    }

    /// Returns whether the arugments are in a minimal order with regards to the symmetry.
    /// ("minimal" here might slightly differ depending on the symmetry used,
    /// but is well defined for each of the symmetries)
    pub(crate) fn is_minimal<T: PartialOrd>(&self, args: &[T]) -> bool {
        match self {
            Symmetry::All => args
                .iter()
                .zip(args.iter().skip(1))
                .all(|(arg_0, arg_1)| arg_0 <= arg_1),
            Symmetry::Reverse => {
                if let Some(index) = (0..args.len())
                    .filter(|index| args[*index] != args[args.len() - 1 - index])
                    .next()
                {
                    args[index] < args[args.len() - 1 - index]
                } else {
                    false
                }
            }
            Symmetry::SwapLast01 => args[args.len() - 2] <= args[args.len() - 1],
            Symmetry::TwoPairSwap => {
                args[0] <= args[1]
                    && args[2] <= args[3]
                    && args[0] <= args[2]
                    && (args[0] < args[2] || args[1] <= args[3])
            }
            Symmetry::None => true,
        }
    }
}
