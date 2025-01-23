use rand::{thread_rng, RngCore};
use smallvec::SmallVec;

use crate::{
    embeddings::{embedded_diagram::EmbeddedDiagram, geo_float::GeoFloat, TryEmbed},
    geometry::{construction::Construction, construction_type::ConstructionType},
    groups::group_action::GroupAction,
};

use super::diagram_extender::DiagramExtender;

/// A [`DiagramExtender`] that takes the resulting constructions from another extender,
/// and builds all their symmetrical constructions.
pub struct SymmetricalExtender<E: DiagramExtender> {
    /// The extender whose constructions' symmetries we will be building.
    extender: E,
    /// The indices in the diagram that [`Self::action`] is acting on.
    domain: Vec<usize>,
    /// A group defining the symmetries to apply on [`Self::domain`].
    action: Box<dyn GroupAction>,
}

impl<E: DiagramExtender> SymmetricalExtender<E> {
    pub fn new(extender: E, domain: Vec<usize>, action: Box<dyn GroupAction>) -> Self {
        Self {
            extender,
            domain,
            action,
        }
    }
}

impl<E: DiagramExtender> DiagramExtender for SymmetricalExtender<E> {
    fn extend_diagram<F: GeoFloat>(&self, embedded_diagram: &mut EmbeddedDiagram<F>)
    where
        ConstructionType: TryEmbed<F, Box<dyn RngCore>>,
    {
        let mut rng: Box<dyn RngCore> = Box::new(thread_rng());

        let old_diagram_size = embedded_diagram.diagram().constructions.len();
        self.extender.extend_diagram(embedded_diagram);
        let new_diagram_size = embedded_diagram.diagram().constructions.len();

        (old_diagram_size..new_diagram_size).for_each(|construction_index| {
            (0..self.action.group_size()).for_each(|symmetry_index| {
                self.try_push_symmetry(embedded_diagram, construction_index, symmetry_index, &mut rng);
            })
        });
    }
}

impl<E: DiagramExtender> SymmetricalExtender<E> {
    /// Attempts to add a construction symmetric to some other construction in the diagram.
    /// (We might be add other new construction in the process if we need them to define the new element)
    ///
    /// Note: The reason we require an Embedding, is so that we are able to detect
    /// elements that are not symmetric in the textual sense, but that are symmetries in the geometrical sense.
    /// For example: If in the triangle ABC, we have h_a, h_b, and h_c be the altitudes,
    /// then H = line_intersection(h_a, h_b) is the orthocenter, and should be used as symmetric
    /// to any permutation of {A, B, C}. Thus the Circumcircle of HAB is symmetric of the Circumcircle of HAC.
    /// We need the embedding to tell this, because `line_intersection(h_a, h_b) == line_intersection(h_a, h_c)`.
    ///
    /// embedded_diagram:       An embedding of the diagram in which we are building the symmetry.
    /// construction_index:     The index of the construction whose symmetry we are building.
    /// symmetry_index:         The index of the element in the [`Self::group_action`] group we are using as a symmetry.
    pub(crate) fn try_push_symmetry<F: GeoFloat>(
        &self,
        embedded_diagram: &mut EmbeddedDiagram<F>,
        construction_index: usize,
        symmetry_index: usize,
        rng: &mut Box<dyn RngCore>,
    ) -> Option<usize>
    where
        ConstructionType: TryEmbed<F, Box<dyn RngCore>>,
    {
        if let Some(i) = self.domain.iter().position(|&i| i == construction_index) {
            return Some(self.domain[self.action.apply(symmetry_index, i)]);
        }

        let Construction { _type, arguments } =
            embedded_diagram.diagram().constructions[construction_index].clone();

        let Some(symmetrical_arguments) = arguments
            .into_iter()
            .map(|argument| self.try_push_symmetry(embedded_diagram, argument, symmetry_index, rng))
            .collect::<Option<SmallVec<_>>>()
        else {
            return None;
        };

        let symmetrical_construction = Construction {
            _type,
            arguments: symmetrical_arguments,
        };

        if let Some(index) = embedded_diagram.try_find(&symmetrical_construction, rng) {
            Some(index)
        } else if embedded_diagram.try_push(symmetrical_construction, rng) {
            Some(embedded_diagram.diagram().constructions.len() - 1)
        } else {
            None
        }
    }
}
