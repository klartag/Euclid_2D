import itertools
from typing import Mapping

from ...geometry_objects.geo_object import GeoObject

from ..predicate import Predicate
from .symmetric_predicate import SymmetricPredicate


class DistinctPredicate(SymmetricPredicate):
    NAME = 'distinct'

    def __init__(self, objects: tuple[GeoObject, ...]):
        super().__init__(DistinctPredicate.NAME, objects)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return DistinctPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def is_valid(self) -> bool:
        if len(self.components) == 0:
            return True
        first_type = self.components[0].type
        return all(obj.type == first_type for obj in self.components)

    def unpack(self) -> list[Predicate]:
        return [SymmetricPredicate('not_equals', (o1, o2)) for o1, o2 in itertools.combinations(self.components, 2)]
