use rand::RngCore;

use crate::{
    embeddings::{embedded_diagram, geo_float::GeoFloat, TryEmbed},
    geometry::construction_type::ConstructionType,
};

use self::embedded_diagram::EmbeddedDiagram;

/// Represents structures that have strategies for taking a [`Diagram`] and adding new [`Construction`]s to it.
pub trait DiagramExtender {
    /// Adds new objects to a given [`EmbeddedDiagram`] according to this [`DiagramExtender`]'s strategy.
    fn extend_diagram<F: GeoFloat>(&self, embedded_diagram: &mut EmbeddedDiagram<F>) -> bool
    where
        ConstructionType: TryEmbed<F, Box<dyn RngCore>>;
}
