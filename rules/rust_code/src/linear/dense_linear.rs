use super::dense_vec::Vector;
use crate::hashmap;
use itertools::Itertools;
use num_traits::{One, Zero};
use pyo3::prelude::*;
use rand::{thread_rng, Rng};
use rustc_hash::FxHashMap;
use std::fmt::Debug;
use std::hash::Hash;
use std::ops::{Add, AddAssign, Mul, SubAssign};

type HashType = i64;

/// A trait of structs that track linear algebra relations and inequalities, implementing the shared behavior.
/// Relations are tracked suing standard linear algebra.
/// Non-zero relations are more difficult. They are stored as a list of non-zero relations, since they are not additive,
/// and to check if some linear combinations is non-zero, it is first reduced using the relations,
/// reduced using one of the non-zeroes, and reduced again using the relations.
///
/// The linear solver is a trait for linear algebra systems using dense vectors, and supports both vector spaces or modules.
/// The basic functions to get data from the linear algebra object are:
/// 1. `get_data`: Provides the list of basis vectors for the vector space or the module.
/// 2. `get_map`: Provides a mapping from outer objects to their index in the dense vectors.
pub trait LinearSolver<
    Key: PartialEq + Eq + Hash + Clone,
    Scalar: Default + Clone + Debug + PartialEq,
