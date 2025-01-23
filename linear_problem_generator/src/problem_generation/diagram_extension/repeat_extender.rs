use rand::rngs::ThreadRng;

use crate::{
    embeddings::{embedded_diagram::EmbeddedDiagram, geo_float::GeoFloat, TryEmbed},
    geometry::construction_type::ConstructionType,
};

use super::diagram_extender::DiagramExtender;

/// A [`DiagramExtender`] that repeats the [`DiagramExtender`] it contains until
/// the amount of new constructions surpasses a predefined limit.
/// (This might create slightly more than the amount of constructions required)
#[derive(Default)]
pub struct RepeatExtender<E: DiagramExtender> {
    /// The extender to run repeatedly
    extender: E,
    /// The target amount of new objects to construct
    construction_count: usize,
}

impl<E: DiagramExtender> RepeatExtender<E> {
    pub fn new(extender: E, construction_count: usize) -> Self {
        Self {
            extender,
            construction_count,
        }
    }
}

impl<E: DiagramExtender> DiagramExtender for RepeatExtender<E> {
    fn extend_diagram<F: GeoFloat>(&self, embedded_diagram: &mut EmbeddedDiagram<F>)
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        let target_construction_count =
            embedded_diagram.diagram().constructions.len() + self.construction_count;

        while embedded_diagram.diagram().constructions.len() < target_construction_count {
            self.extender.extend_diagram(embedded_diagram);
        }
    }
}
