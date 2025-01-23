use itertools::Itertools;
use pyo3::prelude::*;
use rand::{thread_rng, Rng};
use rustc_hash::FxHashMap;
use std::cmp::Ordering;
use std::fmt::Debug;
use std::hash::Hash;
use std::{mem, vec};

use super::sparse_vec::{SparseVecType, SparseVector};
use crate::{hashmap, HashType, MonType};

/// A trait implementing the shared behavior of a linear algebra system,
/// operating on Euclidean Domains.
///
/// Vectors in the module or vector space handled by the system are stored as a list of monomials,
/// sorted by an arbitrary consistent order.
///
/// The sparse linear algebra system whose behavior is implemented by the trait must provide:
/// 1. A map from top monomials to the unique vector in the reduced basis with the given top monomial.
/// Uniqueness is guaranteed since in a PID, if there are several vectors with the same top monomial,
/// there exists a vector in the module where the coefficient of the top monomial is the generator of
/// the ideal formed by the coefficients of the given vectors, and that vector can be used to reduce all other vectors.
/// The vectors in the map are stored in a fully-reduced mode:
/// For any monomial `c_1*M` in a vector that is the top monomial `c_2*M` of another vector,
/// the coefficient `c_1` is chosen to be a canonical representative in the domain modulo `c_2`
///
/// 2. A map from top monomials to combinations of variables that are known not ot be zero,
/// whose top monomial is the given variable. The coefficient of the top monomial of all such vectors is
/// chosen to be a canonical representative modulo multiplication by a unit.
///
/// The constant key is the key representing the degree-0 coefficient of the vector:
/// The vector `5x+3` would be stored as `[(3, constant_key), (5, x_key)]`
///
/// The trait can be extended to Principal Ideal Domains, by overriding interreduce.
pub trait SparseLinearSolver<
    OuterKey: PartialEq + Eq + Hash + Clone,
    Mon: PartialEq + Eq + Hash + Clone + Copy + Ord + Debug + TryFrom<usize> + Default,
    Scalar: Default + Clone + Debug + PartialEq + SparseVecType,