>
{
    /// Gets the index of the constant element.
    fn get_const_key(&self) -> Key;
    /// Gets a mutable reference to the name map.
    fn get_map_mut(&mut self) -> &mut FxHashMap<Key, usize>;
    /// Gets the name map.
    fn get_map(&self) -> &FxHashMap<Key, usize>;
    /// Gets a mutable reference to the data and nonzero array.
    fn get_data_and_nonzero_mut(&mut self) -> (&mut Vec<Vector<Scalar>>, &mut Vec<Vector<Scalar>>);
    /// Gets the data array.
    fn get_data(&self) -> &Vec<Vector<Scalar>>;
    /// Gets the nonzero array.
    fn get_nonzero(&self) -> &Vec<Vector<Scalar>>;
    /// Checks which vector is the better reducer at the given column.
    fn is_better_reducer(v1: &Vector<Scalar>, v2: &Vector<Scalar>, col: usize) -> bool;
    /// Checks if the given value is zero, or sufficiently close to 0.
    fn is_zero(t: &Scalar) -> bool;
    /// Reduces the first vector with the second vector, usizng the given column.
    fn reduce_with(reduced: &mut Vector<Scalar>, with: &Vector<Scalar>, col: usize);
    /// Reduces the first vector with the second vector, usizng the given column.
    fn reduce_row_with(rows: &mut Vec<Vector<Scalar>>, reduced: usize, with: usize, col: usize);
    /// Transforms a vector to a canonical form.
    fn normalize_col(v: &mut Vector<Scalar>, col: usize);
    /// Transforms a vector to a canonical form.
    fn normalize(v: &mut Vector<Scalar>) {
        for i in (0..v.len()).rev() {
            if !Self::is_zero(&v[i]) {
                Self::normalize_col(v, i);
                return;
            }
        }
    }

    /// Gets the index of the constant factor.
    fn get_const_idx(&self) -> usize {
        *self
            .get_map()
            .get(&self.get_const_key())
            .expect("LinearSolver::get_const_idx: Solver does not have a const key!")
    }

    /// Checks if the given relation has a single known value.
    fn get_value(&self, rel: FxHashMap<Key, Scalar>) -> Option<Scalar> {
        let mut row = self.make_row(rel)?;
        self.reduce(&mut row);
        let nonzero_count = row.iter().filter(|t| !Self::is_zero(*t)).count();
        if nonzero_count == 0 {
            return Some(Scalar::default());
        }
        let const_idx = *self.get_map().get(&self.get_const_key())?;
        if nonzero_count == 1 && !Self::is_zero(&row[const_idx]) {
            return Some(row[const_idx].clone());
        }
        None
    }

    /// Gets a mutable reference to the data array.
    fn get_data_mut(&mut self) -> &mut Vec<Vector<Scalar>> {
        self.get_data_and_nonzero_mut().0
    }

    /// Gets a mutable reference to the nonzero array.
    fn get_nonzero_mut(&mut self) -> &mut Vec<Vector<Scalar>> {
        self.get_data_and_nonzero_mut().1
    }

    /// Adds new objects to the linear solver.
    fn add_objects(&mut self, new_objs: Vec<Key>) {
        let new_object_count = new_objs
            .iter()
            .unique()
            .filter(|obj| !self.get_map().contains_key(obj))
            .count();
        let new_length = self.get_map().len() + new_object_count;
        for v in self.get_data_mut().iter_mut() {
            v.resize(new_length);
        }
        for v in self.get_nonzero_mut().iter_mut() {
            v.resize(new_length);
        }
        let mut idx = self.get_map().len();
        for obj in new_objs.into_iter() {
            if !self.get_map().contains_key(&obj) {
                self.get_map_mut().insert(obj.clone(), idx);
                idx += 1;
            }
        }
    }

    /// Adds a new nonzero identity to the linear algebra tracker.
    fn add_nonzero(&mut self, rel: FxHashMap<Key, Scalar>) {
        self.add_objects(rel.keys().cloned().collect_vec());
        let mut row = self
            .make_row(rel)
            .expect("All objects should have been added to the tracker!");
        Self::_reduce_normalize(self.get_data(), &mut row);
        self.get_nonzero_mut().push(row);
    }

    /// Adds a new relation to the linear algebra tracker.
    fn add_relation(&mut self, rel: FxHashMap<Key, Scalar>) {
        self.add_objects(rel.keys().cloned().collect_vec());
        let row = self
            .make_row(rel)
            .expect("All objects should have been added to the tracker!");

        self.get_data_mut().push(row);
        self.echelonize();
    }

    /// Returns the number of objects tracked by the linear algebra solver.
    fn len(&self) -> usize {
        self.get_map().len()
    }

    /// Reduces a vector given a list of relations.
    fn _reduce(relations: &Vec<Vector<Scalar>>, v: &mut Vector<Scalar>) {
        let mut curr_row = 0;
        for col in (0..v.len()).rev() {
            if relations.len() == curr_row {
                break;
            }
            if !Self::is_zero(&relations[curr_row][col]) {
                Self::reduce_with(v, &relations[curr_row], col);
                curr_row += 1;
            }
        }
    }

    /// Reduces a vector given a list of relations.
    /// Normalizes the rightmost nonzero value of the vector to ensure it is reduced to canonical form.
    fn _reduce_normalize(relations: &Vec<Vector<Scalar>>, v: &mut Vector<Scalar>) {
        let mut curr_row = 0;
        let mut normalize = true;

        for col in (0..v.len()).rev() {
            if curr_row < relations.len() && !Self::is_zero(&relations[curr_row][col]) {
                Self::reduce_with(v, &relations[curr_row], col);
                curr_row += 1;
            }
            if normalize && !Self::is_zero(&v[col]) {
                Self::normalize_col(v, col);
                normalize = false;
            }
        }
    }

    /// Reduces a vector to the canonical form.
    /// The result of the reduction must be the canonical representative.
    fn reduce(&self, v: &mut Vector<Scalar>) {
        Self::_reduce(self.get_data(), v);
    }

    /// Reduces the vectors in the solver to an echelonized canonical form.
    fn echelonize(&mut self) {
        let cols = self.len();
        let (rows, nonzeroes) = self.get_data_and_nonzero_mut();
        let mut curr_row = 0;
        for col in (0..cols).rev() {
            // We have finished reducing the array.
            if curr_row == rows.len() {
                break;
            }
            loop {
                // Checking if the column is a zero column except for the top row.
                let mut finish_col = true;
                for row in (curr_row + 1)..rows.len() {
                    if !Self::is_zero(&rows[row][col]) {
                        finish_col = false;
                        break;
                    }
                }

                if finish_col {
                    for other_col in col + 1..cols {
                        assert!(Self::is_zero(&rows[curr_row][other_col]));
                    }
                    // If the row is nonzero, then we reduce all rows above the current row using the current row and normalize it.
                    if !Self::is_zero(&rows[curr_row][col]) {
                        // Reducing all rows above the given object.
                        for above_row in 0..curr_row {
                            Self::reduce_row_with(rows, above_row, curr_row, col);
                        }
                        Self::normalize(&mut rows[curr_row]);
                        curr_row += 1;
                    }
                    break;
                }
                // Finding the best reducer, and moving it to the current row.
                for other_row in (curr_row + 1)..rows.len() {
                    if Self::is_better_reducer(&rows[other_row], &rows[curr_row], col) {
                        rows.swap(curr_row, other_row);
                    }
                }
                // Reducing all other rows with the best reducer.
                for other_row in (curr_row + 1)..rows.len() {
                    Self::reduce_row_with(rows, other_row, curr_row, col);
                }
            }
        }

        // Attempting to improve numeric stability.
        for row in rows.iter_mut() {
            for val in row.iter_mut() {
                if Self::is_zero(val) {
                    *val = Scalar::default();
                }
            }
        }

        // Removing empty rows.
        while let Some(last_row) = rows.last_mut() {
            if last_row.iter().all(Self::is_zero) {
                rows.pop();
            } else {
                break;
            }
        }
        // Reducing and normalizing all the non-zero rows.
        for nonz in nonzeroes.iter_mut() {
            Self::_reduce_normalize(rows, nonz);
        }
    }

    /// Converts a dictionary to a vector.
    fn make_row(&self, rel: FxHashMap<Key, Scalar>) -> Option<Vector<Scalar>> {
        let mut data = vec![Scalar::default(); self.len()];
        for (key, val) in rel {
            if !Self::is_zero(&val) {
                data[*self.get_map().get(&key)?] = val;
            }
        }
        Some(Vector::new(data))
    }

    /// Checks if the linear algebra solver contains the given nonzero relation.
    fn contains_nonzero(&self, rel: FxHashMap<Key, Scalar>) -> bool {
        let Some(mut data) = self.make_row(rel) else {
            return false;
        };

        self.reduce(&mut data);

        // Checks if the reduced data is equal to some known value.
        let const_idx = self.get_const_idx();
        if (0..data.len())
            .into_iter()
            .all(|i| (i == const_idx) != (Self::is_zero(&data[i])))
        {
            return true;
        }

        let mut col = None;
        for i in 0..self.len() {
            if !Self::is_zero(&data[i]) {
                col = Some(i);
            }
        }
        if let Some(col) = col {
            // After reducing the relation, we have some non-zero coefficient.
            // The reduction is not trivial.

            // In this case, we have to check if the given vector is equal to one of the known nonzeroes.
            // We transform it to the canonical form, with normalized rightmost nonzero.
            // This takes care of multiplication by a unit.
            Self::normalize(&mut data);
            self.reduce(&mut data);

            // We then check if it is equal to one of the known nonzeroes.
            // Since != 0 is only closed to multiplication by a unit and we have taken the quotient by units,
            // it should be exactly equal to one of the nonzeroes
            for nonz in self.get_nonzero() {
                let mut cl = data.clone();
                // We first reduce using the nonzero.
                // If this worked, we check if the result is equal to zero.
                // We don't allow multiplication by a constant, so we have to make sure that the reduction is a subtraction (or xor).
                if nonz[col] != cl[col] {
                    continue;
                }
                Self::reduce_with(&mut cl, nonz, col);
                if cl.iter().all(Self::is_zero) {
                    return true;
                }
            }
            return false;
        } else {
            // After reducing the relation, we got 0.
            // This counts as a non-zero only if we have a null nonzero (Which also implies a contradiction).
            return self
                .get_nonzero()
                .iter()
                .any(|nonz| nonz.iter().all(Self::is_zero));
        }
    }

    /// Checks if the linear algebra solver contains the given relation.
    fn contains_relation(&self, rel: FxHashMap<Key, Scalar>) -> bool {
        let Some(mut data) = self.make_row(rel) else {
            return false;
        };
        self.reduce(&mut data);
        data.iter().all(Self::is_zero)
    }

    /// Checks if the tracker tracks the given object.
    fn contains(&self, key: &Key) -> bool {
        self.get_map().contains_key(key)
    }
}

