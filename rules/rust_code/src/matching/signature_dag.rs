use std::{
    fmt::Debug,
    hash::{Hash, Hasher},
    sync::{Arc, RwLock},
};

use super::{matching_vec::MatchingVec, Matching};
use crate::{
    linear::{sparse_linear::SparseLinearSolver, sparse_vec::SparseVecType},
    HashType, MonType,
};
use itertools::Itertools;
use pyo3::prelude::*;
use rustc_hash::{FxHashMap, FxHashSet, FxHasher};

pub(crate) trait Pattern<Match: Matching> {
    fn id(&self) -> HashType;
    /// Gets the matches of the pattern.
    fn matches(&self) -> (&Match, &Match, &Match);
    /// Gets the matches of the pattern.
    fn matches_mut(&mut self) -> (&mut Match, &mut Match, &mut Match);
    /// Gets the old matches of the pattern.
    fn old_matches(&self) -> &Match {
        self.matches().0
    }
    /// Gets the old matches of the pattern.
    fn old_matches_mut(&mut self) -> &mut Match {
        self.matches_mut().0
    }
    /// Gets the old matches of the pattern.
    fn new_matches(&self) -> &Match {
        self.matches().1
    }
    /// Gets the new matches of the pattern.
    fn new_matches_mut(&mut self) -> &mut Match {
        self.matches_mut().1
    }
    /// Gets the old matches of the pattern.
    fn all_matches(&self) -> &Match {
        self.matches().2
    }
    /// Gets all the matches of the pattern.
    fn all_matches_mut(&mut self) -> &mut Match {
        self.matches_mut().2
    }

    /// Marks all the new matches of the pattern as old.
    fn mark_pushed(&mut self) {
        *self.old_matches_mut() = self.all_matches().clone();
        *self.new_matches_mut() = Match::zero();
    }
    /// The number of matches found by the pattern.
    fn len(&self) -> usize {
        self.old_matches().len()
    }
    /// Updates the pattern to take new matches of its sub-patterns into account.
    fn update(&mut self);
    /// The number of pure objects matched by the pattern.
    fn keys(&self) -> &FxHashSet<HashType>;

    /// A string representation of the pattern.
    fn to_string(&self) -> String;
}

pub(crate) type PatternRef<Match> = Arc<RwLock<dyn Pattern<Match> + Send + Sync>>;

pub(crate) struct BasePattern<Match: Matching> {
    pub pred: RustPredicate,
    degrees_of_freedom: FxHashSet<HashType>,
    old_matches: Match,
    new_matches: Match,
    all_matches: Match,
}

pub(crate) type BasePatternRef<Match> = Arc<RwLock<BasePattern<Match>>>;

impl<Match: Matching> BasePattern<Match> {
    pub fn new(pred: RustPredicate) -> BasePattern<Match> {
        BasePattern {
            degrees_of_freedom: pred.arg_ids.iter().copied().collect(),
            old_matches: Match::zero(),
            new_matches: Match::zero(),
            all_matches: Match::zero(),
            pred,
        }
    }
}

impl<Match: Matching> BasePattern<Match> {
    pub fn add_predicate(&mut self, pred: RustPredicate) {
        let mtch = Match::new(self.pred.arg_ids.clone(), vec![pred.arg_ids.clone()]);
        self.new_matches.extend(&mtch);
        self.all_matches.extend(&mtch);
    }
}

impl<Match: Matching> Pattern<Match> for BasePattern<Match> {
    fn matches(&self) -> (&Match, &Match, &Match) {
        (&self.old_matches, &self.new_matches, &self.all_matches)
    }

    fn matches_mut(&mut self) -> (&mut Match, &mut Match, &mut Match) {
        (
            &mut self.old_matches,
            &mut self.new_matches,
            &mut self.all_matches,
        )
    }

    fn update(&mut self) {}

    fn keys(&self) -> &FxHashSet<HashType> {
        &self.degrees_of_freedom
    }

    fn id(&self) -> HashType {
        self.pred.id
    }

    fn to_string(&self) -> String {
        format!(
            "BasePattern(pred=({}, {:?}), old={} new={})",
            self.pred.id,
            self.pred.arg_ids,
            self.old_matches.len(),
            self.new_matches.len()
        )
    }
}

struct IntersectPattern<Match: Matching> {
    components: Vec<PatternRef<Match>>,
    accumulators: Vec<Match>,

    old_matches: Match,
    new_matches: Match,
    all_matches: Match,

    last_update: usize,
    degrees_of_freedom: FxHashSet<HashType>,

