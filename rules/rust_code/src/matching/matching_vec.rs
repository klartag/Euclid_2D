use itertools::Itertools;
use pyo3::prelude::*;
use rustc_hash::FxHashMap;

use super::Matching;

/// A struct representing all possible mappings of some Python objects to other Python objects.
/// The keys are sorted in ascending order, and the data is sorted arbitrarily.
#[pyclass]
#[derive(Debug, Clone)]
pub struct MatchingVec {
    /// The objects to which we match other objects.
    keys: Vec<i64>,
    /// All possible matchings of values to the given keys.
    data: Vec<Vec<i64>>,
}

/// Merges two data arrays that agree on all shared indices.
/// The data arrays are sorted arbitrarily to merge efficiently.
/// Parameters:
/// * `left_values`: One data array.
/// * `right_values`: The other data array.
/// * `res`: The data array into which to push everything.
/// * `shared_keys`: A slice containing pairs of columns that must agree in the result.
/// * `right_indices`: A slice specifying which columns from the right map should be added to the result.
pub fn merge(
    left_values: &mut [Vec<i64>],
    right_values: &mut [Vec<i64>],
    res: &mut Vec<Vec<i64>>,
    shared_keys: &[(usize, usize)],
    res_indices: &[(usize, bool)],
) {
    if left_values.len() == 0 || right_values.len() == 0 {
        return;
    }

    // Both sides match on all keys.
    // We merge them.
    if shared_keys.len() == 0 {
        let res_len = res_indices.len();
        for v1 in left_values.iter() {
            for v2 in right_values.iter() {
                let mut new_row = Vec::new();
                new_row.reserve_exact(res_len);
                for (idx, is_left) in res_indices.iter().cloned() {
                    new_row.push(if is_left { v1[idx] } else { v2[idx] });
                }
                res.push(new_row);
            }
        }
        return;
    }
    let (left_idx, right_idx) = shared_keys[0];
    left_values.sort_unstable_by_key(|v| v[left_idx]);
    right_values.sort_unstable_by_key(|v| v[right_idx]);

    let mut right_v = 0;
    let mut left_v = 0;

    while left_v != left_values.len() && right_v != right_values.len() {
        // If the right key is smaller than the left key, advance the right key.
        if right_values[right_v][right_idx] < left_values[left_v][left_idx] {
            while right_v < right_values.len()
                && right_values[right_v][right_idx] < left_values[left_v][left_idx]
            {
                right_v += 1;
            }
            continue;
        }
        // If the left key is smaller than the right key, advance the left key.
        if right_values[right_v][right_idx] > left_values[left_v][left_idx] {
            while left_v < left_values.len()
                && right_values[right_v][right_idx] > left_values[left_v][left_idx]
            {
                left_v += 1;
            }
            continue;
        }
        // If they are equal, recurse on the product and advance both.
        let mut next_left_v = left_v + 1;
        let mut next_right_v = right_v + 1;
        while next_left_v < left_values.len()
            && left_values[next_left_v][left_idx] == left_values[left_v][left_idx]
        {
            next_left_v += 1;
        }
        while next_right_v < right_values.len()
            && right_values[next_right_v][right_idx] == right_values[right_v][right_idx]
        {
            next_right_v += 1;
        }
        merge(
            &mut left_values[left_v..next_left_v],
            &mut right_values[right_v..next_right_v],
            res,
            &shared_keys[1..],
            res_indices,
        );
        left_v = next_left_v;
        right_v = next_right_v;
    }
}

/// Removes duplicates from the given 2D array.
fn dedup_data(data: &mut Vec<Vec<i64>>) {
    data.sort();
    for i in (1..data.len()).rev() {
        if data[i - 1] == data[i] {
            data.swap_remove(i);
        }
    }
}

#[pymethods]
impl MatchingVec {
    #[new]
    pub fn new(keys: Vec<i64>, data: Vec<Vec<i64>>) -> MatchingVec {
        let indices = (0..keys.len())
            .sorted_unstable_by_key(|&i| keys[i])
            .collect_vec();

        let keys = indices.iter().map(|&idx| keys[idx]).collect_vec();
        let mut data = data
            .iter()
            .map(|v| indices.iter().map(|&i| v[i]).collect_vec())
            .collect_vec();
        dedup_data(&mut data);
        MatchingVec { keys, data }
    }

    #[staticmethod]
    pub fn one() -> MatchingVec {
        MatchingVec {
            keys: Vec::new(),
            data: vec![Vec::new()],
        }
    }

    #[staticmethod]
    pub fn of(src: i64, tar: i64) -> MatchingVec {
        MatchingVec {
            keys: vec![src],
            data: vec![vec![tar]],
        }
    }

    #[staticmethod]
    pub fn zero() -> MatchingVec {
        MatchingVec {
            keys: Vec::new(),
            data: Vec::new(),
        }
    }

