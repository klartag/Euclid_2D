use rustc_hash::FxHashMap;

pub mod match_blob;
pub mod matching_hash;
pub mod matching_vec;
pub mod signature_dag;

pub trait Matching: Clone + 'static + Send + Sync {
    fn new(keys: Vec<i64>, data: Vec<Vec<i64>>) -> Self;

    fn one() -> Self;

    fn of(src: i64, tar: i64) -> Self;

    fn zero() -> Self;

    /// Checks if the matching object doesn't currenly hold any mapping.
    fn is_one(&self) -> bool;
    /// Checks if the matching object doesn't currenly hold any mapping.
    fn is_zero(&self) -> bool;

    /// Checks if the matching object holds some mapping.
    fn is_nonzero(&self) -> bool;

    /// Returns the keys of the matching.
    fn keys(&self) -> Vec<i64>;
    /// Returns the keys of the matching.
    fn matchings(&self) -> Vec<Vec<i64>>;

    /// Adds the data in the other matching to self.
    fn extend(&mut self, other: &Self);

    /// Returns all the matches in `self` that do not appear in `other`.
    fn subtract(&mut self, other: &mut Self) -> Self;

    /// Finds the product of two Match objects.
    fn product(&mut self, other: &mut Self) -> Self;

    fn len(&self) -> usize;

    /// Maps the keys of the matching to another set of keys.
    ///
    /// Parameters:
    /// * `mapping`: A dictionary giving a key for each key of the current Matching object.
    ///
    /// Return:
    ///
    /// A new Matching object, where each key is replaced by mapping[key].
    fn map_keys(&self, mapping: &FxHashMap<i64, i64>) -> Self;
}