    id: i64,
}

impl<Match: Matching> IntersectPattern<Match> {
    pub fn new(components: Vec<PatternRef<Match>>) -> IntersectPattern<Match> {
        IntersectPattern {
            accumulators: vec![Match::zero(); components.len()],
            old_matches: Match::zero(),
            new_matches: Match::zero(),
            all_matches: Match::zero(),
            last_update: 0,
            degrees_of_freedom: components
                .iter()
                .map(|comp| comp.try_read().unwrap().keys().clone())
                .flatten()
                .collect(),
            id: components
                .iter()
                .map(|c| c.try_read().unwrap().id())
                .sum::<HashType>(),
            components,
        }
    }
}

impl<Match: Matching> Hash for IntersectPattern<Match> {
    fn hash<H: std::hash::Hasher>(&self, state: &mut H) {
        self.id.hash(state);
    }
}

impl<Match: Matching> IntersectPattern<Match> {
    fn score(found_dof: &FxHashSet<HashType>, pattern: PatternRef<Match>) -> HashType {
        let pattern = pattern.try_read().unwrap();
        let all_keys = pattern.keys().len() as f64;
        let rem_keys = pattern
            .keys()
            .iter()
            .filter(|k| !found_dof.contains(*k))
            .count() as f64;
        ((pattern.len() as f64).powf(rem_keys / all_keys.max(1.)) * 1000.) as HashType
    }

    /// Reorders the patterns of the intersection pattern to minimize the expected intermediate match count.
    fn reorder(&mut self) {
        assert!(!self.components.is_empty());

        let mut new_comps = Vec::new();
        let mut old_comps = self.components.clone();
        let mut found_dof = FxHashSet::default();

        while !old_comps.is_empty() {
            let best_idx = (0..old_comps.len())
                .min_by_key(|i| Self::score(&found_dof, old_comps[*i].clone()))
                .unwrap();
            let best_pattern = old_comps.swap_remove(best_idx);
            found_dof.extend(best_pattern.try_read().unwrap().keys());
            new_comps.push(best_pattern);
        }
        self.components = new_comps;

        self.accumulators[0] = self.components[0].try_read().unwrap().old_matches().clone();

        for (idx, pat) in self.components.iter().enumerate().skip(1) {
            self.accumulators[idx] =
                self.accumulators[idx - 1].product(pat.try_write().unwrap().old_matches_mut());
        }
        self.last_update = self
            .accumulators
            .iter()
            .map(|acc| acc.len())
            .max()
            .unwrap_or_default();
    }
}

impl<Match: Matching> Pattern<Match> for IntersectPattern<Match> {
    fn matches(&self) -> (&Match, &Match, &Match) {
        (&self.old_matches, &self.new_matches, &self.all_matches)
    }
    fn matches_mut(&mut self) -> (&mut Match, &mut Match, &mut Match) {
        (
            &mut self.old_matches,
            &mut self.new_matches,
            &mut self.all_matches,
        )
    }

    fn update(&mut self) {
        assert!(!self.components.is_empty());

        if self
            .accumulators
            .iter()
            .any(|acc| acc.len() > 2 * self.last_update)
        {
            self.reorder();
        }

        // println!("IntersectPattern update!");

        let mut new_acc = self.components[0].try_read().unwrap().new_matches().clone();
        // println!("Initial: {}", new_acc.len());
        for (prev_acc, comp) in self
            .accumulators
            .iter_mut()
            .zip(self.components.iter().skip(1))
        {
            let mut lock = comp.try_write().unwrap();
            let (_, new_mut, all_mut) = lock.matches_mut();
            new_acc = new_acc.product(all_mut);
            new_acc.extend(&prev_acc.product(new_mut));
        }

        self.new_matches.extend(&new_acc);
        self.all_matches.extend(&new_acc);
    }

    fn keys(&self) -> &FxHashSet<HashType> {
        &self.degrees_of_freedom
    }

    fn id(&self) -> HashType {
        self.id
    }

    fn to_string(&self) -> String {
        format!(
            "IntersectPattern({:?}, old={}, new={})",
            self.components
                .iter()
                .map(|comp| comp.try_read().unwrap().id())
                .collect_vec(),
            self.old_matches.len(),
            self.new_matches.len()
        )
    }
}

struct RekeyPattern<Match: Matching> {
    pattern: PatternRef<Match>,
    key_map: FxHashMap<HashType, HashType>,

    old_matches: Match,
    new_matches: Match,
    all_matches: Match,

