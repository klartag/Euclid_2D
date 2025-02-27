from typing import Optional

from ..embedded_objects import EPSILON, EmbeddedPoint, EmbeddedCircle, EmbeddedScalar

from .line_intersection import line_intersection
from .parallels_and_perpendiculars import perpendicular_bisector


def circumcenter(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedPoint]:
    if point0.is_equal(point1) or point0.is_equal(point2) or point1.is_equal(point2):
        return None

    if (point1 - point0).is_proportional(point2 - point0):
        return None

    perpendicular_bisector0 = perpendicular_bisector(point0, point1)
    perpendicular_bisector1 = perpendicular_bisector(point0, point2)

    if perpendicular_bisector0 is None or perpendicular_bisector1 is None:
        return None

    return line_intersection(perpendicular_bisector0, perpendicular_bisector1)


def circumcircle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedCircle]:
    center = circumcenter(point0, point1, point2)

    if center is None:
        return None

    return EmbeddedCircle(center, (point0 - center).length_squared())

def circle_from_center_and_point(point0: EmbeddedPoint, point1: EmbeddedPoint) -> Optional[EmbeddedCircle]:
    if point0.is_equal(point1):
        return None
    return EmbeddedCircle(point0, (point0 - point1).length_squared())

def circle_from_center_and_radius(point: EmbeddedPoint, scalar: EmbeddedScalar) -> Optional[EmbeddedCircle]:
    if scalar.value < EPSILON:
        return None
    return EmbeddedCircle(point, scalar.value ** 2)