pub trait ToHash {
    fn to_hash(&self) -> HashType;
}

impl ToHash for i64 {
    fn to_hash(&self) -> HashType {
        *self
    }
}
impl ToHash for i32 {
    fn to_hash(&self) -> HashType {
        *self as HashType
    }
}

impl ToHash for f64 {
    fn to_hash(&self) -> HashType {
        (self * 1024.).round() as HashType
    }
}

impl ToHash for bool {
    fn to_hash(&self) -> HashType {
        if *self {
            1
        } else {
            0
        }
    }
}

pub trait CombinationFindScalar:
    Default + Clone + Debug + Zero + One + Mul + Add + AddAssign + SubAssign + ToHash + PartialEq
{
}
impl CombinationFindScalar for i32 {}
impl CombinationFindScalar for i64 {}
impl CombinationFindScalar for f64 {}

pub trait CombinationFind<Key, Scalar> {
    /// Converts a scalar to an integer to allow hashing.
    // fn scalar_to_int(s: &Scalar) -> HashType;
    /// Finds all sets of objects such that the given combination of objects is zero.
    fn find_combinations(
        &self,
        coefficients: Vec<Scalar>,
        const_coef: Scalar,
        coef_keys: Vec<Vec<Key>>,
    ) -> Vec<Vec<Key>>;
}

