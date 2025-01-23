use std::{
    ops::Index,
    slice::{Iter, SliceIndex},
};

use rand::rngs::ThreadRng;

use crate::geometry::{construction::Construction, construction_type::ConstructionType};

use super::{CheckApply, Diagram, EmbeddedObject, GeoFloat, TryEmbed};

/// A list of geometry objects pertaining to some [`Diagram`], and embedded in F^2 space.
pub struct Embedding<F: GeoFloat> {
    objects: Vec<EmbeddedObject<F>>,
}

impl<F: GeoFloat> Embedding<F> {
    pub(crate) fn new() -> Self {
        Self {
            objects: Default::default(),
        }
    }

    pub(crate) fn len(&self) -> usize {
        self.objects.len()
    }

    pub(crate) fn push(&mut self, object: EmbeddedObject<F>) {
        self.objects.push(object)
    }

    /// Checks whether a construction can already be found in an embedding.
    /// Returns the index in which it was found.
    pub(crate) fn find(&self, diagram: &Diagram, construction: &Construction) -> Option<usize>
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        let object = diagram.try_embed_construction(construction, self).ok()?;

        let equals_predicate_type = object.geo_type().equals_predicate();

        self.objects.iter().position(|embedded_object| {
            embedded_object.geo_type() == object.geo_type()
                && equals_predicate_type.applies(&[*embedded_object, object])
        })
    }

    /// Checks whether a construction can be found in a specified index of an embedding.
    /// Returns whether it was found there.
    pub(crate) fn is_found_here(
        &self,
        diagram: &Diagram,
        construction: &Construction,
        index: usize,
    ) -> bool
    where
        ConstructionType: TryEmbed<F, ThreadRng>,
    {
        let Ok(object) = diagram.try_embed_construction(construction, self) else {
            return false;
        };

        let equals_predicate_type = object.geo_type().equals_predicate();

        self.objects.get(index).is_some_and(|embedded_object| {
            embedded_object.geo_type() == object.geo_type()
                && equals_predicate_type.applies(&[*embedded_object, object])
        })
    }

    pub(crate) fn iter(&self) -> Iter<'_, EmbeddedObject<F>> {
        (&self).into_iter()
    }
}

impl<Idx, F: GeoFloat> Index<Idx> for Embedding<F>
where
    Idx: SliceIndex<[EmbeddedObject<F>]>,
{
    type Output = Idx::Output;

    fn index(&self, index: Idx) -> &Self::Output {
        &self.objects[index]
    }
}

impl<F: GeoFloat> IntoIterator for Embedding<F> {
    type Item = EmbeddedObject<F>;

    type IntoIter = <Vec<EmbeddedObject<F>> as IntoIterator>::IntoIter;

    fn into_iter(self) -> Self::IntoIter {
        self.objects.into_iter()
    }
}

impl<'a, F: GeoFloat> IntoIterator for &'a Embedding<F> {
    type Item = &'a EmbeddedObject<F>;

    type IntoIter = <&'a [EmbeddedObject<F>] as IntoIterator>::IntoIter;

    fn into_iter(self) -> Self::IntoIter {
        self.objects.iter()
    }
}