>
{
    /// Gets the index of the constant element.
    /// The vector `5x+3` would be stored as `[(3, constant_key), (5, x_key)]`
    fn get_const_key(&self) -> OuterKey;
    /// Gets a mutable reference to map mapping outer variables to indernal monomials.
    /// A vector `5x + 3y`, where `x` and `y` are some variables,
    /// would be stored as `[(5, map(x)), (3, map(y))]`.
    ///
    /// TODO: Replace the map with a bijection.
    fn get_map_mut(&mut self) -> &mut FxHashMap<OuterKey, Mon>;
    /// Gets a mutable reference to map mapping outer variables.
    /// A vector `5x + 3y`, where `x` and `y` are some variables,
    /// would be stored as `[(5, map(x)), (3, map(y))]`.
    ///
    /// TODO: Replace the map with a bijection.
    fn get_map(&self) -> &FxHashMap<OuterKey, Mon>;
    /// Gets a mutable reference to the both the basis and the nozeroes.
    /// This is a safe version of (self.get_map_mut(), self.get_nonzero_mut()).
    fn get_data_and_nonzero_mut(
        &mut self,
    ) -> (
        &mut FxHashMap<Mon, SparseVector<Mon, Scalar>>,
        &mut FxHashMap<Mon, Vec<SparseVector<Mon, Scalar>>>,
    );
    /// Gets a reference to map mapping outer variables to indernal monomials.
    /// A vector `5x + 3y`, where `x` and `y` are some variables,
    /// would be stored as `[(5, map(x)), (3, map(y))]`.
    ///
    /// TODO: Replace the map with a bijection.
    fn get_data(&self) -> &FxHashMap<Mon, SparseVector<Mon, Scalar>>;
    /// Gets the nonzero array.
    fn get_nonzero(&self) -> &FxHashMap<Mon, Vec<SparseVector<Mon, Scalar>>>;
    /// Checks which vector is the better reducer.
    fn better_reducer(v1: &SparseVector<Mon, Scalar>, v2: &SparseVector<Mon, Scalar>) -> Ordering;
    /// Checks if the given value is zero, or sufficiently close to 0.
    fn is_zero(t: &Scalar) -> bool;
    /// Reduces the first vector with the second vector, usizng the given column.
    fn reduce_with(reduced: &mut SparseVector<Mon, Scalar>, with: &SparseVector<Mon, Scalar>);
    /// Reduces two vectors with each other, so that the coefficient of the top monomial of one is the generator of the ideal of t
    fn interreduce(
        generator: &mut SparseVector<Mon, Scalar>,
        reduced: &mut SparseVector<Mon, Scalar>,
    ) {
        if reduced.top_monomial() != generator.top_monomial() {
            return;
        }

        // Making sure that the generator is worse reducer.
        if let Ordering::Less = Self::better_reducer(generator, reduced) {
            mem::swap(generator, reduced);
        }
        while !reduced.is_zero() && reduced.top_monomial() == generator.top_monomial() {
            // The generator becomes the better reducer.
            mem::swap(reduced, generator);
            Self::reduce_with(reduced, generator);
        }
    }

    /// Transforms a vector to a canonical form.
    fn normalize(v: &mut SparseVector<Mon, Scalar>);

    /// Gets the index of the constant factor.
    fn get_const_idx(&self) -> Mon {
        *self
            .get_map()
            .get(&self.get_const_key())
            .expect("LinearSolver::get_const_idx: Solver does not have a const key!")
    }

    /// Checks if the given relation has a single known value.
    fn get_value(&self, rel: FxHashMap<OuterKey, Scalar>) -> Option<Scalar> {
        let mut row = self.make_row(rel)?;
        self.reduce(&mut row);

        if row.len() == 0 {
            Some(Scalar::default())
        } else if row.len() == 1 {
            let (mon, val) = row.data[0].clone();
            if mon == self.get_const_idx() {
                Some(val)
            } else {
                None
            }
        } else {
            None
        }
    }

    /// Gets a mutable reference to the data array.
    fn get_data_mut(&mut self) -> &mut FxHashMap<Mon, SparseVector<Mon, Scalar>> {
        self.get_data_and_nonzero_mut().0
    }

    /// Gets a mutable reference to the nonzero array.
    fn get_nonzero_mut(&mut self) -> &mut FxHashMap<Mon, Vec<SparseVector<Mon, Scalar>>> {
        self.get_data_and_nonzero_mut().1
    }

    /// Adds new objects to the linear solver.
    fn add_objects(&mut self, new_objs: impl IntoIterator<Item = OuterKey>) {
        let map = self.get_map_mut();
        for obj in new_objs {
            if !map.contains_key(&obj) {
                map.insert(obj, Mon::try_from(map.len()).ok().expect("Failed to create index for an object! This is likely caused by having more than 2^16 objects in the linear tracker."));
            }
        }
    }

    /// Adds a new nonzero identity to the linear algebra tracker.
    fn add_nonzero(&mut self, rel: FxHashMap<OuterKey, Scalar>) {
        self.add_objects(rel.keys().cloned());
        let mut row = self
            .make_row(rel)
            .expect("All objects should have been added to the tracker!");
        Self::_reduce_normalize(self.get_data(), &mut row);
        if let Some(mon) = row.top_monomial() {
            self.get_nonzero_mut().entry(mon).or_default().push(row);
        } else {
            // If we have found that 0 is nonzero, we mark a contradiction.
            *self.contradiction_mut() = true;
            return;
        }
    }

    /// Adds a new relation to the linear algebra tracker.
    fn add_relation(&mut self, rel: FxHashMap<OuterKey, Scalar>) {
        self.add_objects(rel.keys().cloned().collect_vec());

        let mut row = self
            .make_row(rel)
            .expect("All objects should have been added to the tracker!");

        let (data, nonzeros) = self.get_data_and_nonzero_mut();

        // Inserting the row to the data, while possibly breaking the full reduction of everything.
        while let Some(mon) = row.top_monomial() {
            let Some(reducer) = data.get_mut(&mon) else {
                break;
            };
            Self::interreduce(reducer, &mut row);
        }

        if let Some(mon) = row.top_monomial() {
            // If the row is nonzero, we add it.
            assert!(!data.contains_key(&mon));
            data.insert(mon, row);
        }

        // Finding vectors that now have to be fully reduced. This requires a full iteration over the data.
        let affected = data
            .iter()
            .filter_map(|(mon, row)| {
                assert_eq!(row.top_monomial().unwrap(), *mon);
                if row
                    .iter()
                    .any(|(curr_mon, _)| curr_mon != mon && data.contains_key(curr_mon))
                {
                    Some(*mon)
                } else {
                    None
                }
            })
            .collect_vec();

        // Going over the rows by order of ascending top monomial.
        for top_mon in affected.iter().copied() {
            let mut row = data.remove(&top_mon).unwrap();
            Self::_reduce(data, &mut row);
            if let Some(mon) = row.top_monomial() {
                data.insert(mon, row);
            }
        }

        let mut affected = Vec::new();
        let mons = nonzeros.keys().copied().collect_vec();
        for mon in mons {
            let v = nonzeros.get_mut(&mon).unwrap();
            let mut mon_affected = false;
            for i in (0..v.len()).rev() {
                if v[i].iter().any(|(mon, _)| data.contains_key(mon)) {
                    mon_affected = true;
                    Self::_reduce_normalize(&data, &mut v[i]);
                    if v[i].top_monomial() != Some(mon) {
                        affected.push(v.swap_remove(i));
                    }
                }
            }
            if mon_affected {
                v.dedup();
            }
        }
        nonzeros.retain(|_, v| !v.is_empty());
        for v in affected {
            let Some(mon) = v.top_monomial() else {
                *self.contradiction_mut() = true;
                break;
            };
            nonzeros.entry(mon).or_default().push(v);
        }
    }

    /// Returns the number of objects tracked by the linear algebra solver.
    fn len(&self) -> usize {
        self.get_map().len()
    }

    /// Reduces a vector given a list of relations.
    ///
    /// Parameters:
    /// * `relations`: An echelonized map of the relations. Since we work in euclidean domains, the vectors of the relations should be of length 1,
    ///                 and every reduction should be done in a single attempt.
    /// * `v`:
    fn _reduce(
        relations: &FxHashMap<Mon, SparseVector<Mon, Scalar>>,
        v: &mut SparseVector<Mon, Scalar>,
    ) {
        // Doing top reductions.
        loop {
            let Some(mon) = v.top_monomial() else {
                return;
            };
            let Some(reducer) = relations.get(&mon) else {
                break;
            };
            Self::reduce_with(v, reducer);

            // Checking if the reduction had failed.
            if v.top_monomial()
                .map(|new_mon| new_mon == mon)
                .unwrap_or_default()
            {
                break;
            }
        }
        // Reducing the rest of the monomials.
        let Some(mut curr_mon) = v.top_monomial() else {
            return;
        };

        while let Some((below_mon, _)) = v.next_largest_item(curr_mon).map(Clone::clone) {
            curr_mon = below_mon;
            let Some(reducer) = relations.get(&below_mon) else {
                continue;
            };
            Self::reduce_with(v, reducer);
        }
    }

    /// Reduces a vector given a list of relations.
    /// Normalizes the rightmost nonzero value of the vector to ensure it is reduced to canonical form.
    fn _reduce_normalize(
        relations: &FxHashMap<Mon, SparseVector<Mon, Scalar>>,
        v: &mut SparseVector<Mon, Scalar>,
    ) {
        Self::_reduce(relations, v);
        Self::normalize(v);
        Self::_reduce(relations, v);
    }

    /// Reduces a vector to the canonical form.
    /// The result of the reduction must be the canonical representative.
    fn reduce(&self, v: &mut SparseVector<Mon, Scalar>) {
        Self::_reduce(self.get_data(), v);
    }

    /// Converts a dictionary to a vector.
    fn make_row(&self, rel: FxHashMap<OuterKey, Scalar>) -> Option<SparseVector<Mon, Scalar>> {
        let mut data = Vec::new();
        for (key, val) in rel {
            if !Self::is_zero(&val) {
                data.push((*self.get_map().get(&key)?, val));
            }
        }
        Some(SparseVector::new(data))
    }

    /// Checks if the linear algebra solver contains the given nonzero relation.
    fn contains_nonzero(&self, rel: FxHashMap<OuterKey, Scalar>) -> bool {
        if self.contradiction() {
            return true;
        }
        let Some(mut data) = self.make_row(rel) else {
            return false;
        };
        Self::_reduce_normalize(self.get_data(), &mut data);
        let Some(mon) = data.top_monomial() else {
            return false;
        };
        // If the value of the vector is known (e.g. is 12) it is nonzero.
        if mon == self.get_const_idx() && data.len() == 1 {
            return true;
        }

        let Some(nonz) = self.get_nonzero().get(&mon) else {
            return false;
        };
        return nonz.contains(&data);
    }

    /// Checks if the linear algebra solver contains the given relation.
    fn contains_relation(&self, rel: FxHashMap<OuterKey, Scalar>) -> bool {
        let Some(mut data) = self.make_row(rel) else {
            return false;
        };
        self.reduce(&mut data);
        data.is_zero()
    }

    /// Checks if the tracker tracks the given object.
    fn contains(&self, key: &OuterKey) -> bool {
        self.get_map().contains_key(key)
    }

    fn find_combinations(
        &self,
        coefficients: Vec<Scalar>,
        const_coef: Scalar,
        coef_keys: Vec<Vec<OuterKey>>,
    ) -> Vec<Vec<OuterKey>>
    where
        Scalar: ToHash,
    {
        debug_assert_eq!(coefficients.len(), coef_keys.len());
        let mut rng = thread_rng();

        let all_keys = coef_keys.iter().cloned().flatten().unique().collect_vec();

        // Generating the hashes.
        let mut outer_hashes = FxHashMap::default();
        let mut inner_hashes = FxHashMap::default();

        for (outer, inner) in self.get_map() {
            let hash = rng.gen::<HashType>();
            outer_hashes.insert(outer.clone(), hash);
            inner_hashes.insert(*inner, hash);
        }

        for v in &coef_keys {
            for outer in v {
                outer_hashes
                    .entry(outer.clone())
                    .or_insert(rng.gen::<HashType>());
            }
        }

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
            let mut vec_acc = SparseVector::new(vec![(const_idx, const_coef.clone())]);
            let mut scalar_acc: HashType = 0;
            for (key, coef) in neg_comb.iter().zip(coefficients.iter()) {
                if let Some(v) = reduced_singles.get(key) {
                    vec_acc += v * coef.clone();
                } else {
                    scalar_acc = scalar_acc.wrapping_add(outer_hashes
                            .get(key)
                            .expect("CombinationFind::find_combinations: All objects should have a hash!")
                            .wrapping_mul(coef.to_hash()));
                }
            }
            self.reduce(&mut vec_acc);
            let vec_acc = vec_acc
                .iter()
                .map(|(mon, coef)| coef.to_hash().wrapping_mul(*inner_hashes.get(mon).unwrap()))
                .sum::<HashType>();

            let total = vec_acc.wrapping_add(scalar_acc);
            db.entry(total).or_insert(Vec::new()).push(neg_comb);
        }

        let mut res = Vec::new();

        for pos_comb in pos_combinations.iter().multi_cartesian_product() {
            let mut vec_acc = SparseVector::new(Vec::new());
            let mut scalar_acc: HashType = 0;
            for (key, coef) in pos_comb.iter().zip(coefficients[db_size..].iter()) {
                if let Some(v) = reduced_singles.get(key) {
                    vec_acc -= v * coef.clone();
                } else {
                    scalar_acc = scalar_acc.wrapping_sub(outer_hashes
                            .get(key)
                            .expect("CombinationFind::find_combinations: All objects should have a hash!")
                            .wrapping_mul(coef.to_hash()),
                        );
                }
            }

            self.reduce(&mut vec_acc);
            let vec_acc = vec_acc
                .iter()
                .map(|(mon, coef)| coef.to_hash().wrapping_mul(*inner_hashes.get(mon).unwrap()))
                .sum::<HashType>();
            let total = vec_acc.wrapping_add(scalar_acc);

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

    fn contradiction(&self) -> bool;

    fn contradiction_mut(&mut self) -> &mut bool;
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

#[derive(Default, Clone)]
pub struct ModSparseLinearSolverBase {
    pub name_map: FxHashMap<HashType, MonType>,
    pub data: FxHashMap<MonType, SparseVector<MonType, i32>>,
    /// A list of all linear combinations known to to be equal to 0.
    pub nonzeroes: FxHashMap<MonType, Vec<SparseVector<MonType, i32>>>,
    pub const_key: HashType,
    /// Whether we have found a contradiction.
    pub contradiction: bool,
}

impl ModSparseLinearSolverBase {
    pub fn new(const_key: HashType) -> ModSparseLinearSolverBase {
        ModSparseLinearSolverBase {
            name_map: hashmap!(const_key => 0),
            data: FxHashMap::default(),
            nonzeroes: FxHashMap::default(),
            const_key,
            contradiction: false,
        }
    }
}

impl SparseLinearSolver<HashType, MonType, i32> for ModSparseLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<HashType, MonType> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<HashType, MonType> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(
        &mut self,
    ) -> (
        &mut FxHashMap<MonType, SparseVector<MonType, i32>>,
        &mut FxHashMap<MonType, Vec<SparseVector<MonType, i32>>>,
    ) {
        (&mut self.data, &mut self.nonzeroes)
    }

    fn get_data(&self) -> &FxHashMap<MonType, SparseVector<MonType, i32>> {
        &self.data
    }

    fn get_nonzero(&self) -> &FxHashMap<MonType, Vec<SparseVector<MonType, i32>>> {
        &self.nonzeroes
    }

    fn reduce_with(reduced: &mut SparseVector<MonType, i32>, with: &SparseVector<MonType, i32>) {
        let Some(mon) = with.top_monomial() else {
            return;
        };
        let Some(&val) = reduced.coefficient(&mon) else {
            return;
        };

        let factor = -val.div_euclid(with.top_coefficient().unwrap());

        *reduced += with * factor;
    }

    fn better_reducer(
        v1: &SparseVector<MonType, i32>,
        v2: &SparseVector<MonType, i32>,
    ) -> Ordering {
        let Some((_, c1)) = v1.data.last() else {
            return Ordering::Greater;
        };
        let Some((_, c2)) = v2.data.last() else {
            return Ordering::Less;
        };
        return c1.cmp(&c2);
    }

    fn is_zero(t: &i32) -> bool {
        *t == 0
    }

    fn get_const_key(&self) -> HashType {
        self.const_key
    }

    fn normalize(v: &mut SparseVector<MonType, i32>) {
        let Some(coef) = v.top_coefficient() else {
            return;
        };
        if coef.is_negative() {
            *v *= -1;
        }
    }

    fn contradiction(&self) -> bool {
        self.contradiction
    }

    fn contradiction_mut(&mut self) -> &mut bool {
        &mut self.contradiction
    }
}

#[derive(Default, Clone)]
pub struct BoolSparseLinearSolverBase {
    pub name_map: FxHashMap<HashType, MonType>,
    pub data: FxHashMap<MonType, SparseVector<MonType, bool>>,
    pub nonzeros: FxHashMap<MonType, Vec<SparseVector<MonType, bool>>>,
    pub const_key: HashType,
    /// Whether we have found a contradiction.
    pub contradiction: bool,
    pub found_false: bool,
}

impl BoolSparseLinearSolverBase {
    pub fn new(const_key: HashType) -> BoolSparseLinearSolverBase {
        BoolSparseLinearSolverBase {
            name_map: hashmap!(const_key => 0),
            data: FxHashMap::default(),
            nonzeros: FxHashMap::default(),
            const_key,
            contradiction: false,
            found_false: false,
        }
    }
}

impl SparseLinearSolver<HashType, MonType, bool> for BoolSparseLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<HashType, MonType> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<HashType, MonType> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(
        &mut self,
    ) -> (
        &mut FxHashMap<MonType, SparseVector<MonType, bool>>,
        &mut FxHashMap<MonType, Vec<SparseVector<MonType, bool>>>,
    ) {
        (&mut self.data, &mut self.nonzeros)
    }

    fn get_data(&self) -> &FxHashMap<MonType, SparseVector<MonType, bool>> {
        &self.data
    }

    fn get_nonzero(&self) -> &FxHashMap<MonType, Vec<SparseVector<MonType, bool>>> {
        &self.nonzeros
    }

    fn reduce_with(reduced: &mut SparseVector<MonType, bool>, with: &SparseVector<MonType, bool>) {
        let Some(mon) = with.top_monomial() else {
            return;
        };
        if reduced.coefficient(&mon).is_none() {
            return;
        }
        *reduced += with;
    }

    fn better_reducer(
        v1: &SparseVector<MonType, bool>,
        _: &SparseVector<MonType, bool>,
    ) -> Ordering {
        // All reducers are of the same value: Do they have 1 in the given position or not.
        if let Some((_, c1)) = v1.data.last() {
            if *c1 {
                return Ordering::Less;
            }
        }
        Ordering::Greater
    }

    fn is_zero(t: &bool) -> bool {
        !t
    }

    fn add_nonzero(&mut self, rel: FxHashMap<HashType, bool>) {
        // Bool linear algebra trackers don't differentiate between relations and nonzeroes.
        let mut rel = rel.clone();
        *rel.entry(self.const_key).or_insert(false) ^= true;
        self.add_relation(rel);
    }

    fn contains_nonzero(&self, rel: FxHashMap<HashType, bool>) -> bool {
        // Bool linear algebra trackers don't differentiate between relations and nonzeroes.
        let mut rel = rel.clone();
        *rel.entry(self.const_key).or_insert(false) ^= true;
        self.contains_relation(rel)
    }

    fn get_const_key(&self) -> HashType {
        self.const_key
    }

    fn normalize(_: &mut SparseVector<MonType, bool>) {}

    fn contradiction(&self) -> bool {
        self.contradiction
    }

    fn contradiction_mut(&mut self) -> &mut bool {
        &mut self.contradiction
    }
}