impl<Key, Scalar, Solver> CombinationFind<Key, Scalar> for Solver
where
    Solver: LinearSolver<Key, Scalar>,
    Key: PartialEq + Eq + Hash + Clone + Default + Debug,
    Scalar: CombinationFindScalar,
{
    fn find_combinations(
        &self,
        coefficients: Vec<Scalar>,
        const_coef: Scalar,
        coef_keys: Vec<Vec<Key>>,
    ) -> Vec<Vec<Key>> {
        {
            debug_assert_eq!(coefficients.len(), coef_keys.len());
            let mut rng = thread_rng();

            let all_keys = coef_keys.iter().cloned().flatten().unique().collect_vec();
            let mut hashes: FxHashMap<Key, HashType> = all_keys
                .iter()
                .cloned()
                .map(|i| (i, rng.gen::<HashType>()))
                .collect();
            for key in self.get_map().keys() {
                hashes.insert(key.clone(), rng.gen::<HashType>());
            }
            let hashes = hashes;

            // All keys, ordered in a vec, so that keys[idx] is the key mapped to idx.
            let keys = {
                let mut curr = vec![Key::default(); self.len()];
                for (key, idx) in self.get_map() {
                    curr[*idx] = key.clone();
                }
                curr
            };

            // The hashes of the keys.
            // For some keys we have already generated hashes, and we use them to be consistent. For other keys we haven't,
            // and we sample new hashes for them.
            let key_hashes: Vec<HashType> = keys
                .iter()
                .map(|k| {
                    hashes
                        .get(k)
                        .map(Clone::clone)
                        .expect("CombinationFind::find_combinations: A key exists for which no hash was picked.")
                })
                .collect_vec();

            let mut reduced_singles = FxHashMap::default();
            for key in all_keys.iter().cloned() {
                let Some(mut vec) = self.make_row(hashmap! {key => Scalar::one()}) else {
                    continue;
                };
                self.reduce(&mut vec);
                reduced_singles.insert(key, vec);
            }

            let db_size = coefficients.len() / 2;

            let mut db = FxHashMap::default();
            let const_idx = self.get_const_idx();
            let neg_combinations = coef_keys[..db_size].to_vec();
            let pos_combinations = coef_keys[db_size..].to_vec();
            for neg_comb in neg_combinations.iter().multi_cartesian_product() {
                let mut vec_acc = Vector::new(vec![Scalar::zero(); self.len()]);

                vec_acc[const_idx] += const_coef.clone();

                let mut scalar_acc: HashType = 0;
                for (key, coef) in neg_comb.iter().zip(coefficients.iter()) {
                    if let Some(v) = reduced_singles.get(key) {
                        vec_acc += v * coef.clone();
                    } else {
                        scalar_acc = scalar_acc.wrapping_add(hashes
                            .get(key)
                            .expect("CombinationFind::find_combinations: All objects should have a hash!")
                            .wrapping_mul(coef.to_hash()));
                    }
                }
                self.reduce(&mut vec_acc);
                let vec_acc = vec_acc
                    .iter()
                    .zip(key_hashes.iter())
                    .map(|(i, j)| i.to_hash().wrapping_mul(*j))
                    .sum::<HashType>();

                let total = vec_acc.wrapping_add(scalar_acc);
                // println!("N {neg_comb:?} {total}");
                db.entry(total).or_insert(Vec::new()).push(neg_comb);
            }

            let mut res = Vec::new();

            for pos_comb in pos_combinations.iter().multi_cartesian_product() {
                let mut vec_acc = Vector::new(vec![Scalar::zero(); self.len()]);
                let mut scalar_acc: HashType = 0;
                for (key, coef) in pos_comb.iter().zip(coefficients[db_size..].iter()) {
                    if let Some(v) = reduced_singles.get(key) {
                        vec_acc -= v * coef.clone();
                    } else {
                        scalar_acc = scalar_acc.wrapping_sub(
                            hashes
                                .get(key)
                                .expect("All objects should have a hash!")
                                .wrapping_mul(coef.to_hash()),
                        );
                    }
                }

                self.reduce(&mut vec_acc);
                let vec_acc = vec_acc
                    .iter()
                    .zip(key_hashes.iter())
                    .map(|(i, j)| i.to_hash().wrapping_mul(*j))
                    .sum::<HashType>();
                let total = vec_acc.wrapping_add(scalar_acc);
                // println!("P {pos_comb:?} {total}");

                if let Some(neg_combs) = db.get(&total) {
                    for neg_comb in neg_combs {
                        let mut total_comb = Vec::new();
                        total_comb.reserve_exact(coefficients.len());
                        total_comb.extend(neg_comb.iter().map(|k| (*k).clone()));
                        total_comb.extend(pos_comb.iter().map(|k| (*k).clone()));
                        res.push(total_comb);
                    }
                }
            }

            res
        }
    }
}

impl<Key, Solver> CombinationFind<Key, bool> for Solver
where
    Solver: LinearSolver<Key, bool>,
    Key: PartialEq + Eq + Hash + Clone + Default + Debug,
{
    fn find_combinations(
        &self,
        coefficients: Vec<bool>,
        const_coef: bool,
        coef_keys: Vec<Vec<Key>>,
    ) -> Vec<Vec<Key>> {
        {
            debug_assert_eq!(coefficients.len(), coef_keys.len());
            let mut rng = thread_rng();

            let all_keys = coef_keys.iter().cloned().flatten().unique().collect_vec();
            let mut hashes: FxHashMap<Key, HashType> = all_keys
                .iter()
                .cloned()
                .map(|i| (i, rng.gen::<HashType>()))
                .collect();
            for key in self.get_map().keys() {
                hashes.insert(key.clone(), rng.gen::<HashType>());
            }
            let hashes = hashes;

            // All keys, ordered in a vec, so that keys[idx] is the key mapped to idx.
            let keys = {
                let mut curr = vec![Key::default(); self.len()];
                for (key, idx) in self.get_map() {
                    curr[*idx] = key.clone();
                }
                curr
            };

            // The hashes of the keys.
            // For some keys we have already generated hashes, and we use them to be consistent. For other keys we haven't,
            // and we sample new hashes for them.
            let key_hashes: Vec<HashType> = keys
                .iter()
                .map(|k| {
                    hashes
                        .get(k)
                        .map(Clone::clone)
                        .expect("CombinationFind::find_combinations: A key exists for which no hash was picked.")
                })
                .collect_vec();

            let mut reduced_singles = FxHashMap::default();
            for key in all_keys.iter().cloned() {
                let Some(mut vec) = self.make_row(hashmap! {key => true}) else {
                    continue;
                };
                self.reduce(&mut vec);
                reduced_singles.insert(key, vec);
            }

            let db_size = coefficients.len() / 2;

            let mut db = FxHashMap::default();
            let const_idx = self.get_const_idx();
            let neg_combinations = coef_keys[..db_size].to_vec();
            let pos_combinations = coef_keys[db_size..].to_vec();
            for neg_comb in neg_combinations.iter().multi_cartesian_product() {
                let mut vec_acc = Vector::new(vec![false; self.len()]);

                vec_acc[const_idx] ^= const_coef.clone();

                let mut scalar_acc: HashType = 0;
                for (key, coef) in neg_comb.iter().zip(coefficients.iter()) {
                    if let Some(v) = reduced_singles.get(key) {
                        if *coef {
                            vec_acc ^= v;
                        }
                    } else {
                        scalar_acc = scalar_acc ^ hashes
                            .get(key)
                            .expect("CombinationFind::find_combinations: All objects should have a hash!")
                            .wrapping_mul(coef.to_hash());
                    }
                }
                self.reduce(&mut vec_acc);
                let vec_acc = vec_acc
                    .iter()
                    .zip(key_hashes.iter())
                    .map(|(i, j)| i.to_hash().wrapping_mul(*j))
                    .sum::<HashType>();

                let total = vec_acc ^ scalar_acc;

                // println!("N {neg_comb:?} {total}");
                db.entry(total).or_insert(Vec::new()).push(neg_comb);
            }

            let mut res = Vec::new();

            for pos_comb in pos_combinations.iter().multi_cartesian_product() {
                let mut vec_acc = Vector::new(vec![false; self.len()]);
                let mut scalar_acc: HashType = 0;
                for (key, coef) in pos_comb.iter().zip(coefficients[db_size..].iter()) {
                    if let Some(v) = reduced_singles.get(key) {
                        if *coef {
                            vec_acc ^= v;
                        }
                    } else {
                        scalar_acc = scalar_acc
                            ^ hashes
                                .get(key)
                                .expect("All objects should have a hash!")
                                .wrapping_mul(coef.to_hash());
                    }
                }

                self.reduce(&mut vec_acc);
                let vec_acc = vec_acc
                    .iter()
                    .zip(key_hashes.iter())
                    .map(|(i, j)| i.to_hash().wrapping_mul(*j))
                    .sum::<HashType>();
                let total = vec_acc ^ scalar_acc;
                // println!("P {pos_comb:?} {total}");

                if let Some(neg_combs) = db.get(&total) {
                    for neg_comb in neg_combs {
                        let mut total_comb = Vec::new();
                        total_comb.reserve_exact(coefficients.len());
                        total_comb.extend(neg_comb.iter().map(|k| (*k).clone()));
                        total_comb.extend(pos_comb.iter().map(|k| (*k).clone()));
                        res.push(total_comb);
                    }
                }
            }

            res
        }
    }
}