    keys: FxHashSet<HashType>,
    id: HashType,
}

impl<Match: Matching> RekeyPattern<Match> {
    pub fn get_id(
        base_pattern: PatternRef<Match>,
        key_map: &FxHashMap<HashType, HashType>,
    ) -> HashType {
        let mut hasher = FxHasher::default();
        base_pattern.try_read().unwrap().id().hash(&mut hasher);
        (key_map
            .iter()
            .map(|(key, val)| {
                let mut hasher = FxHasher::default();
                key.hash(&mut hasher);
                val.hash(&mut hasher);
                hasher.finish()
            })
            .sum::<u64>() as i64)
            .hash(&mut hasher);

        hasher.finish() as HashType
    }

    pub fn new(
        base_pattern: PatternRef<Match>,
        key_map: FxHashMap<HashType, HashType>,
    ) -> RekeyPattern<Match> {
        let copy = base_pattern.clone();
        let base = base_pattern.try_read().unwrap();

        assert!(
            base.keys().iter().all(|key| key_map.contains_key(key)),
            "RekeyPattern was initialized without the required keys!"
        );
        assert_eq!(key_map.len(), base.keys().len());
        let keys = base
            .keys()
            .iter()
            .map(|k| *key_map.get(k).unwrap())
            .collect();
        let old_matches = base.old_matches().map_keys(&key_map);
        let new_matches = base.new_matches().map_keys(&key_map);
        let all_matches = base.all_matches().map_keys(&key_map);

        let id = RekeyPattern::get_id(base_pattern.clone(), &key_map);

        RekeyPattern {
            pattern: copy,
            key_map,
            old_matches,
            new_matches,
            all_matches,
            keys,
            id,
        }
    }
}

impl<Match: Matching> Pattern<Match> for RekeyPattern<Match> {
    fn id(&self) -> HashType {
        self.id
    }

    fn matches(&self) -> (&Match, &Match, &Match) {
        (&self.old_matches, &self.new_matches, &self.all_matches)
    }

    fn matches_mut(&mut self) -> (&mut Match, &mut Match, &mut Match) {
        (
            &mut self.old_matches,
            &mut self.new_matches,
            &mut self.all_matches,
        )
    }

    fn update(&mut self) {
        let base = self.pattern.try_read().unwrap();
        self.old_matches = base.old_matches().map_keys(&self.key_map);
        self.new_matches = base.new_matches().map_keys(&self.key_map);
        self.all_matches = base.all_matches().map_keys(&self.key_map);
    }

    fn keys(&self) -> &FxHashSet<HashType> {
        &self.keys
    }

    fn to_string(&self) -> String {
        format!(
            "RekeyPattern(id={}, base={}, map={:?} old={}, new={})",
            self.id,
            self.pattern.try_read().unwrap().id(),
            self.key_map,
            self.old_matches.len(),
            self.new_matches.len(),
        )
    }
}

/// Finds the index of the object in an array.
fn index<T: Eq>(obj: &T, arr: &[T]) -> Option<usize> {
    for (idx, t) in arr.iter().enumerate() {
        if obj == t {
            return Some(idx);
        }
    }
    None
}

/// A pattern tracking equations.
pub(crate) struct EqPattern<
    Scalar: Default + Clone + Debug + PartialEq + SparseVecType,
    Match: Matching,
> {
    id: HashType,

    /// The components of the EqPattern are a list of components
    /// such that the results of the EqPattern should be in the intersection of the patterns.
    ids: Vec<HashType>,
    components: Vec<PatternRef<Match>>,
    coefficients: Vec<Scalar>,
    const_coef: Scalar,

    left_intersection: IntersectPattern<Match>,
    left_ids: Vec<HashType>,
    left_coefficients: Vec<Scalar>,

    right_ids: Vec<HashType>,
    right_intersection: IntersectPattern<Match>,
    right_coefficients: Vec<Scalar>,

    unsorted_ids: FxHashSet<HashType>,
    old_matches: Match,
    new_matches: Match,
    all_matches: Match,

    last_reorder: usize,
}