    /// Checks if the matching object doesn't currenly hold any mapping.
    pub fn is_one(&self) -> bool {
        self.keys.len() == 0 && self.data.len() > 0
    }
    /// Checks if the matching object doesn't currenly hold any mapping.
    pub fn is_zero(&self) -> bool {
        self.data.is_empty()
    }

    /// Checks if the matching object holds some mapping.
    pub fn is_nonzero(&self) -> bool {
        !self.data.is_empty()
    }

    /// Returns the keys of the matching.
    pub fn keys(&self) -> Vec<i64> {
        self.keys.clone()
    }
    /// Returns the keys of the matching.
    pub fn matchings(&self) -> Vec<Vec<i64>> {
        self.data.clone()
    }

    /// Returns a copy of the matching.
    pub fn clone(&self) -> MatchingVec {
        MatchingVec {
            keys: self.keys.clone(),
            data: self.data.clone(),
        }
    }

    /// Adds the data in the other matching to self.
    pub fn extend(&mut self, other: &MatchingVec) {
        if other.is_zero() {
            return;
        }
        if self.is_zero() {
            self.keys = other.keys.clone();
            self.data = other.data.clone();
            return;
        }
        debug_assert_eq!(
            self.keys, other.keys,
            "Attempted to extend Matchings with different keys!"
        );
        self.data.extend(other.data.iter().cloned());
        dedup_data(&mut self.data);
    }

    /// Returns all the matches in `self` that do not appear in `other`.
    pub fn subtract(&mut self, other: &mut MatchingVec) -> MatchingVec {
        if other.is_zero() || self.is_zero() {
            return self.clone();
        }
        assert_eq!(
            self.keys(),
            other.keys(),
            "Attempted to substract matchings with different keys!"
        );
        self.data.sort();
        other.data.sort();

        let mut other_idx = 0;
        let mut res = Vec::new();

        for row in &self.data {
            while other_idx < other.data.len() && row > &other.data[other_idx] {
                other_idx += 1;
            }
            if other_idx == other.data.len() || row != &other.data[other_idx] {
                res.push(row.clone());
            }
        }

        MatchingVec::new(self.keys.clone(), res)
    }

    /// Finds the product of two Match objects.
    pub fn product(&mut self, other: &mut MatchingVec) -> MatchingVec {
        if self.is_one() || other.is_zero() {
            return other.clone();
        }
        if self.is_zero() || other.is_one() {
            return self.clone();
        }

        // A vector containing pairs of indices where the keys are equal.
        let mut shared_keys = Vec::new();
        // A vector containing pairs of indices and whether they come from the left matching (self) or the right matching (other).
        let mut res_indices = Vec::new();
        // The keys of the merged matching.
        let mut res_keys = Vec::new();

        let mut vl = 0;
        let mut vr = 0;
        while vl < self.keys.len() || vr < other.keys.len() {
            if (vl == self.keys.len()) || (vr < other.keys.len() && other.keys[vr] < self.keys[vl])
            {
                // Pushing the right index.
                res_keys.push(other.keys[vr]);
                res_indices.push((vr, false));
                vr += 1;
                continue;
            }
            if (vr == other.keys.len()) || (vl < self.keys.len() && self.keys[vl] < other.keys[vr])
            {
                // Pushing the left index.
                res_keys.push(self.keys[vl]);
                res_indices.push((vl, true));
                vl += 1;
                continue;
            }
            // The two indices exist and are equal.
            res_keys.push(self.keys[vl]);
            res_indices.push((vl, true));
            shared_keys.push((vl, vr));
            vl += 1;
            vr += 1;
        }
        let mut res = Vec::new();
        merge(
            &mut self.data,
            &mut other.data,
            &mut res,
            &shared_keys,
            &res_indices,
        );
        MatchingVec::new(res_keys, res)
    }

    pub fn len(&self) -> usize {
        self.data.len()
    }

    #[staticmethod]
    pub fn concat(matchings: Vec<&PyCell<MatchingVec>>) -> MatchingVec {
        let matchings = matchings.iter().map(|cell| cell.borrow()).collect_vec();
        // If there are no matchings given or the matching is illegal, we return the illegal matching.
        let Some(legal_keys) = matchings
            .iter()
            .filter_map(|m| {
                if m.is_nonzero() {
                    Some(m.keys.clone())
                } else {
                    None
                }
            })
            .next()
        else {
            return MatchingVec::zero();
        };
        // Making sure that all matchings can be concatenated.
        for m in matchings.iter().filter(|m| m.is_nonzero()) {
            assert_eq!(&m.keys, &legal_keys);
        }

        // If any matching is the empty matching, we just return the empty matching,
        // since all inputs are guaranted to be empty.
        if matchings.iter().any(|m| m.is_one()) {
            return MatchingVec::one();
        }

        let mut res_data = Vec::new();
        res_data.reserve_exact(matchings.iter().map(|m| m.len()).sum());
        matchings
            .iter()
            .filter(|m| m.is_nonzero())
            .for_each(|m| res_data.extend(m.data.iter().cloned()));

        dedup_data(&mut res_data);

        MatchingVec {
            keys: legal_keys,
            data: res_data,
        }
    }

