from typing import Mapping
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from ...symmetry import Symmetry


SIMPLE_SYMMETRIC_PREDICATE_NAMES: set[str] = {
    'equals',
    'equals_mod_360',
    'not_equals',
    'not_collinear',
}


class SymmetricPredicate(Predicate):
    def __init__(self, name: str, objects: tuple[GeoObject, ...]):
        super().__init__(name, objects, Symmetry.ALL)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return SymmetricPredicate(self.name, tuple(obj.substitute(replacements) for obj in self.components))
