from mpmath import mpf
from typing import Optional
from ..embedded_objects import EmbeddedPoint, EmbeddedLine


def parallel_line(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedLine:
    return EmbeddedLine(point, line.direction)


def perpendicular_bisector(point0: EmbeddedPoint, point1: EmbeddedPoint) -> Optional[EmbeddedLine]:
    if point0.is_equal(point1):
        return None
    midpoint = (point0 + point1).scale(mpf('0.5'))
    direction = point1 - point0
    orthogonal_direction = EmbeddedPoint(direction.y, -direction.x)
    return EmbeddedLine(midpoint, orthogonal_direction)
