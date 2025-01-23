use super::sparse_poly::{MPoly, MPolyType, Monomial};
use itertools::Itertools;
use pyo3::prelude::*;
use rustc_hash::FxHashMap;
use smallvec::{Array, SmallVec};
use std::fmt::{Debug, Display};
use std::hash::Hash;
use std::mem;

type HashType = i64;
type MonType = u16;

/// A macro to build hash-maps.
macro_rules! hash_map {
    {$($k: expr => $v: expr),* $(,)?} => {
        [$(($k.clone(), $v),)*].into_iter().collect()
    };
}

/// A trait of structs that track linear algebra relations and inequalities, implementing the shared behavior.
/// Relations are tracked suing standard linear algebra.
/// Non-zero relations are more difficult. They are stored as a list of non-zero relations, since they are not additive,
/// and to check if some linear combinations is non-zero, it is first reduced using the relations,
/// reduced using one of the non-zeroes, and reduced again using the relations.
/// This is made difficult, and can't be done using a canonical form,
/// because non-zero relations are closed to multiplication by a non-zero.
///
/// Note: Unlike the normal linear solver, this is only implemented for field elements currently.
/// Ring elements add more complexity.
pub trait SparseLinearSolver<
    Key: PartialEq + Eq + Hash + Clone + Ord + Copy + Debug,
    Scalar: Default + Clone + Copy + Debug + PartialEq + MPolyType + Display,
