from typing import Mapping
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from .symmetric_predicate import SymmetricPredicate


class ExistsPredicate(SymmetricPredicate):
    NAME = 'exists'

    def __init__(self, objects: tuple[GeoObject, ...]):
        super().__init__(ExistsPredicate.NAME, objects)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return ExistsPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def is_valid(self) -> bool:
        return True

    def unpack(self) -> list[Predicate]:
        return [ExistsPredicate((obj,)) for obj in self.components]
