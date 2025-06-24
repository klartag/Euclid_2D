from typing import Mapping

from ...geometry_objects.geo_type import GeoType
from .symmetric_predicate import SymmetricPredicate
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from ...symmetry import Symmetry


class BetweenPredicate(Predicate):
    """
    TODO: Document
    """

    NAME = 'between'

    """
    The between predicate satisfies between(A, B, C) <=> between(C, B, A).
    """

    def __init__(self, objects: 'tuple[GeoObject, ...]'):
        super().__init__(BetweenPredicate.NAME, objects, Symmetry.BETWEEN)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return BetweenPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def is_valid(self) -> bool:
        return len(self.components) >= 3 and all(obj.type == GeoType.POINT for obj in self.components)

    def unpack(self) -> list[Predicate]:
        objs = self.components
        n = len(objs)
        betweens_list = [BetweenPredicate(objs[i : i + 3]) for i in range(n - 2)]
        collinears_list = [SymmetricPredicate('collinear', objs[i : i + 3]) for i in range(n - 2)]

        return betweens_list + collinears_list
