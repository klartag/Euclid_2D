use linear_b::linear::sparse_linear;

#[cfg(test)]
mod tests {
    use itertools::Itertools;
    use linear_b::{
        hashmap,
        linear::dense_linear::{
            BoolLinearSolverBase, CombinationFind, LinearSolver, RLinearSolverBase,
        },
    };

    /// Tests that the combination finder finds only the correct combinations in a simple example.
    /// Here, we search X + Y + 1 - Z == 0
    #[test]
    fn test_combinations_real() {
        let mut lin = RLinearSolverBase::new(0);
        lin.add_relation(hashmap!(0 => 1., 1 => -1.));
        lin.add_relation(hashmap!(0 => 2., 2 => -1.));
        lin.add_relation(hashmap!(0 => 3., 3 => -1.));
        lin.add_relation(hashmap!(0 => 4., 4 => -1.));

        let combs = lin
            .find_combinations(
                vec![1., 1., -1.],
                1.,
                vec![
                    vec![0, 1, 2, 3, 4, 5],
                    vec![0, 1, 2, 3, 4, 5],
                    vec![0, 1, 2, 3, 4, 5],
                ],
            )
            .into_iter()
            .sorted()
            .collect_vec();

        assert_eq!(
            combs,
            vec![
                vec![0, 0, 3],
                vec![0, 1, 3],
                vec![0, 2, 4],
                vec![1, 0, 3],
                vec![1, 1, 3],
                vec![1, 2, 4],
                vec![2, 0, 4],
                vec![2, 1, 4],
            ]
        );
    }
    #[test]
    fn test_combinations_bool() {
        let mut lin = BoolLinearSolverBase::new(0);
        // 1 is 1.
        // 2 is 0.
        // 3 is unknown.
        // The combinations known to be 0 are those that contain 2 exactly one, and then either 3 twice or 0 and 1 twice.

        lin.add_relation(hashmap!(0 => true, 1 => true));
        lin.add_relation(hashmap!(0 => true, 1 => true, 2 => true));

        let combs = lin
            .find_combinations(
                vec![true, true, true],
                false,
                vec![vec![0, 1, 2, 3], vec![0, 1, 2, 3], vec![0, 1, 2, 3]],
            )
            .into_iter()
            .sorted()
            .collect_vec();
        assert_eq!(
            combs,
            vec![
                vec![0, 0, 2],
                vec![0, 1, 2],
                vec![0, 2, 0],
                vec![0, 2, 1],
                vec![1, 0, 2],
                vec![1, 1, 2],
                vec![1, 2, 0],
                vec![1, 2, 1],
                vec![2, 0, 0],
                vec![2, 0, 1],
                vec![2, 1, 0],
                vec![2, 1, 1],
                vec![2, 2, 2],
                vec![2, 3, 3],
                vec![3, 2, 3],
                vec![3, 3, 2]
            ]
        );
    }
}

fn main() {
    sparse_linear::main();
    // sparse_linear::sparse_linear_tests::test_nonzero_mod();
    // test_mod_solver();
    // test_r_solver();
    // test_bool_solver();
    // test_explicit();
    // test_matching();
    // geometry::embed::main();

    // test_combinations()
}
