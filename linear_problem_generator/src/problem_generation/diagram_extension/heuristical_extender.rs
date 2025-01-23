use rand::rngs::ThreadRng;

use crate::{
    embeddings::{embedded_diagram::EmbeddedDiagram, geo_float::GeoFloat, TryEmbed},
    geometry::{construction::Construction, construction_type::ConstructionType, diagram::Diagram},
};

use super::diagram_extender::DiagramExtender;

/// A [`DiagramExtender`] that runs some other extender, and then uses
/// predefined heuristics to draw constructions based on the ones the other extender added.
#[derive(Default)]
pub struct HeuristicalExtender<E: DiagramExtender> {
    /// The extender whose constructions we will use when running our heuristics.
    extender: E,
}

impl<E: DiagramExtender> HeuristicalExtender<E> {
    pub fn new(extender: E) -> Self {
        Self { extender }
    }
}

impl<E: DiagramExtender> DiagramExtender for HeuristicalExtender<E> {
    fn extend_diagram<F: GeoFloat>(&self, embedded_diagram: &mut EmbeddedDiagram<F>)
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        let old_diagram_size = embedded_diagram.diagram().constructions.len();
        self.extender.extend_diagram(embedded_diagram);
        let new_diagram_size = embedded_diagram.diagram().constructions.len();

        (old_diagram_size..new_diagram_size).for_each(|construction_index| {
            self.construction_heuristics(&embedded_diagram.diagram(), construction_index)
                .into_iter()
                .for_each(|heuristical_construction| {
                    embedded_diagram.try_push(heuristical_construction);
                });
        });
    }
}

impl<E: DiagramExtender> HeuristicalExtender<E> {
    /// Gets new constructions that should automatically be created whenever a construction is built.
    ///
    /// For example, whenever we project a point onto a line, we want to automatically also draw the altitude.
    pub(crate) fn construction_heuristics(
        &self,
        diagram: &Diagram,
        construction_index: usize,
    ) -> Vec<Construction> {
        let construction = &diagram.constructions[construction_index];

        match construction._type {
            ConstructionType::Projection => {
                vec![diagram.construct(
                    ConstructionType::Line,
                    &[construction.arguments[0], construction_index],
                )]
            }

            ConstructionType::Midpoint => {
                vec![diagram.construct(
                    ConstructionType::Line,
                    &[construction.arguments[0], construction.arguments[1]],
                )]
            }

            ConstructionType::NewPoint
            | ConstructionType::NewLine
            | ConstructionType::NewCircle
            | ConstructionType::PointOnLine
            | ConstructionType::PointOnCircle
            | ConstructionType::Line
            | ConstructionType::Center
            | ConstructionType::LineIntersection
            | ConstructionType::Circumcircle
            | ConstructionType::LineOnPoint
            | ConstructionType::LineCircleIntersection
            | ConstructionType::CircleIntersection
            | ConstructionType::LineCircleOtherIntersection
            | ConstructionType::CircleCircleOtherIntersection
            | ConstructionType::CircleFromCenterAndRadius
            | ConstructionType::CircleFromCenter
            | ConstructionType::InternalBisector
            | ConstructionType::ExternalBisector
            | ConstructionType::Parallel
            | ConstructionType::Tangent
            | ConstructionType::OtherTangent
            | ConstructionType::CollinearPoint => vec![],
        }
    }
}