impl<Scalar: Default + Clone + Debug + PartialEq + SparseVecType, Match: Matching>
    EqPattern<Scalar, Match>
{
    /// Picks a new subset of patterns to be the left and right patterns,
    /// in an attempt to minimize the number of combinations checked by the linear algebra solver.
    pub fn reorder(&mut self) {
        if self.left_intersection.len() + self.right_intersection.len() <= 2 * self.last_reorder {
            return;
        }

        self.last_reorder = self.left_intersection.len() + self.right_intersection.len()
    }

    pub fn update_checker(&mut self, checker: &impl SparseLinearSolver<HashType, MonType, Scalar>) {
        self.reorder();

        self.left_intersection.update();
        self.right_intersection.update();

        let left_indices = self
            .left_ids
            .iter()
            .map(|id| index(id, &self.left_intersection.all_matches.keys()).unwrap())
            .collect_vec();

        let right_indices = self
            .left_ids
            .iter()
            .map(|id| index(id, &self.left_intersection.all_matches.keys()).unwrap())
            .collect_vec();

        let left_combinations = self
            .left_intersection
            .all_matches
            .matchings()
            .into_iter()
            .map(|v| left_indices.iter().map(|i| v[*i]).collect_vec())
            .collect_vec();

        let right_combinations = self
            .right_intersection
            .all_matches
            .matchings()
            .into_iter()
            .map(|v| right_indices.iter().map(|i| v[*i]).collect_vec())
            .collect_vec();

        let all_objects = left_combinations
            .iter()
            .flatten()
            .chain(right_combinations.iter().flatten())
            .copied()
            .unique()
            .collect_vec();
    }
}

impl<Scalar: Default + Clone + Debug + PartialEq + SparseVecType, Match: Matching> Pattern<Match>
    for EqPattern<Scalar, Match>
{
    fn id(&self) -> HashType {
        self.id
    }

    fn matches(&self) -> (&Match, &Match, &Match) {
        (&self.old_matches, &self.new_matches, &self.all_matches)
    }

    fn matches_mut(&mut self) -> (&mut Match, &mut Match, &mut Match) {
        (
            &mut self.old_matches,
            &mut self.new_matches,
            &mut self.all_matches,
        )
    }

    /// An EqPattern is not updated using the generic updating system.
    fn update(&mut self) {}

    fn to_string(&self) -> String {
        format!(
            "EqPattern({}, coefs={:?}, old={}, new={})",
            self.id,
            self.coefficients,
            self.old_matches.len(),
            self.new_matches.len()
        )
    }

    fn keys(&self) -> &FxHashSet<HashType> {
        &self.unsorted_ids
    }
}

/// A struct allowing to find collections of objects satisfying certain conditions.
pub struct SignatureDag<Match: Matching, Out: Clone> {
    sorted_patterns: Vec<PatternRef<Match>>,
    base_patterns: FxHashMap<HashType, BasePatternRef<Match>>,
    patterns_by_id: FxHashMap<HashType, PatternRef<Match>>,
    out_patterns: Vec<(Out, PatternRef<Match>)>,
}

impl<Match: Matching, Out: Clone> Default for SignatureDag<Match, Out> {
    fn default() -> Self {
        Self {
            sorted_patterns: Default::default(),
            base_patterns: Default::default(),
            patterns_by_id: Default::default(),
            out_patterns: Default::default(),
        }
    }
}

impl<Match: Matching, Out: Clone> SignatureDag<Match, Out> {
    /// Adds the predicate to the SignatureMatcher.
    pub(crate) fn add_predicate(&mut self, pred: RustPredicate) {
        let Some(base_pattern) = self.base_patterns.get(&pred.id) else {
            // If we don't have an appropriate base pattern, we skip.
            return;
        };
        base_pattern.try_write().unwrap().add_predicate(pred);
    }

    /// Makes the pattern of the given predicate.
    pub(crate) fn get_pred_pattern(&mut self, pred: RustPredicate) -> PatternRef<Match> {
        let id = pred.id;
        if let Some(base) = self.base_patterns.get(&id) {
            // The pattern already exists. We either use it directly or rekey it.
            let inner = base.try_read().unwrap();
            if inner.pred == pred {
                return base.clone();
            } else {
                let map: FxHashMap<HashType, HashType> = inner
                    .pred
                    .arg_ids
                    .iter()
                    .copied()
                    .zip(pred.arg_ids.iter().copied())
                    .collect();
                let res_pattern = Arc::new(RwLock::new(RekeyPattern::new(base.clone(), map)));
                let id = res_pattern.try_read().unwrap().id;
                if let Some(old) = self.patterns_by_id.get(&id) {
                    return old.clone();
                }
                self.sorted_patterns.push(res_pattern.clone());
                self.patterns_by_id.insert(id, res_pattern.clone());
                return res_pattern;
            }
        }

        let new_pattern = Arc::new(RwLock::new(BasePattern::new(pred)));
        self.sorted_patterns.push(new_pattern.clone());
        self.base_patterns.insert(id, new_pattern.clone());
        new_pattern
    }