>
{
    /// Gets a mutable reference to the name map.
    fn get_map_mut(&mut self) -> &mut FxHashMap<Key, MonType>;
    /// Gets the name map.
    fn get_map(&self) -> &FxHashMap<Key, MonType>;
    /// Gets a mutable reference to the data and nonzero array.
    fn get_data_and_nonzero_mut(
        &mut self,
    ) -> (
        &mut Vec<Vec<MPoly<MonType, Scalar>>>,
        &mut Vec<MPoly<MonType, Scalar>>,
    );
    /// Gets the relations array.
    ///
    /// Parameters:
    /// * `self`
    ///
    /// Return:
    ///
    /// A vector containing multivariate polynomials. The vector `self.get_data[i]` contains all known relations of degree `i`.
    fn get_data(&self) -> &Vec<Vec<MPoly<MonType, Scalar>>>;
    /// Gets the nonzero array.
    fn get_nonzero(&self) -> &Vec<MPoly<MonType, Scalar>>;
    /// Checks if the given value is zero, or sufficiently close to 0.
    fn is_zero(t: &Scalar) -> bool;
    /// Reduces the first vector with the second vector, using the given monomial.
    fn reduce_with(
        reduced: &mut MPoly<MonType, Scalar>,
        with: &MPoly<MonType, Scalar>,
        mon: &Monomial<MonType>,
    );

    /// Checks if the given relation has a single known value.
    fn get_value(&self, rel: FxHashMap<Monomial<Key>, Scalar>) -> Option<Scalar> {
        let mut row = self.make_row(rel);
        self.reduce(&mut row);
        // The MPoly is a constant.
        if row.data.len() == 1 && row.data[0].0.degree() == 0 {
            Some(row.data[0].1)
        } else {
            None
        }
    }

    /// Gets a mutable reference to the data array.
    fn get_data_mut(&mut self) -> &mut Vec<Vec<MPoly<MonType, Scalar>>> {
        self.get_data_and_nonzero_mut().0
    }

    /// Gets a mutable reference to the nonzero array.
    fn get_nonzero_mut(&mut self) -> &mut Vec<MPoly<MonType, Scalar>> {
        self.get_data_and_nonzero_mut().1
    }

    /// Adds new objects to the linear solver.
    fn add_objects(&mut self, new_objs: impl IntoIterator<Item = Key>) {
        let map = self.get_map_mut();
        new_objs.into_iter().for_each(|obj| {
            if !map.contains_key(&obj) {
                map.insert(obj, map.len() as MonType);
            }
        })
    }

    /// Adds a new nonzero identity to the linear algebra tracker.
    fn add_nonzero(&mut self, rel: FxHashMap<Monomial<Key>, Scalar>) {
        self.add_objects(rel.keys().map(|m| m.vars.iter().cloned()).flatten());
        let mut row = self.make_row(rel);
        self.reduce(&mut row);
        Self::normalize(&mut row);
        self.get_nonzero_mut().push(row);
    }

    /// Adds a new relation to the linear algebra tracker.
    fn add_relation(&mut self, rel: FxHashMap<Monomial<Key>, Scalar>) {
        self.add_objects(rel.keys().map(|m| m.vars.iter().cloned()).flatten());
        let row = self.make_row(rel);
        let data = self.get_data_mut();
        while data.len() <= row.degree() {
            data.push(Vec::new());
        }
        data[row.degree()].push(row);
        self.echelonize();
    }

    /// Returns the number of objects tracked by the linear algebra solver.
    fn object_count(&self) -> usize {
        self.get_map().len()
    }

    /// Reduces a vector given a list of relations.
    ///
    /// Parameters:
    /// * `relations`: The list of relations to use when reducing the vector.
    /// * `v`: The vector to reduce.
    /// * `full_reduction`: Whether to also remove monomials that aren't the top monoials of the vector.
    fn _reduce(
        relations: &Vec<Vec<MPoly<MonType, Scalar>>>,
        v: &mut MPoly<MonType, Scalar>,
        full_reduction: bool,
    ) {
        if v.data.len() == 0 {
            return;
        }
        // The current monomial of `v` to reduce.
        let mut curr_mon = v.data.last().unwrap().0.clone();
        let mut curr_row = 0;
        'reduction: loop {
            // Attempting reduction using a vector of a lower degree.
            for deg in 0..curr_mon.degree() {
                for poly in relations[deg].iter() {
                    // The polynomial can't be zero.
                    if curr_mon.is_divisible_by(&poly.data.last().unwrap().0) {
                        Self::reduce_with(v, poly, &curr_mon);
                        if let Some((next_mon, _)) = v.next_largest_item(curr_mon).map(Clone::clone)
                        {
                            curr_mon = next_mon;
                            continue 'reduction;
                        } else {
                            return;
                        }
                    }
                }
            }
            if v.degree() < relations.len() {
                let same_deg = &relations[v.degree()];
                while curr_row < same_deg.len() && same_deg[curr_row].top_monomial().0 > curr_mon {
                    curr_row += 1;
                }
                if curr_row < same_deg.len() && same_deg[curr_row].top_monomial().0 == curr_mon {
                    Self::reduce_with(v, &same_deg[curr_row], &curr_mon);
                    if let Some((next_mon, _)) = v.next_largest_item(curr_mon).map(Clone::clone) {
                        curr_mon = next_mon;
                        continue 'reduction;
                    } else {
                        return;
                    }
                }
            }
            // We have failed to top-reduce the polynomial.
            if !full_reduction {
                return;
            }
            // We have finished reducing the polynomial.
            let Some((next_mon, _)) = v.next_largest_item(curr_mon).map(Clone::clone) else {
                return;
            };
            curr_mon = next_mon;
        }
    }

    /// Multiplies the vector by a unit to transform it to the canonical form.
    fn normalize(v: &mut MPoly<MonType, Scalar>);

    /// Reduces a vector to the canonical form.
    /// The result of the reduction must be the canonical representative.
    fn reduce(&self, v: &mut MPoly<MonType, Scalar>) {
        Self::_reduce(self.get_data(), v, true);
    }

    /// Reduces the vectors in the solver to an echelonized canonical form.
    fn echelonize(&mut self) {
        let (relations, nonzeros) = self.get_data_and_nonzero_mut();

        let unhandled_relations = &mut vec![vec![]; relations.len()];
        mem::swap(relations, unhandled_relations);

        // Base reduction loop. At the end of this loop, no polynomial is top-reducible by any other polynomial,
        // and the unhandled polynomials are empty.

        loop {
            // Finding the unhandled relation with the smallest degree.
            let Some(mut rel) = unhandled_relations
                .iter_mut()
                .filter_map(|v| v.pop())
                .next()
            else {
                break;
            };

            // Reducing the relation.
            Self::_reduce(relations, &mut rel, false);

            if rel.is_zero() {
                continue;
            }
            let top_mon = rel.top_monomial().0;
            // Reducing old relations with it. If a relation is reduced, then it is pushed to the unhandled queue.
            for by_deg in relations.iter_mut() {
                let mut i = 0;
                while i < by_deg.len() {
                    if by_deg[i].top_monomial().0.is_divisible_by(&top_mon) {
                        let mut reduced = by_deg.swap_remove(i);
                        Self::reduce_with(&mut reduced, &rel, &top_mon);
                        unhandled_relations[reduced.degree()].push(reduced);
                    } else {
                        i += 1;
                    }
                }
            }
            relations[top_mon.degree()].push(rel);
        }

        for by_deg in relations.iter_mut() {
            by_deg.sort_unstable_by(|p1, p2| p2.top_monomial().0.cmp(&p1.top_monomial().0));
        }

        // Reducing the nonzeroes. The nonzeroes are fully reduced, and not only top-reduced.
        for nonz in nonzeros.iter_mut() {
            Self::_reduce(&relations, nonz, true);
            Self::normalize(nonz);
        }
    }

    /// Converts a dictionary to a vector.
    fn make_row(&self, rel: FxHashMap<Monomial<Key>, Scalar>) -> MPoly<MonType, Scalar> {
        let mut data = Vec::new();
        for (key, val) in rel {
            let mon = Monomial {
                vars: key
                    .vars
                    .into_iter()
                    .map(|v| self.get_map().get(&v).unwrap())
                    .cloned()
                    .sorted()
                    .collect(),
            };

            data.push((mon, val));
        }
        MPoly::new(data)
    }

    /// Checks if the linear algebra solver contains the given nonzero relation.
    fn contains_nonzero(&self, rel: FxHashMap<Monomial<Key>, Scalar>) -> bool {
        // Checking if the relation is known to reduce to a nonzero constant.
        if let Some(val) = self.get_value(rel.clone()) {
            if !val.is_zero() {
                return true;
            }
        }

        let mut data = self.make_row(rel);
        // We first reduce the data to a canonical quotient form.
        // Since the sparse linear only works for field elements, we don't have to handle the quotient complexity.
        self.reduce(&mut data);
        // We divide by the appropriate unit to normalize the data.
        Self::normalize(&mut data);
        // Since != 0 is only closed to multiplication by a unit and we have taken the quotient by units,
        // it should be exactly equal to one of the nonzeroes
        self.get_nonzero().iter().any(|nonz| {
            nonz.data
                .iter()
                .zip(data.data.iter())
                .all(|((m1, v1), (m2, v2))| {
                    m1 == m2 && Self::is_zero(&v1.clone().mpoly_sub(v2.clone()))
                })
        })
    }

    /// Checks if the linear algebra solver contains the given relation.
    fn contains_relation(&self, rel: FxHashMap<Monomial<Key>, Scalar>) -> bool {
        let mut data = self.make_row(rel);
        self.reduce(&mut data);
        data.iter().all(|(_, v)| Self::is_zero(v))
    }

    /// Checks if the tracker tracks the given object.
    fn contains(&self, key: &Key) -> bool {
        self.get_map().contains_key(key)
    }
}