#[derive(Default, Clone)]
pub struct RSparseLinearSolverBase {
    /// A map from the python indices to indices in the map.
    pub name_map: FxHashMap<HashType, MonType>,
    /// A list of all linear combinations known to be equal to 0.
    pub data: FxHashMap<MonType, SparseVector<MonType, f64>>,
    /// A list of all linear combinations known to to be equal to 0.
    pub nonzeroes: FxHashMap<MonType, Vec<SparseVector<MonType, f64>>>,
    /// The key of the literal values.
    pub const_key: HashType,
    /// Whether we have found a contradiction.
    pub contradiction: bool,
}

impl RSparseLinearSolverBase {
    pub fn new(const_key: HashType) -> RSparseLinearSolverBase {
        RSparseLinearSolverBase {
            name_map: hashmap!(const_key => 0),
            data: FxHashMap::default(),
            nonzeroes: FxHashMap::default(),
            const_key,
            contradiction: false,
        }
    }
}

impl SparseLinearSolver<HashType, MonType, f64> for RSparseLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<HashType, MonType> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<HashType, MonType> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(
        &mut self,
    ) -> (
        &mut FxHashMap<MonType, SparseVector<MonType, f64>>,
        &mut FxHashMap<MonType, Vec<SparseVector<MonType, f64>>>,
    ) {
        (&mut self.data, &mut self.nonzeroes)
    }

    fn get_data(&self) -> &FxHashMap<MonType, SparseVector<MonType, f64>> {
        &self.data
    }

    fn get_nonzero(&self) -> &FxHashMap<MonType, Vec<SparseVector<MonType, f64>>> {
        &self.nonzeroes
    }

    fn reduce_with(reduced: &mut SparseVector<MonType, f64>, with: &SparseVector<MonType, f64>) {
        let Some(mon) = with.top_monomial() else {
            return;
        };
        let Some(&val) = reduced.coefficient(&mon) else {
            return;
        };

        let factor = -val / with.top_coefficient().unwrap();
        *reduced += with * factor;
    }

    fn better_reducer(
        v1: &SparseVector<MonType, f64>,
        v2: &SparseVector<MonType, f64>,
    ) -> Ordering {
        // Zero is the worst reducer.
        let Some((_, c1)) = v1.data.last() else {
            return Ordering::Greater;
        };
        let Some((_, c2)) = v2.data.last() else {
            return Ordering::Less;
        };
        c1.abs().total_cmp(&c2.abs())
    }

    fn is_zero(t: &f64) -> bool {
        t.abs() < 1e-9
    }

    fn get_const_key(&self) -> HashType {
        self.const_key
    }

    fn normalize(v: &mut SparseVector<MonType, f64>) {
        let Some(coef) = v.top_coefficient() else {
            return;
        };
        *v *= coef.recip();
    }

    fn contradiction(&self) -> bool {
        self.contradiction
    }

    fn contradiction_mut(&mut self) -> &mut bool {
        &mut self.contradiction
    }
}