    /// Makes the pattern of the given predicate.
    pub(crate) fn get_intersect_pattern(
        &mut self,
        sub_patterns: Vec<PatternRef<Match>>,
    ) -> PatternRef<Match> {
        let h = sub_patterns
            .iter()
            .map(|p| p.try_read().unwrap().id())
            .sum::<HashType>();

        if self.patterns_by_id.contains_key(&h) {
            return self.patterns_by_id.get(&h).unwrap().clone();
        }

        let new_pattern = Arc::new(RwLock::new(IntersectPattern::new(sub_patterns)));
        self.sorted_patterns.push(new_pattern.clone());
        self.patterns_by_id.insert(h, new_pattern.clone());
        new_pattern
    }

    /// Links a given pattern with an output marker.
    pub(crate) fn add_out_pattern(&mut self, pattern: PatternRef<Match>, out: Out) {
        self.out_patterns.push((out, pattern));
    }

    pub fn update(&mut self) -> Vec<(Out, Vec<i64>)> {
        for pattern in &self.sorted_patterns {
            pattern.try_write().unwrap().update();
        }

        let res = self
            .out_patterns
            .iter()
            .map(|(out, pattern)| {
                let new_matches = pattern.try_read().unwrap().new_matches().matchings();
                new_matches.into_iter().map(|v| (out.clone(), v))
            })
            .flatten()
            .collect_vec();

        for pattern in &self.sorted_patterns {
            pattern.try_write().unwrap().mark_pushed();
        }

        res
    }
}

#[pyclass]
#[derive(Clone, Eq, PartialEq)]
pub struct RustPredicate {
    pub id: HashType,
    pub arg_ids: Vec<HashType>,
}

/// A way to hold patterns in Python.
#[pyclass]
pub struct RustPattern {
    internal: PatternRef<MatchingVec>,
}

impl RustPattern {
    pub(crate) fn new(pattern: PatternRef<MatchingVec>) -> RustPattern {
        RustPattern { internal: pattern }
    }
}
#[pymethods]
impl RustPattern {
    pub fn to_string(&self) -> String {
        self.internal.try_read().unwrap().to_string()
    }
}

/// A python handle for the SignatureDag.
/// Match=MatchingVec
/// Uses Out=i64
///
/// At least until I implement the probably better `MatchingBlob` properly.
#[pyclass]
pub struct RustSignatureDag {
    internal: SignatureDag<MatchingVec, HashType>,
}

#[pymethods]
impl RustPredicate {
    #[new]
    pub fn new(id: HashType, arg_ids: Vec<HashType>) -> RustPredicate {
        RustPredicate { id, arg_ids }
    }

    pub fn pred_id(&self) -> HashType {
        self.id
    }

    pub fn arg_ids(&self) -> Vec<HashType> {
        self.arg_ids.clone()
    }
}

#[pymethods]
impl RustSignatureDag {
    #[new]
    pub fn new() -> RustSignatureDag {
        RustSignatureDag {
            internal: SignatureDag::default(),
        }
    }

    pub fn get_predicate_pattern(&mut self, pred: RustPredicate) -> RustPattern {
        RustPattern::new(self.internal.get_pred_pattern(pred))
    }

    pub fn get_intersection_pattern(&mut self, patterns: Vec<&PyCell<RustPattern>>) -> RustPattern {
        let patterns: Vec<PatternRef<MatchingVec>> = patterns
            .iter()
            .map(|cell| PyCell::<RustPattern>::borrow(cell).internal.clone())
            .collect_vec();

        RustPattern::new(self.internal.get_intersect_pattern(patterns))
    }

    pub fn add_out_pattern(&mut self, pattern: &RustPattern, out: i64) {
        self.internal.add_out_pattern(pattern.internal.clone(), out);
    }

    pub fn add_predicate(&mut self, pred: RustPredicate) {
        self.internal.add_predicate(pred);
    }

    pub fn update(&mut self) -> Vec<(HashType, Vec<HashType>)> {
        self.internal.update()
    }

    /// Returns the number of patterns tracked by the signature DAG.
    pub fn pattern_count(&self) -> usize {
        self.internal.sorted_patterns.len()
    }

    pub fn sorted_patterns(&self) -> Vec<RustPattern> {
        self.internal
            .sorted_patterns
            .iter()
            .cloned()
            .map(|pattern| RustPattern::new(pattern))
            .collect_vec()
    }
}
