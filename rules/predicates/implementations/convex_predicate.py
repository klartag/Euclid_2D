from typing import Mapping
from .symmetric_predicate import SymmetricPredicate
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from ...geometry_objects.geo_type import GeoType
from ...symmetry import Symmetry


class ConvexPredicate(Predicate):
    NAME = 'convex'

    def __init__(self, objects: tuple[GeoObject, ...]):
        super().__init__(ConvexPredicate.NAME, objects, Symmetry.CIRCLE_SYMMETRY)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return ConvexPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def is_valid(self) -> bool:
        return all(obj.type == GeoType.POINT for obj in self.components)

    def unpack(self) -> list[Predicate]:
        """
        A convex predicate can be unpacked to n^2 orientation statements.
        """
        length = len(self.components)
        orientations = []
        res = []
        for i in range(length):
            for j in range(2, length - 1):
                triple: tuple[GeoObject, GeoObject, GeoObject] = (
                    self.components[i],
                    self.components[(i + 1) % length],
                    self.components[(i + j) % length],
                )
                orientations.append(ConstructionObject.from_args('orientation', triple))
                # res.append(MacroPredicate('triangle', triple))
        for i in range(1, len(orientations)):
            res.append(SymmetricPredicate('equals', (orientations[i - 1], orientations[i])))

        return res
