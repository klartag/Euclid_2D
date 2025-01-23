use itertools::Itertools;
use rand::rngs::ThreadRng;

use crate::{
    geometry::{construction::Construction, construction_type::ConstructionType, diagram::Diagram},
    problem_generation::{
        problem_finding::problem_finder::MAX_EMBED_ATTEMPTS, REQUIRED_EMBEDDING_COUNT,
    },
};

use super::{embedding::Embedding, geo_float::GeoFloat, TryEmbed};

/// The number of embeddings we are allowed to fail in `try_push` before failing.
const ALLOWED_EMBEDDING_FAILURES: usize = 16;

/// A diagram together with a bunch of embeddings.
/// (We hold more than one embedding in case we fail when attempting to add a construction to one of them)
pub struct EmbeddedDiagram<F: GeoFloat>
where
    ConstructionType: TryEmbed<F, ThreadRng>,
{
    diagram: Diagram,
    embeddings: Vec<Embedding<F>>,
}

impl<F: GeoFloat> EmbeddedDiagram<F>
where
    ConstructionType: TryEmbed<F, ThreadRng>,
{
    pub fn new(diagram: Diagram) -> Self {
        let mut embedded_diagram = Self {
            diagram,
            embeddings: Default::default(),
        };
        embedded_diagram.extend_embeddings();
        embedded_diagram
    }

    pub fn diagram(&self) -> &Diagram {
        &self.diagram
    }

    pub fn embeddings(&self) -> &[Embedding<F>] {
        &self.embeddings
    }

    pub(crate) fn try_find(&self, construction: &Construction) -> Option<usize> {
        if let Some(index) = self
            .diagram
            .constructions
            .iter()
            .position(|existing_construction| construction.is_identical(existing_construction))
        {
            return Some(index);
        }

        let index = self
            .embeddings
            .iter()
            .next()
            .map(|embedding| embedding.find(&self.diagram, construction))
            .flatten()?;

        self.embeddings
            .iter()
            .skip(1)
            .all(|embedding| embedding.is_found_here(&self.diagram, construction, index))
            .then_some(index)
    }

    /// Attempts to add a new [`Construction`] to the [`EmbeddedDiagram`].
    /// Returns whether it succeeded.
    pub(crate) fn try_push(&mut self, construction: Construction) -> bool {
        if !self.is_distinct_from_all_embeddings(&construction) {
            return false;
        }

        let embeddings_of_new_construction = self
            .embeddings
            .iter()
            .map(|embedding| {
                self.diagram
                    .try_embed_construction(&construction, &embedding)
            })
            .collect_vec();

        if embeddings_of_new_construction
            .iter()
            .filter(|result| result.is_err())
            .count()
            > ALLOWED_EMBEDDING_FAILURES
        {
            return false;
        }

        self.embeddings.retain_mut(|embedding| {
            let embedded_object = self
                .diagram
                .try_embed_construction(&construction, &embedding);
            if let Ok(embedded_object) = embedded_object {
                embedding.push(embedded_object);
            }
            embedded_object.is_ok()
        });
        self.diagram.push(construction);
        self.extend_embeddings();

        return true;
    }

    /// Checks whether there is no other construction in the diagram
    /// with identical embeddings to a given construction.
    pub(crate) fn is_distinct_from_all_embeddings(&self, construction: &Construction) -> bool {
        self.embeddings
            .iter()
            .all(|embedding| embedding.find(&self.diagram, construction).is_none())
    }

    /// Pushes new embeddings to the `embeddings` list until it is of length [`REQUIRED_EMBEDDING_COUNT`].
    fn extend_embeddings(&mut self) {
        if let Some(required_additional_embeddings) =
            REQUIRED_EMBEDDING_COUNT.checked_sub(self.embeddings.len())
        {
            self.embeddings.extend(
                (0..)
                    .map(|_| self.diagram.embed::<F>(MAX_EMBED_ATTEMPTS))
                    .filter_map(|result| result.ok())
                    .take(required_additional_embeddings),
            );
        }
    }
}
