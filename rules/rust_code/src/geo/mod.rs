use elsa::FrozenVec;
use rustc_hash::FxHashMap;
use smallvec::SmallVec;
type HashType = u64;

const MAX_ARGS: usize = 4;

/// The data of a predicate.
/// Specifies how the predicate is unpacked.
#[derive(Hash, Debug, PartialEq, Eq)]
pub struct PredicateData<'t> {
    pub name: String,
    pub args: SmallVec<[&'t GeoObject<'t>; MAX_ARGS]>,
    pub id: usize,
    pub conclusions: Vec<Predicate<'t>>,
}

/// A specific predicate.
#[derive(Hash, Debug, PartialEq, Eq)]
pub struct Predicate<'t> {
    pred: &'t PredicateData<'t>,
    args: SmallVec<[&'t GeoObject<'t>; MAX_ARGS]>,
}

/// A GeoObject.
#[derive(Hash, Debug, PartialEq, Eq)]
pub struct GeoObject<'t> {
    construction_id: &'t ConstructionData<'t>,
    args: SmallVec<[&'t GeoObject<'t>; MAX_ARGS]>,
    id: HashType,
}

#[derive(Hash, PartialEq, Eq, Debug)]
pub struct ConstructionData<'t> {
    name: String,
    args: SmallVec<[&'t GeoObject<'t>; MAX_ARGS]>,
    conclusions: Vec<Predicate<'t>>,
}

pub struct GeoDataStore<'t> {
    geo_objects_storage: FrozenVec<GeoObject<'t>>,
    pred_data_storage: FrozenVec<PredicateData<'t>>,
    construction_data_storage: FrozenVec<ConstructionData<'t>>,

    geo_objects: FxHashMap<HashType, &'t GeoObject<'t>>,
    predicates: FxHashMap<String, &'t PredicateData<'t>>,
    constructions: FxHashMap<String, &'t ConstructionData<'t>>,
}

impl<'t> GeoDataStore<'t> {
    pub fn predicate_data(&'t self, name: String) -> Option<&'t PredicateData<'t>> {
        self.predicates.get(&name).map(|o| *o)
    }
    pub fn construction_data(&'t self, name: String) -> Option<&'t ConstructionData<'t>> {
        self.constructions.get(&name).map(|o| *o)
    }
    pub fn object(&'t self, name: String) -> Option<&'t PredicateData<'t>> {
        self.predicates.get(&name).map(|o| *o)
    }
}
