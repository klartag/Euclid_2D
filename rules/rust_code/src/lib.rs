use elsa::FrozenMap;
use pyo3::prelude::*;
pub mod geo;
pub mod linear;
pub mod matching;

/// A macro to build hash-maps.
#[macro_export]
macro_rules! hashmap {
    {$($k: expr => $v: expr),* $(,)?} => {
        [$(($k.clone(), $v),)*].into_iter().collect()
    };
}
pub(crate) type HashType = i64;
pub(crate) type MonType = u16;
pub(crate) type FxFrozenMap<K, V> = FrozenMap<K, V, rustc_hash::FxHasher>;

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn linear_b(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<linear::dense_linear::RLinearSolver>()?;
    m.add_class::<linear::dense_linear::ModLinearSolver>()?;
    m.add_class::<linear::dense_linear::BoolLinearSolver>()?;

    m.add_class::<linear::sparse_linear::RSparseLinearSolver>()?;
    m.add_class::<linear::sparse_linear::ModSparseLinearSolver>()?;
    m.add_class::<linear::sparse_linear::BoolSparseLinearSolver>()?;

    m.add_class::<matching::matching_vec::MatchingVec>()?;
    m.add_class::<matching::matching_hash::MatchingHash>()?;

    m.add_class::<matching::signature_dag::RustPattern>()?;
    m.add_class::<matching::signature_dag::RustSignatureDag>()?;
    m.add_class::<matching::signature_dag::RustPredicate>()?;

    Ok(())
}

pub fn main() {}