#[pyclass]
pub struct RSparseLinearSolver {
    solver: RSparseLinearSolverBase,
}

#[pymethods]
impl RSparseLinearSolver {
    #[new]
    pub fn new(const_key: HashType) -> RSparseLinearSolver {
        RSparseLinearSolver {
            solver: RSparseLinearSolverBase::new(const_key),
        }
    }

    fn add_relation(&mut self, rel: FxHashMap<HashType, f64>) {
        self.solver.add_relation(rel)
    }

    fn contains_relation(&self, rel: FxHashMap<HashType, f64>) -> bool {
        self.solver.contains_relation(rel)
    }

    fn add_nonzero(&mut self, rel: FxHashMap<HashType, f64>) {
        self.solver.add_nonzero(rel)
    }

    fn contains_nonzero(&self, rel: FxHashMap<HashType, f64>) -> bool {
        self.solver.contains_nonzero(rel)
    }

    fn contains(&self, key: HashType) -> bool {
        self.solver.contains(&key)
    }

    fn clone(&self) -> RSparseLinearSolver {
        RSparseLinearSolver {
            solver: self.solver.clone(),
        }
    }

    /// Gathers all relations of the solver for Python.
    fn relations(&self) -> Vec<Vec<(HashType, f64)>> {
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        self.solver
            .data
            .values()
            .map(|v| {
                v.data
                    .iter()
                    .map(|(mon, coef)| (*rev_map.get(mon).unwrap(), *coef))
                    .collect_vec()
            })
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn nonzeroes(&self) -> Vec<Vec<(HashType, f64)>> {
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        self.solver
            .nonzeroes
            .values()
            .map(|v| v.iter())
            .flatten()
            .map(|v| {
                v.data
                    .iter()
                    .map(|(mon, coef)| (*rev_map.get(mon).unwrap(), *coef))
                    .collect_vec()
            })
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn indices(&self) -> FxHashMap<HashType, MonType> {
        self.solver.name_map.clone()
    }

    /// Checks if a value is known.
    fn get_value(&self, rel: FxHashMap<HashType, f64>) -> Option<f64> {
        self.solver.get_value(rel)
    }

    fn find_combinations(
        &self,
        coefficients: Vec<f64>,
        const_coef: f64,
        coef_keys: Vec<Vec<HashType>>,
    ) -> Vec<Vec<HashType>> {
        self.solver
            .find_combinations(coefficients, const_coef, coef_keys)
    }

    /// Reduces the given vector modulo the relations of the linear algebra tracker.
    fn reduce(&self, rel: FxHashMap<HashType, f64>) -> FxHashMap<HashType, f64> {
        let mut v = self.solver.make_row(rel).unwrap();
        self.solver.reduce(&mut v);
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        v.iter()
            .map(|(m, v)| (*rev_map.get(m).unwrap(), *v))
            .collect()
    }
}

#[pyclass]
pub struct ModSparseLinearSolver {
    solver: ModSparseLinearSolverBase,
}

#[pymethods]
impl ModSparseLinearSolver {
    #[new]
    fn new(const_key: HashType) -> ModSparseLinearSolver {
        ModSparseLinearSolver {
            solver: ModSparseLinearSolverBase::new(const_key),
        }
    }

    fn add_objects(&mut self, objects: Vec<HashType>) {
        self.solver.add_objects(objects);
    }

    fn add_relation(&mut self, rel: FxHashMap<HashType, i32>) {
        self.solver.add_relation(rel)
    }

    fn contains_relation(&self, rel: FxHashMap<HashType, i32>) -> bool {
        self.solver.contains_relation(rel)
    }

    fn add_nonzero(&mut self, rel: FxHashMap<HashType, i32>) {
        self.solver.add_nonzero(rel)
    }

    fn contains_nonzero(&self, rel: FxHashMap<HashType, i32>) -> bool {
        self.solver.contains_nonzero(rel)
    }

    fn contains(&self, key: HashType) -> bool {
        self.solver.contains(&key)
    }

    fn clone(&self) -> ModSparseLinearSolver {
        ModSparseLinearSolver {
            solver: self.solver.clone(),
        }
    }

    /// Gathers all relations of the solver for Python.
    fn relations(&self) -> Vec<Vec<(HashType, i32)>> {
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        self.solver
            .data
            .values()
            .map(|v| {
                v.data
                    .iter()
                    .map(|(mon, coef)| (*rev_map.get(mon).unwrap(), *coef))
                    .collect_vec()
            })
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn nonzeroes(&self) -> Vec<Vec<(HashType, i32)>> {
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        self.solver
            .nonzeroes
            .values()
            .map(|v| v.iter())
            .flatten()
            .map(|v| {
                v.data
                    .iter()
                    .map(|(mon, coef)| (*rev_map.get(mon).unwrap(), *coef))
                    .collect_vec()
            })
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn indices(&self) -> FxHashMap<HashType, MonType> {
        self.solver.name_map.clone()
    }

    /// Checks if a value is known.
    fn get_value(&self, rel: FxHashMap<HashType, i32>) -> Option<i32> {
        self.solver.get_value(rel)
    }

    fn find_combinations(
        &self,
        coefficients: Vec<i32>,
        const_coef: i32,
        coef_keys: Vec<Vec<HashType>>,
    ) -> Vec<Vec<HashType>> {
        self.solver
            .find_combinations(coefficients, const_coef, coef_keys)
    }

    /// Reduces the given vector modulo the relations of the linear algebra tracker.
    fn reduce(&self, rel: FxHashMap<HashType, i32>) -> FxHashMap<HashType, i32> {
        let mut v = self.solver.make_row(rel).unwrap();
        self.solver.reduce(&mut v);
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        v.iter()
            .map(|(m, v)| (*rev_map.get(m).unwrap(), *v))
            .collect()
    }
}

#[pyclass]
pub struct BoolSparseLinearSolver {
    solver: BoolSparseLinearSolverBase,
}

#[pymethods]
impl BoolSparseLinearSolver {
    #[new]
    fn new(const_key: HashType) -> BoolSparseLinearSolver {
        BoolSparseLinearSolver {
            solver: BoolSparseLinearSolverBase::new(const_key),
        }
    }

    fn add_objects(&mut self, objects: Vec<HashType>) {
        self.solver.add_objects(objects);
    }

    fn add_relation(&mut self, rel: FxHashMap<HashType, bool>) {
        self.solver.add_relation(rel)
    }

    fn contains_relation(&self, rel: FxHashMap<HashType, bool>) -> bool {
        self.solver.contains_relation(rel)
    }

    fn add_nonzero(&mut self, rel: FxHashMap<HashType, bool>) {
        self.solver.add_nonzero(rel)
    }

    fn contains_nonzero(&self, rel: FxHashMap<HashType, bool>) -> bool {
        self.solver.contains_nonzero(rel)
    }

    fn contains(&self, key: HashType) -> bool {
        self.solver.contains(&key)
    }

    fn clone(&self) -> BoolSparseLinearSolver {
        BoolSparseLinearSolver {
            solver: self.solver.clone(),
        }
    }

    /// Gathers all relations of the solver for Python.
    fn relations(&self) -> Vec<Vec<(HashType, bool)>> {
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        self.solver
            .data
            .values()
            .map(|v| {
                v.data
                    .iter()
                    .map(|(mon, coef)| (*rev_map.get(mon).unwrap(), *coef))
                    .collect_vec()
            })
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn nonzeroes(&self) -> Vec<Vec<(HashType, bool)>> {
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();
        // Note that the nonzeroes are just the complements of all relations.
        self.solver
            .data
            .values()
            .map(|v| v + &SparseVector::new(vec![(self.solver.get_const_idx(), true)]))
            .map(|v| {
                v.data
                    .iter()
                    .map(|(mon, coef)| (*rev_map.get(mon).unwrap(), *coef))
                    .collect_vec()
            })
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn indices(&self) -> FxHashMap<HashType, MonType> {
        self.solver.name_map.clone()
    }

    /// Checks if a value is known.
    fn get_value(&self, rel: FxHashMap<HashType, bool>) -> Option<bool> {
        self.solver.get_value(rel)
    }

    fn find_combinations(
        &self,
        coefficients: Vec<bool>,
        const_coef: bool,
        coef_keys: Vec<Vec<HashType>>,
    ) -> Vec<Vec<HashType>> {
        self.solver
            .find_combinations(coefficients, const_coef, coef_keys)
    }

    /// Reduces the given vector modulo the relations of the linear algebra tracker.
    fn reduce(&self, rel: FxHashMap<HashType, bool>) -> FxHashMap<HashType, bool> {
        let mut v = self.solver.make_row(rel).unwrap();
        self.solver.reduce(&mut v);
        let rev_map: FxHashMap<MonType, HashType> = self
            .solver
            .name_map
            .iter()
            .map(|(key, val)| (*val, *key))
            .collect();

        v.iter()
            .map(|(m, v)| (*rev_map.get(m).unwrap(), *v))
            .collect()
    }
}

#[allow(unused_imports)]
pub mod sparse_linear_tests {
    use itertools::Itertools;
    use rand::{rngs::StdRng, Rng, SeedableRng};
    use rustc_hash::FxHashMap;

    use super::{ModSparseLinearSolverBase, RSparseLinearSolverBase, SparseLinearSolver};
    use crate::linear::{
        dense_linear::{LinearSolver, ModLinearSolver, ModLinearSolverBase},
        sparse_vec::SparseVector,
    };
    use crate::{hashmap, HashType};

    #[test]
    pub fn test_stuff() {
        let mut solv = ModSparseLinearSolverBase::default();
        solv.add_objects(vec![1, 2, 3, 3]);
        assert_eq!(solv.name_map.len(), 3);
        solv.add_objects(vec![1, 4]);
        assert_eq!(solv.name_map.len(), 4);
    }
    #[test]
    pub fn test_echelonization() {
        let mut solv = ModSparseLinearSolverBase::default();
        solv.add_objects(vec![0, 1, 2]);
        solv.add_relation(hashmap!(0 => 1, 1 => 3, 2 => 3));
        solv.add_relation(hashmap!(0 => 5, 1 => 2, 2 => 1));

        let red = SparseVector::new(vec![(0, -14), (1, -3)]);
        assert!(solv.data.get(&1).unwrap() == &red);
    }

    #[test]
    pub fn test_nonzero_mod() {
        let mut solv = ModSparseLinearSolverBase::new(0);
        solv.add_objects(vec![0]);
        solv.add_relation(hashmap!(0 => 180));

        assert!(!solv.contains_nonzero(hashmap!(0 => 0)));
        assert!(!solv.contains_nonzero(hashmap!(0 => 180)));
        assert!(solv.contains_nonzero(hashmap!(0 => 1)));
        assert!(solv.contains_nonzero(hashmap!(0 => 12)));
    }

    /// Makes sure that the relations of the sparse solver are exactly equivalent to the relations of the dense solver
    /// by ensuring that each one contains the span of the other.
    #[test]
    pub fn compare_with_dense() {
        const KEY_COUNT: usize = 10;
        const REL_COUNT: usize = 8;
        let rng = &mut StdRng::seed_from_u64(0x12345678);
        let keys = (0..KEY_COUNT).map(|i| i as HashType).collect_vec();
        for _ in 0..100 {
            let mut s1 = ModLinearSolverBase::new(0);
            let mut s2 = ModSparseLinearSolverBase::new(0);
            s2.add_objects(keys.iter().copied());
            s1.add_objects(keys.clone());

            for _ in 0..REL_COUNT {
                let rel: FxHashMap<HashType, i32> = keys
                    .iter()
                    .copied()
                    .map(|key| (key, rng.gen_range(-1..=1)))
                    .collect();
                s1.add_relation(rel.clone());
                s2.add_relation(rel);
            }
            for rel in &s1.data {
                assert!(s2.contains_relation(
                    rel.iter()
                        .enumerate()
                        .map(|(idx, val)| (idx as HashType, *val))
                        .collect()
                ));
            }
            for rel in s2.data.into_values() {
                assert!(s1.contains_relation(
                    rel.data
                        .into_iter()
                        .map(|(idx, val)| (idx as HashType, val))
                        .collect()
                ));
            }
        }
    }
}

pub fn main() {
    let mut solv = ModSparseLinearSolverBase::new(0);
    solv.add_objects([0i64, 1i64]);
    solv.add_relation(hashmap!(0 => 180));
    // solv.add_relation(hashmap!(0 => 540, 1 => 1));
    let mut v = SparseVector::new(vec![(0, 540), (1, 1)]);
    solv.reduce(&mut v);
    println!("{:?}", v);
}