trait ToHash {
    fn to_hash(&self) -> HashType;
}

impl ToHash for i64 {
    fn to_hash(&self) -> HashType {
        *self
    }
}

impl ToHash for f64 {
    fn to_hash(&self) -> HashType {
        (self * 1024.).round() as HashType
    }
}

impl ToHash for bool {
    fn to_hash(&self) -> HashType {
        1
    }
}

#[derive(Default, Clone)]
pub struct BoolSparseLinearSolverBase {
    pub name_map: FxHashMap<i64, MonType>,
    pub data: Vec<Vec<MPoly<MonType, bool>>>,
    pub nonzeros: Vec<MPoly<MonType, bool>>,
    pub const_key: i64,
}

impl BoolSparseLinearSolverBase {
    pub fn new(const_key: i64) -> BoolSparseLinearSolverBase {
        BoolSparseLinearSolverBase {
            name_map: FxHashMap::default(),
            data: Vec::new(),
            nonzeros: Vec::new(),
            const_key,
        }
    }
}

impl SparseLinearSolver<i64, bool> for BoolSparseLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<i64, MonType> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<i64, MonType> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(
        &mut self,
    ) -> (
        &mut Vec<Vec<MPoly<MonType, bool>>>,
        &mut Vec<MPoly<MonType, bool>>,
    ) {
        (&mut self.data, &mut self.nonzeros)
    }

    fn get_data(&self) -> &Vec<Vec<MPoly<MonType, bool>>> {
        &self.data
    }

    fn get_nonzero(&self) -> &Vec<MPoly<MonType, bool>> {
        &self.nonzeros
    }

    fn reduce_with(
        reduced: &mut MPoly<MonType, bool>,
        with: &MPoly<MonType, bool>,
        mon: &Monomial<MonType>,
    ) {
        if !reduced[mon] {
            return;
        }
        let (with_mon, _) = with.data.last().unwrap();

        if with_mon != mon {
            assert!(mon.is_divisible_by(with_mon));
            *reduced ^= &(with * (mon / with_mon).unwrap());
        } else {
            *reduced ^= with;
        }
    }
    fn normalize(_v: &mut MPoly<MonType, bool>) {
        // There are no units apart from 1 in F2.
    }

    fn is_zero(t: &bool) -> bool {
        !t
    }

    fn add_nonzero(&mut self, mut rel: FxHashMap<Monomial<i64>, bool>) {
        // Bool linear algebra trackers don't differentiate between relations and nonzeroes.
        *rel.entry(Monomial::constant()).or_insert(false) ^= true;
        self.add_relation(rel);
    }

    fn contains_nonzero(&self, mut rel: FxHashMap<Monomial<i64>, bool>) -> bool {
        // Bool linear algebra trackers don't differentiate between relations and nonzeroes.
        *rel.entry(Monomial::constant()).or_insert(false) ^= true;
        self.contains_relation(rel)
    }
}

