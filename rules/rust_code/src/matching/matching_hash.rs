use itertools::Itertools;
use pyo3::prelude::*;
use rustc_hash::{FxHashMap, FxHashSet};

use super::matching_vec::merge;

/// A struct representing all possible mappings of some Python objects to other Python objects.
/// The keys are sorted in ascending order, and the data is sorted arbitrarily.
#[pyclass]
#[derive(Debug, Clone)]
pub struct MatchingHash {
    /// The objects to which we match other objects.
    keys: Vec<i64>,
    /// All possible matchings of values to the given keys.
    data: FxHashSet<Vec<i64>>,
}

impl MatchingHash {
    pub fn rnew(keys: Vec<i64>, data: FxHashSet<Vec<i64>>) -> MatchingHash {
        let indices = (0..keys.len())
            .sorted_unstable_by_key(|&i| keys[i])
            .collect_vec();

        MatchingHash {
            keys: indices.iter().map(|&i| keys[i]).collect_vec(),
            data: data
                .into_iter()
                .map(|v| indices.iter().map(|&i| v[i]).collect_vec())
                .collect(),
        }
    }
}

#[pymethods]
impl MatchingHash {
    #[new]
    pub fn new(keys: Vec<i64>, data: Vec<Vec<i64>>) -> MatchingHash {
        let indices = (0..keys.len())
            .sorted_unstable_by_key(|&i| keys[i])
            .collect_vec();

        MatchingHash {
            keys: indices.iter().map(|&i| keys[i]).collect_vec(),
            data: data
                .into_iter()
                .map(|v| indices.iter().map(|&i| v[i]).collect_vec())
                .collect(),
        }
    }

    #[staticmethod]
    pub fn one() -> MatchingHash {
        let mut data = FxHashSet::default();
        data.insert(Vec::new());
        MatchingHash {
            keys: Vec::new(),
            data,
        }
    }

    #[staticmethod]
    pub fn of(src: i64, tar: i64) -> MatchingHash {
        let mut data = FxHashSet::default();
        data.insert(vec![tar]);

        MatchingHash {
            keys: vec![src],
            data,
        }
    }

    #[staticmethod]
    pub fn zero() -> MatchingHash {
        MatchingHash {
            keys: Vec::new(),
            data: FxHashSet::default(),
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
        self.data.iter().cloned().collect_vec()
    }

    /// Returns a copy of the matching.
    pub fn clone(&self) -> MatchingHash {
        MatchingHash {
            keys: self.keys.clone(),
            data: self.data.clone(),
        }
    }

    /// Adds the data in the other matching to self.
    pub fn extend(&mut self, other: &MatchingHash) {
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
    }

    /// Returns all the matches in `self` that do not appear in `other`.
    pub fn subtract(&self, other: &MatchingHash) -> MatchingHash {
        if other.is_zero() || self.is_zero() {
            return self.clone();
        }
        assert_eq!(
            self.keys(),
            other.keys(),
            "Attempted to substract matchings with different keys!"
        );

        MatchingHash {
            keys: self.keys.clone(),
            data: self
                .data
                .iter()
                .filter(|v| !other.data.contains(*v))
                .cloned()
                .collect(),
        }
    }

    /// Finds the product of two Match objects.
    pub fn product(&mut self, other: &mut MatchingHash) -> MatchingHash {
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

        let mut self_data = self.data.iter().cloned().collect_vec();
        let mut other_data = other.data.iter().cloned().collect_vec();

        merge(
            &mut self_data,
            &mut other_data,
            &mut res,
            &shared_keys,
            &res_indices,
        );
        MatchingHash::new(res_keys, res)
    }

    pub fn len(&self) -> usize {
        self.data.len()
    }

    #[staticmethod]
    pub fn concat(matchings: Vec<&PyCell<MatchingHash>>) -> MatchingHash {
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
            return MatchingHash::zero();
        };
        // Making sure that all matchings can be concatenated.
        for m in matchings.iter().filter(|m| m.is_nonzero()) {
            assert_eq!(&m.keys, &legal_keys);
        }

        // If any matching is the empty matching, we just return the empty matching,
        // since all inputs are guaranted to be empty.
        if matchings.iter().any(|m| m.is_one()) {
            return MatchingHash::one();
        }

        let mut res_data = FxHashSet::default();
        res_data.reserve(matchings.iter().map(|m| m.len()).sum());
        matchings
            .iter()
            .filter(|m| m.is_nonzero())
            .for_each(|m| res_data.extend(m.data.iter().cloned()));

        MatchingHash {
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
    fn map_keys(&self, mapping: FxHashMap<i64, i64>) -> MatchingHash {
        let new_keys = self
            .keys
            .iter()
            .map(|k| *mapping.get(k).unwrap())
            .collect_vec();
        MatchingHash::rnew(new_keys, self.data.clone())
    }
}
