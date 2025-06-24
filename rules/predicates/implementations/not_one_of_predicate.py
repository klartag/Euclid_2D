from typing import Mapping
from .symmetric_predicate import SymmetricPredicate
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from ...symmetry import Symmetry


class NotOneOfPredicate(Predicate):
    """
    TODO: Document
    """

    NAME = 'not_one_of'

    def __init__(self, objects: 'tuple[GeoObject, ...]'):
        super().__init__(NotOneOfPredicate.NAME, objects, Symmetry.LAST_ELEMENTS)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return NotOneOfPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def is_valid(self) -> bool:
        if len(self.components) == 0:
            return True
        first_type = self.components[0].type
        return all(obj.type == first_type for obj in self.components)

    def unpack(self) -> list[Predicate]:
        inputs = self.components
        first_input = inputs[0]
        last_inputs = inputs[1:]
        return [SymmetricPredicate('not_equals', (first_input, obj)) for obj in last_inputs]
