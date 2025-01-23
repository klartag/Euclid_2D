from decimal import Decimal
from typing import List, Mapping, Tuple, Optional

from ...embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from .embedded_construction import EmbeddedConstruction


def perpendicular_bisector(point0: EmbeddedPoint, point1: EmbeddedPoint) -> Optional[EmbeddedLine]:
    if point0.is_equal(point1):
        return None
    midpoint = (point0 + point1).scale(Decimal('0.5'))
    direction = point1 - point0
    orthogonal_direction = EmbeddedPoint(direction.y, -direction.x)
    return EmbeddedLine(midpoint, orthogonal_direction)


class PerpendicularBisector(EmbeddedConstruction[Tuple[EmbeddedPoint, EmbeddedPoint], EmbeddedLine]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedLine]:
        (point0, point1) = self.get_parameters(embedded_objects)
        return perpendicular_bisector(point0, point1)
