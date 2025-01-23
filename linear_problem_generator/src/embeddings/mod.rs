pub(crate) mod constructions_simple;
pub(crate) mod embedded_diagram;
pub(crate) mod embedded_objects;
pub(crate) mod embedding;
pub(crate) mod geo_float;
pub(crate) mod predicates_simple;
pub(crate) mod tau;

pub use embedded_diagram::EmbeddedDiagram;

use embedded_objects::embedded_object::{EmbeddedObject, EmbeddingError};
use embedding::Embedding;
use geo_float::GeoFloat;
use smallvec::SmallVec;

use crate::{consts::MAX_ARGS, geometry::diagram::Diagram};

/// A trait for geometric constructions that can be embedded in `F^2` space.
pub trait TryEmbed<F: GeoFloat, Meta> {
    /// Embeds the object using the given embedding of its arguments.
    ///
    /// Parameters:
    /// * `args`: The embeddings of the arguments of the construction.
    /// * `meta`: Metadata used by the construction, such as an `Rng` object or a custom precision.
    fn try_build(
        &self,
        args: &[EmbeddedObject<F>],
        meta: &mut Meta,
    ) -> Result<EmbeddedObject<F>, EmbeddingError>;
}

/// A trait for geometric predicates that allows them to check whether they are correct
/// in a specific embedding.
pub(crate) trait CheckApply<F: GeoFloat> {
    /// Checks whether the predicate applies,
    /// given the embeddings of the predicate's arguments.
    fn applies(&self, args: &[EmbeddedObject<F>]) -> bool;

    /// Finds all tuples of constructions in a diagram that satisfy the predicate.
    fn find_all(
        &self,
        diagram: &Diagram,
        embedding: &Embedding<F>,
    ) -> Vec<SmallVec<[usize; MAX_ARGS]>>;
}
