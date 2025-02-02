from typing import Optional

from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle

from .reflection import reflect


def line_circle_other_intersection(
    first_intersection: EmbeddedPoint, line: EmbeddedLine, circle: EmbeddedCircle
) -> Optional[EmbeddedPoint]:
    orthogonal_direction = EmbeddedPoint(line.direction.y, -line.direction.x)
    symmetry_line = EmbeddedLine(circle.center, orthogonal_direction)
    other_intersection = reflect(first_intersection, symmetry_line)
    if other_intersection.is_equal(first_intersection):
        return None
    return other_intersection


def circle_circle_other_intersection(
    first_intersection: EmbeddedPoint, circle0: EmbeddedCircle, circle1: EmbeddedCircle
) -> Optional[EmbeddedPoint]:
    if circle0.center.is_equal(circle1.center):
        return None
    symmetry_line = EmbeddedLine(circle0.center, circle1.center - circle0.center)
    other_intersection = reflect(first_intersection, symmetry_line)
    if other_intersection.is_equal(first_intersection):
        return None
    return other_intersection