#[pyclass]
#[derive(Default, Clone)]
pub struct RSparseLinearSolverBase {
    /// A map from the python indices to indices in the map.
    pub name_map: FxHashMap<i64, MonType>,
    /// A list of all linear combinations known to be equal to 0.
    pub relations: Vec<Vec<MPoly<MonType, f64>>>,
    /// A list of all linear combinations known to to be equal to 0.
    pub nonzeroes: Vec<MPoly<MonType, f64>>,
}

impl RSparseLinearSolverBase {
    fn new() -> RSparseLinearSolverBase {
        RSparseLinearSolverBase {
            name_map: FxHashMap::default(),
            relations: Vec::new(),
            nonzeroes: Vec::new(),
        }
    }
}

impl SparseLinearSolver<i64, f64> for RSparseLinearSolverBase {
    fn get_map_mut(&mut self) -> &mut FxHashMap<i64, MonType> {
        &mut self.name_map
    }

    fn get_map(&self) -> &FxHashMap<i64, MonType> {
        &self.name_map
    }

    fn get_data_and_nonzero_mut(
        &mut self,
    ) -> (
        &mut Vec<Vec<MPoly<MonType, f64>>>,
        &mut Vec<MPoly<MonType, f64>>,
    ) {
        (&mut self.relations, &mut self.nonzeroes)
    }

    fn get_data(&self) -> &Vec<Vec<MPoly<MonType, f64>>> {
        &self.relations
    }

    fn get_nonzero(&self) -> &Vec<MPoly<MonType, f64>> {
        &self.nonzeroes
    }

    fn reduce_with(
        reduced: &mut MPoly<MonType, f64>,
        with: &MPoly<MonType, f64>,
        mon: &Monomial<MonType>,
    ) {
        if Self::is_zero(&reduced[mon]) {
            return;
        }

        let red_val = reduced[mon];
        let (with_mon, with_val) = with.data.last().unwrap();
        let factor = -red_val / with_val;
        assert!(factor.is_finite());

        if with_mon != mon {
            assert!(mon.is_divisible_by(with_mon));
            *reduced += with * &((mon / with_mon).unwrap(), factor);
        } else {
            *reduced += with * factor;
        }
    }

    fn normalize(v: &mut MPoly<MonType, f64>) {
        if v.is_zero() {
            return;
        }
        let (_, val) = v.top_monomial();
        *v /= val;
    }

    fn is_zero(t: &f64) -> bool {
        t.abs() < 1e-9
    }
}

fn map_relation<const D: usize, K, T>(
    rel: FxHashMap<SmallVec<[K; D]>, T>,
) -> FxHashMap<Monomial<<[K; D] as Array>::Item>, T>
where
    [K; D]: smallvec::Array,
    <[K; D] as Array>::Item: Ord + Clone + Copy + Debug + Hash,
{
    rel.into_iter()
        .map(|(k, v)| (Monomial::new(k.into_iter()), v))
        .collect()
}