#[derive(Default, Clone)]
pub struct ModLinearSolverBase {
    pub name_map: FxHashMap<i64, usize>,
    pub data: Vec<Vector<i32>>,
    /// A list of all linear combinations known to to be equal to 0.
    pub nonzeroes: Vec<Vector<i32>>,
    pub const_key: i64,
}

impl ModLinearSolverBase {
    pub fn new(const_key: i64) -> ModLinearSolverBase {
        ModLinearSolverBase {
            name_map: hashmap!(const_key => 0),
            data: Vec::new(),
            nonzeroes: Vec::new(),
            const_key,
        }
    }
}

// #[pymethods]
impl LinearSolver<i64, i32> for ModLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<i64, usize> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<i64, usize> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(&mut self) -> (&mut Vec<Vector<i32>>, &mut Vec<Vector<i32>>) {
        (&mut self.data, &mut self.nonzeroes)
    }

    fn get_data(&self) -> &Vec<Vector<i32>> {
        &self.data
    }

    fn get_nonzero(&self) -> &Vec<Vector<i32>> {
        &self.nonzeroes
    }

    fn reduce_with(reduced: &mut Vector<i32>, with: &Vector<i32>, col: usize) {
        if !Self::is_zero(&with[col]) && !Self::is_zero(&reduced[col]) {
            let factor = reduced[col].div_euclid(with[col]);
            *reduced -= with * factor;
        }
    }
    fn reduce_row_with(rows: &mut Vec<Vector<i32>>, reduced: usize, with: usize, col: usize) {
        if !Self::is_zero(&rows[with][col]) && !Self::is_zero(&rows[reduced][col]) {
            let factor = rows[reduced][col].div_euclid(rows[with][col]);
            let f = &rows[with] * factor;
            rows[reduced] -= f;
        }
    }

    fn normalize_col(_: &mut Vector<i32>, _: usize) {
        // Instead of normalizing nonzeroes in linear algebra modulo something, we just add both x and -x.
        // This is more stable with respect to everything.
    }

    fn add_nonzero(&mut self, rel: FxHashMap<i64, i32>) {
        self.add_objects(rel.keys().cloned().collect_vec());
        let mut pos_row = self
            .make_row(rel)
            .expect("All objects should have been added to the tracker!");
        let mut neg_row = -&pos_row;
        Self::_reduce_normalize(self.get_data(), &mut pos_row);
        Self::_reduce_normalize(self.get_data(), &mut neg_row);
        self.get_nonzero_mut().push(pos_row);
        self.get_nonzero_mut().push(neg_row);
    }

    fn is_better_reducer(v1: &Vector<i32>, v2: &Vector<i32>, col: usize) -> bool {
        v2[col] == 0 || (v1[col] != 0 && v1[col].abs() < v2[col].abs())
    }

    fn is_zero(t: &i32) -> bool {
        *t == 0
    }

    fn get_const_key(&self) -> i64 {
        self.const_key
    }
}