    /// Maps the keys of the matching to another set of keys.
    ///
    /// Parameters:
    /// * `mapping`: A dictionary giving a key for each key of the current Matching object.
    ///
    /// Return:
    ///
    /// A new Matching object, where each key is replaced by mapping[key].
    fn map_keys(&self, mapping: FxHashMap<i64, i64>) -> MatchingVec {
        Matching::map_keys(&self, &mapping)
    }
}

impl Matching for MatchingVec {
    fn new(keys: Vec<i64>, data: Vec<Vec<i64>>) -> Self {
        Self::new(keys, data)
    }

    fn one() -> Self {
        Self::one()
    }

    fn of(src: i64, tar: i64) -> Self {
        Self::of(src, tar)
    }

    fn zero() -> Self {
        Self::zero()
    }

    fn is_one(&self) -> bool {
        Self::is_one(self)
    }

    fn is_zero(&self) -> bool {
        Self::is_zero(self)
    }

    fn is_nonzero(&self) -> bool {
        Self::is_nonzero(self)
    }

    fn keys(&self) -> Vec<i64> {
        Self::keys(self)
    }

    fn matchings(&self) -> Vec<Vec<i64>> {
        Self::matchings(self)
    }

    fn extend(&mut self, other: &Self) {
        Self::extend(self, other)
    }

    fn subtract(&mut self, other: &mut Self) -> Self {
        Self::subtract(self, other)
    }

    fn product(&mut self, other: &mut Self) -> Self {
        Self::product(self, other)
    }

    fn len(&self) -> usize {
        Self::len(self)
    }

    fn map_keys(&self, mapping: &FxHashMap<i64, i64>) -> Self {
        let new_keys = self
            .keys
            .iter()
            .map(|k| *mapping.get(k).unwrap())
            .collect_vec();
        MatchingVec::new(new_keys, self.data.clone())
    }
}

#[cfg(test)]
mod tests {
    use itertools::Itertools;
    use rand::{rngs::StdRng, seq::IteratorRandom, SeedableRng};

    use crate::matching::matching_hash::MatchingHash;

    use super::MatchingVec;
    const KEY_COUNT: usize = 4;
    #[test]
    fn test_product() {
        let rng = &mut StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let keys_1 = (0..10).choose_multiple(rng, KEY_COUNT);
            let keys_2 = (0..10).choose_multiple(rng, KEY_COUNT);

            let data_1 = (0..100)
                .map(|_| (0..30).choose_multiple(rng, KEY_COUNT))
                .collect_vec();
            let data_2 = (0..100)
                .map(|_| (0..30).choose_multiple(rng, KEY_COUNT))
                .collect_vec();

            let mut mv1 = MatchingVec::new(keys_1.clone(), data_1.clone());
            let mut mv2 = MatchingVec::new(keys_2.clone(), data_2.clone());
            let mut mh1 = MatchingHash::new(keys_1, data_1);
            let mut mh2 = MatchingHash::new(keys_2, data_2);

            let pv = mv1.product(&mut mv2);
            let ph = mh1.product(&mut mh2);

            let pv2 = MatchingVec::new(ph.keys(), ph.matchings());
            assert_eq!(pv.keys(), pv2.keys());
            assert_eq!(pv.matchings(), pv2.matchings());
        }
    }
    #[test]
    fn test_subtact() {
        let rng = &mut StdRng::seed_from_u64(0x12345678);
        for _ in 0..100 {
            let keys = (0..KEY_COUNT as i64).collect_vec();

            let data_1 = (0..1000)
                .map(|_| (0..30).choose_multiple(rng, KEY_COUNT))
                .collect_vec();
            let data_2 = (0..1000)
                .map(|_| (0..30).choose_multiple(rng, KEY_COUNT))
                .collect_vec();

            let mut mv1 = MatchingVec::new(keys.clone(), data_1.clone());
            let mut mv2 = MatchingVec::new(keys.clone(), data_2.clone());
            let mh1 = MatchingHash::new(keys.clone(), data_1);
            let mh2 = MatchingHash::new(keys, data_2);

            let pv = mv1.subtract(&mut mv2);
            let ph = mh1.subtract(&mh2);

            let pv2 = MatchingVec::new(ph.keys(), ph.matchings());

            assert_eq!(pv.keys(), pv2.keys());
            assert_eq!(pv.matchings(), pv2.matchings());
        }
    }
}