fn poly_to_map<T: Clone + MPolyType>(poly: &MPoly<MonType, T>) -> FxHashMap<Vec<MonType>, T> {
    poly.data
        .iter()
        .map(|(mon, v)| (Vec::from_iter(mon.vars.iter().cloned()), v.clone()))
        .collect()
}

#[pyclass]
pub struct RSparseLinearSolver {
    solver: RSparseLinearSolverBase,
}

#[pymethods]
impl RSparseLinearSolver {
    #[new]
    pub fn new() -> RSparseLinearSolver {
        RSparseLinearSolver {
            solver: RSparseLinearSolverBase::new(),
        }
    }

    fn add_objects(&mut self, objects: Vec<i64>) {
        self.solver.add_objects(objects);
    }

    fn add_relation(&mut self, rel: FxHashMap<SmallVec<[i64; 2]>, f64>) {
        self.solver.add_relation(map_relation(rel))
    }

    fn contains_relation(&self, rel: FxHashMap<SmallVec<[i64; 2]>, f64>) -> bool {
        self.solver.contains_relation(map_relation(rel))
    }

    fn add_nonzero(&mut self, rel: FxHashMap<SmallVec<[i64; 2]>, f64>) {
        self.solver.add_nonzero(map_relation(rel))
    }

    fn contains_nonzero(&self, rel: FxHashMap<SmallVec<[i64; 2]>, f64>) -> bool {
        self.solver.contains_nonzero(map_relation(rel))
    }

    fn contains(&self, key: i64) -> bool {
        self.solver.contains(&key)
    }

    fn clone(&self) -> RSparseLinearSolver {
        RSparseLinearSolver {
            solver: self.solver.clone(),
        }
    }

    /// Gathers all relations of the solver for Python.
    fn relations(&self) -> Vec<FxHashMap<Vec<u16>, f64>> {
        self.solver
            .relations
            .iter()
            .map(|by_deg| by_deg.iter())
            .flatten()
            .map(|p| poly_to_map(p))
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn nonzeroes(&self) -> Vec<FxHashMap<Vec<u16>, f64>> {
        self.solver
            .nonzeroes
            .iter()
            .map(|p| poly_to_map(p))
            .collect_vec()
    }

    /// Gathers all relations of the solver for Python.
    fn indices(&self) -> FxHashMap<i64, u16> {
        self.solver.name_map.clone()
    }

    /// Checks if a value is known.
    fn get_value(&self, rel: FxHashMap<SmallVec<[i64; 2]>, f64>) -> Option<f64> {
        self.solver.get_value(map_relation(rel))
    }

    /// Prints all the relations.
    fn print(&self) {
        println!("R-SparseLinearAlgebraTracker");
        println!("Relations:");
        self.solver
            .relations
            .iter()
            .for_each(|by_deg| by_deg.iter().for_each(|p| println!("\t{}", p)));
        println!("Nonzeros:");
        self.solver
            .nonzeroes
            .iter()
            .for_each(|p| println!("\t{}", p));
    }
}

// #[pyclass]
// pub struct BoolLinearSolver {
//     solver: BoolLinearSolverBase,
// }

// #[pymethods]
// impl BoolLinearSolver {
//     #[new]
//     fn new(const_key: i64) -> BoolLinearSolver {
//         BoolLinearSolver {
//             solver: BoolLinearSolverBase::new(const_key),
//         }
//     }

//     fn add_objects(&mut self, objects: Vec<i64>) {
//         self.solver.add_objects(objects);
//     }

//     fn reduce(&self, v: Vec<bool>) -> Vec<bool> {
//         let mut v = MPoly:usize, :new(v);
//         self.solver.reduce(&mut v);
//         v.data
//     }

//     fn reduce_rel(&self, rel: FxHashMap<i64, bool>) -> Vec<bool> {
//         let mut data = vec![false; self.solver.len()];
//         for (key, val) in rel {
//             data[*self.solver.get_map().get(&key).unwrap()] ^= val;
//         }
//         self.reduce(data)
//     }

//     fn add_relation(&mut self, rel: FxHashMap<i64, bool>) {
//         self.solver.add_relation(rel)
//     }

//     fn contains_relation(&self, rel: FxHashMap<i64, bool>) -> bool {
//         self.solver.contains_relation(rel)
//     }

//     fn add_nonzero(&mut self, rel: FxHashMap<i64, bool>) {
//         self.solver.add_nonzero(rel)
//     }

//     fn contains_nonzero(&self, rel: FxHashMap<i64, bool>) -> bool {
//         self.solver.contains_nonzero(rel)
//     }

//     fn contains(&self, key: i64) -> bool {
//         self.solver.contains(&key)
//     }

//     fn clone(&self) -> BoolLinearSolver {
//         BoolLinearSolver {
//             solver: self.solver.clone(),
//         }
//     }

//     /// Gethers all relations of the solver for Python.
//     fn relations(&self) -> Vec<Vec<bool>> {
//         self.solver
//             .data
//             .iter()
//             .map(|v| v.data.clone())
//             .collect_vec()
//     }

//     /// Gethers all relations of the solver for Python.
//     fn nonzeroes(&self) -> Vec<Vec<bool>> {
//         // Note that the nonzeroes are just the complements of all relations.
//         let idx = *self.solver.name_map.get(&self.solver.const_key).unwrap();
//         self.solver
//             .data
//             .iter()
//             .map(|v| {
//                 let mut res = v.data.clone();
//                 res[idx] ^= true;
//                 res
//             })
//             .collect_vec()
//     }

//     /// Gethers all relations of the solver for Python.
//     fn indices(&self) -> FxHashMap<i64, usize> {
//         self.solver.name_map.clone()
//     }

//     /// Checks if a value is known.
//     fn get_value(&self, rel: FxHashMap<i64, bool>) -> Option<bool> {
//         self.solver.get_value(rel)
//     }
// }

#[allow(unused_imports)]
mod linear_tests {
    use rustc_hash::FxHashMap;