#[derive(Default, Clone)]
pub struct BoolLinearSolverBase {
    pub name_map: FxHashMap<i64, usize>,
    pub data: Vec<Vector<bool>>,
    pub nonzeros: Vec<Vector<bool>>,
    pub const_key: i64,
}

impl BoolLinearSolverBase {
    pub fn new(const_key: i64) -> BoolLinearSolverBase {
        BoolLinearSolverBase {
            name_map: hashmap!(const_key => 0),
            data: Vec::new(),
            nonzeros: Vec::new(),
            const_key,
        }
    }
}

impl LinearSolver<i64, bool> for BoolLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<i64, usize> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<i64, usize> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(&mut self) -> (&mut Vec<Vector<bool>>, &mut Vec<Vector<bool>>) {
        (&mut self.data, &mut self.nonzeros)
    }

    fn get_data(&self) -> &Vec<Vector<bool>> {
        &self.data
    }

    fn get_nonzero(&self) -> &Vec<Vector<bool>> {
        &self.nonzeros
    }

    fn reduce_with(reduced: &mut Vector<bool>, with: &Vector<bool>, col: usize) {
        if with[col] && reduced[col] {
            *reduced ^= with;
        }
    }
    fn reduce_row_with(rows: &mut Vec<Vector<bool>>, reduced: usize, with: usize, col: usize) {
        if rows[with][col] && rows[reduced][col] {
            let reducer = rows[with].clone();
            rows[reduced] ^= &reducer;
        }
    }

    fn normalize_col(_v: &mut Vector<bool>, _col: usize) {}

    fn is_better_reducer(v1: &Vector<bool>, _v2: &Vector<bool>, col: usize) -> bool {
        // All reducers are of the same value: Do they have 1 in the given position or not.
        v1[col]
    }

    fn is_zero(t: &bool) -> bool {
        !t
    }

    fn add_nonzero(&mut self, rel: FxHashMap<i64, bool>) {
        // Bool linear algebra trackers don't differentiate between relations and nonzeroes.
        let mut rel = rel.clone();
        *rel.entry(self.const_key).or_insert(false) ^= true;
        self.add_relation(rel);
    }

    fn contains_nonzero(&self, rel: FxHashMap<i64, bool>) -> bool {
        // Bool linear algebra trackers don't differentiate between relations and nonzeroes.
        let mut rel = rel.clone();
        *rel.entry(self.const_key).or_insert(false) ^= true;
        self.contains_relation(rel)
    }

    fn get_const_key(&self) -> i64 {
        self.const_key
    }
}

#[pyclass]
#[derive(Default, Clone)]
pub struct RLinearSolverBase {
    /// A map from the python indices to indices in the map.
    pub name_map: FxHashMap<i64, usize>,
    /// A list of all linear combinations known to be equal to 0.
    pub data: Vec<Vector<f64>>,
    /// A list of all linear combinations known to to be equal to 0.
    pub nonzeroes: Vec<Vector<f64>>,
    /// The key of the literal values.
    pub const_key: i64,
}

impl RLinearSolverBase {
    pub fn new(const_key: i64) -> RLinearSolverBase {
        RLinearSolverBase {
            name_map: hashmap!(const_key => 0),
            data: Vec::new(),
            nonzeroes: Vec::new(),
            const_key,
        }
    }
}

impl LinearSolver<i64, f64> for RLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<i64, usize> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<i64, usize> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(&mut self) -> (&mut Vec<Vector<f64>>, &mut Vec<Vector<f64>>) {
        (&mut self.data, &mut self.nonzeroes)
    }

    fn get_data(&self) -> &Vec<Vector<f64>> {
        &self.data
    }

    fn get_nonzero(&self) -> &Vec<Vector<f64>> {
        &self.nonzeroes
    }

    fn reduce_with(reduced: &mut Vector<f64>, with: &Vector<f64>, col: usize) {
        if !Self::is_zero(&with[col]) && !Self::is_zero(&reduced[col]) {
            let factor = reduced[col] / with[col];
            *reduced -= with * factor;
        }
    }
    fn reduce_row_with(rows: &mut Vec<Vector<f64>>, reduced: usize, with: usize, col: usize) {
        if !Self::is_zero(&rows[with][col]) && !Self::is_zero(&rows[reduced][col]) {
            let factor = rows[reduced][col] / rows[with][col];
            let f = &rows[with] * factor;
            rows[reduced] -= f;
        }
    }

    fn normalize_col(v: &mut Vector<f64>, col: usize) {
        if !Self::is_zero(&v[col].abs()) {
            *v /= v[col];
            assert_eq!(v[col], 1.);
        }
    }

    fn is_better_reducer(v1: &Vector<f64>, v2: &Vector<f64>, col: usize) -> bool {
        v1[col].abs() > v2[col].abs()
    }

    fn is_zero(t: &f64) -> bool {
        t.abs() < 1e-9
    }

    fn get_const_key(&self) -> i64 {
        self.const_key
    }
}

#[pyclass]
pub struct RLinearSolver {
    solver: RLinearSolverBase,
}

#[pymethods]
impl RLinearSolver {
    #[new]
    pub fn new(const_key: i64) -> RLinearSolver {
        RLinearSolver {
            solver: RLinearSolverBase::new(const_key),
        }
    }

