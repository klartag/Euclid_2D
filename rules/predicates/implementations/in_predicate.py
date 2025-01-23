from typing import Mapping
from rules.symmetry import Symmetry
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from ...rule_utils import CIRCLE, LINE, POINT


class InPredicate(Predicate):
    NAME = 'in'

    SHAPES = [LINE, CIRCLE]

    def __init__(self, objects: tuple[GeoObject, ...]):
        super().__init__(InPredicate.NAME, objects, Symmetry.NONE)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return InPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def decompose_groups(self) -> tuple['tuple[GeoObject, ...]', 'tuple[GeoObject, ...]']:
        """
        Returns the set of points and the set of shapes referred to by the predicate.
        """
        if len(self.components) == 0:
            return ((), ())

        idx = 0
        for idx, obj in enumerate(self.components):
            if obj.type != POINT:
                break

        return self.components[:idx], self.components[idx:]

    def is_valid(self) -> bool:
        points, shapes = self.decompose_groups()

        return (
            len(points) > 0
            and len(shapes) > 0
            and all(obj.type == POINT for obj in points)
            and all(obj.type in InPredicate.SHAPES for obj in shapes)
        )

    def unpack(self) -> list[Predicate]:
        points, shapes = self.decompose_groups()
        if len(self.components) > 2:
            return [InPredicate((point, shape)) for point in points for shape in shapes]

        return [self]