    use crate::linear::sparse_poly::Monomial;

    use super::{RSparseLinearSolverBase, SparseLinearSolver};

    /// Tests a simple linear algebra reduction.
    #[test]
    pub fn test_simple() {
        let mut solv = RSparseLinearSolverBase::default();
        solv.add_objects([0, 1, 2]);

        let x = Monomial::new([0]);
        let y = Monomial::new([1]);
        let z = Monomial::new([2]);

        solv.add_relation(hash_map!(x.clone() => 1., y.clone() => 3., z.clone() => 2.));
        solv.add_relation(hash_map!(x.clone() => 5., y.clone() => 2., z.clone() => 1.));

        let x = Monomial::new([0u16]);
        let y = Monomial::new([1u16]);
        let z = Monomial::new([2u16]);

        assert_eq!(solv.relations[1][0][&x], 5.);
        assert_eq!(solv.relations[1][0][&y], 2.);
        assert_eq!(solv.relations[1][0][&z], 1.);

        assert_eq!(solv.relations[1][1][&x], -9.);
        assert_eq!(solv.relations[1][1][&y], -1.);
        assert_eq!(solv.relations[1][1][&z], 0.);
    }

    /// Testing a linear algebra reduction that involves multiplication by a monomial.
    #[test]
    pub fn test_mul_by_mon() {
        let mut solv = RSparseLinearSolverBase::default();
        solv.add_objects([0]);

        let x = Monomial::new([0]);

        solv.add_relation(hash_map!(x.clone() => 2.));
        solv.add_relation(hash_map!(&x * &x => 4.));

        let relation_count = solv
            .relations
            .iter()
            .map(|by_deg| by_deg.len())
            .sum::<usize>();
        assert_eq!(relation_count, 1);
    }
}

pub fn main() {
    let mut solv = RSparseLinearSolverBase::default();
    solv.add_objects([0]);

    let x = Monomial::new([0]);

    solv.add_relation(hash_map!(x.clone() => 2.));
    solv.add_relation(hash_map!(&x * &x => 4.));

    solv.relations
        .iter()
        .for_each(|d| d.iter().for_each(|rel| println!("{rel}")));

    let relation_count = solv
        .relations
        .iter()
        .map(|by_deg| by_deg.len())
        .sum::<usize>();
    println!("{}", relation_count);
}