    fn add_objects(&mut self, objects: Vec<i64>) {
        self.solver.add_objects(objects);
    }

    fn reduce(&self, v: Vec<f64>) -> Vec<f64> {
        let mut v = Vector::new(v);
        self.solver.reduce(&mut v);
        v.data
    }

    fn reduce_rel(&self, rel: FxHashMap<i64, f64>) -> Vec<f64> {
        let mut data = vec![0.; self.solver.len()];
        for (key, val) in rel {
            data[*self
                .solver
                .get_map()
                .get(&key)
                .expect("RLinearSolver::reduce_rel: Solver is missing a key in the relation!")] +=
                val;
        }
        self.reduce(data)
    }

    fn add_relation(&mut self, rel: FxHashMap<i64, f64>) {
        self.solver.add_relation(rel)
    }

    fn contains_relation(&self, rel: FxHashMap<i64, f64>) -> bool {
        self.solver.contains_relation(rel)
    }

    fn add_nonzero(&mut self, rel: FxHashMap<i64, f64>) {
        self.solver.add_nonzero(rel)
    }

    fn contains_nonzero(&self, rel: FxHashMap<i64, f64>) -> bool {
        self.solver.contains_nonzero(rel)
    }

    fn contains(&self, key: i64) -> bool {
        self.solver.contains(&key)
    }

    fn clone(&self) -> RLinearSolver {
        RLinearSolver {
            solver: self.solver.clone(),
        }
    }

    /// Gathers all relations of the solver for Python.
    fn relations(&self) -> Vec<Vec<f64>> {
        self.solver
            .data
            .iter()
            .map(|v| v.data.clone())
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn nonzeroes(&self) -> Vec<Vec<f64>> {
        self.solver
            .nonzeroes
            .iter()
            .map(|v| v.data.clone())
            .collect_vec()
    }

    /// Gethers all relations of the solver for Python.
    fn indices(&self) -> FxHashMap<i64, usize> {
        self.solver.name_map.clone()
    }

    /// Checks if a value is known.
    fn get_value(&self, rel: FxHashMap<i64, f64>) -> Option<f64> {
        self.solver.get_value(rel)
    }

    fn find_combinations(
        &self,
        coefficients: Vec<f64>,
        const_coef: f64,
        coef_keys: Vec<Vec<i64>>,
    ) -> Vec<Vec<i64>> {
        self.solver
            .find_combinations(coefficients, const_coef, coef_keys)
    }
}

#[pyclass]
pub struct ModLinearSolver {
    solver: ModLinearSolverBase,
}

#[pymethods]
impl ModLinearSolver {
    #[new]
    fn new(const_key: i64) -> ModLinearSolver {
        ModLinearSolver {
            solver: ModLinearSolverBase::new(const_key),
        }
    }

    fn add_objects(&mut self, objects: Vec<i64>) {
        self.solver.add_objects(objects);
    }

    fn reduce(&self, v: Vec<i32>) -> Vec<i32> {
        let mut v = Vector::new(v);
        self.solver.reduce(&mut v);
        v.data
    }

    fn reduce_rel(&self, rel: FxHashMap<i64, i32>) -> Vec<i32> {
        let mut data = vec![0; self.solver.len()];
        for (key, val) in rel {
            data[*self.solver.get_map().get(&key).expect(
                "ModLinearSolver::reduce_rel: Linear solver is missing a key in the relation!",
            )] += val;
        }
        self.reduce(data)
    }

    fn add_relation(&mut self, rel: FxHashMap<i64, i32>) {
        self.solver.add_relation(rel)
    }

    fn contains_relation(&self, rel: FxHashMap<i64, i32>) -> bool {
        self.solver.contains_relation(rel)
    }

    fn add_nonzero(&mut self, rel: FxHashMap<i64, i32>) {
        self.solver.add_nonzero(rel)
    }

    fn contains_nonzero(&self, rel: FxHashMap<i64, i32>) -> bool {
        self.solver.contains_nonzero(rel)
    }

    fn contains(&self, key: i64) -> bool {
        self.solver.contains(&key)
    }

    fn clone(&self) -> ModLinearSolver {
        ModLinearSolver {
            solver: self.solver.clone(),
        }
    }

    /// Gethers all relations of the solver for Python.
    fn relations(&self) -> Vec<Vec<i32>> {
        self.solver
            .data
            .iter()
            .map(|v| v.data.clone())
            .collect_vec()
    }

    /// Gethers all relations of the solver for Python.
    fn nonzeroes(&self) -> Vec<Vec<i32>> {
        self.solver
            .nonzeroes
            .iter()
            .map(|v| v.data.clone())
            .collect_vec()
    }

    /// Gethers all relations of the solver for Python.
    fn indices(&self) -> FxHashMap<i64, usize> {
        self.solver.name_map.clone()
    }

    /// Checks if a value is known.
    fn get_value(&self, rel: FxHashMap<i64, i32>) -> Option<i32> {
        self.solver.get_value(rel)
    }

    fn find_combinations(
        &self,
        coefficients: Vec<i32>,
        const_coef: i32,
        coef_keys: Vec<Vec<i64>>,
    ) -> Vec<Vec<i64>> {
        self.solver
            .find_combinations(coefficients, const_coef, coef_keys)
    }
}

#[pyclass]
pub struct BoolLinearSolver {
    solver: BoolLinearSolverBase,
}

#[pymethods]
impl BoolLinearSolver {
    #[new]
    fn new(const_key: i64) -> BoolLinearSolver {
        BoolLinearSolver {
            solver: BoolLinearSolverBase::new(const_key),
        }
    }

    fn add_objects(&mut self, objects: Vec<i64>) {
        self.solver.add_objects(objects);
    }

    fn reduce(&self, v: Vec<bool>) -> Vec<bool> {
        let mut v = Vector::new(v);
        self.solver.reduce(&mut v);
        v.data
    }

    fn reduce_rel(&self, rel: FxHashMap<i64, bool>) -> Vec<bool> {
        let mut data = vec![false; self.solver.len()];
        for (key, val) in rel {
            data[*self.solver.get_map().get(&key).expect(
                "BoolLinearSolver::reduce_rel: BoolLinearSolver is missing a key in the relation!",
            )] ^= val;
        }
        self.reduce(data)
    }

    fn add_relation(&mut self, rel: FxHashMap<i64, bool>) {
        self.solver.add_relation(rel)
    }

    fn contains_relation(&self, rel: FxHashMap<i64, bool>) -> bool {
        self.solver.contains_relation(rel)
    }

    fn add_nonzero(&mut self, rel: FxHashMap<i64, bool>) {
        self.solver.add_nonzero(rel)
    }

    fn contains_nonzero(&self, rel: FxHashMap<i64, bool>) -> bool {
        self.solver.contains_nonzero(rel)
    }

    fn contains(&self, key: i64) -> bool {
        self.solver.contains(&key)
    }

    fn clone(&self) -> BoolLinearSolver {
        BoolLinearSolver {
            solver: self.solver.clone(),
        }
    }

    /// Gethers all relations of the solver for Python.
    fn relations(&self) -> Vec<Vec<bool>> {
        self.solver
            .data
            .iter()
            .map(|v| v.data.clone())
            .collect_vec()
    }

    /// Gethers all relations of the solver for Python.
    fn nonzeroes(&self) -> Vec<Vec<bool>> {
        // Note that the nonzeroes are just the complements of all relations.
        let idx = *self
            .solver
            .name_map
            .get(&self.solver.const_key)
            .expect("Solver does not have a const key!");
        self.solver
            .data
            .iter()
            .map(|v| {
                let mut res = v.data.clone();
                res[idx] ^= true;
                res
            })
            .collect_vec()
    }

    /// Gethers all relations of the solver for Python.
    fn indices(&self) -> FxHashMap<i64, usize> {
        self.solver.name_map.clone()
    }

    /// Checks if a value is known.
    fn get_value(&self, rel: FxHashMap<i64, bool>) -> Option<bool> {
        self.solver.get_value(rel)
    }

    fn find_combinations(
        &self,
        coefficients: Vec<bool>,
        const_coef: bool,
        coef_keys: Vec<Vec<i64>>,
    ) -> Vec<Vec<i64>> {
        self.solver
            .find_combinations(coefficients, const_coef, coef_keys)
    }
}

#[allow(unused_imports)]
mod linear_tests {
    use rustc_hash::FxHashMap;

    use super::{LinearSolver, ModLinearSolverBase, RLinearSolverBase};
    use crate::{hashmap, linear::dense_vec::Vector};

    #[test]
    pub fn test_stuff() {
        let mut solv = ModLinearSolverBase::default();
        solv.add_objects(vec![1, 2, 3, 3]);
        assert_eq!(solv.name_map.len(), 3);
        solv.add_objects(vec![1, 4]);
        assert_eq!(solv.name_map.len(), 4);
    }
    #[test]
    pub fn test_echelonization() {
        let mut solv = ModLinearSolverBase::default();

        solv.add_relation([(0, 1), (1, 3), (2, 2)].into_iter().collect());
        solv.add_relation([(0, 5), (1, 2), (2, 1)].into_iter().collect());

        assert_eq!(solv.data[0], Vector::new(vec![-13, 0, 1]));
        assert_eq!(solv.data[1], Vector::new(vec![-9, -1, 0]));
    }

    #[test]
    pub fn test_nonzero_mod() {
        let mut solv = ModLinearSolverBase::new(0);
        solv.add_objects(vec![0]);
        solv.add_relation(hashmap!(0 => 180));

        assert!(!solv.contains_nonzero(hashmap!(0 => 0)));
        assert!(!solv.contains_nonzero(hashmap!(0 => 180)));
        assert!(solv.contains_nonzero(hashmap!(0 => 1)));
        assert!(solv.contains_nonzero(hashmap!(0 => 12)));
        solv.add_nonzero(hashmap!(0 => 90));
        solv.add_relation(hashmap!(0 => 90));
        assert!(solv.contains_nonzero(hashmap!()));
    }

    #[test]
    pub fn test_nonzero_r() {
        let mut solv = RLinearSolverBase::new(0);
        solv.add_objects(vec![0, 1]);
        solv.add_nonzero(hashmap!(0 => 1.));
        solv.add_relation(hashmap!(1 => 1.));
        solv.add_relation(hashmap!(0 => 90., 1 => 1.));
        assert!(solv.contains_nonzero(hashmap!()));
    }
}
