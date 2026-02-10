from typing import Tuple
from mpmath import mpf

from ..embedded_objects import EmbeddedPoint, EPSILON


def collinear(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> bool:
    """
    Checks whether three points are on the same line.
    """
    if point0.is_equal(point1) or point0.is_equal(point2):
        return True
    return (point1 - point0).is_proportional(point2 - point0)


def not_collinear(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> bool:
    """
    Checks whether three points are not on the same line.
    """
    return not collinear(point0, point1, point2)


def between(*points: Tuple[EmbeddedPoint, ...]) -> bool:
    """
    Checks whether a list of points are on the same line, and also in that order.
    """
    for i in range(len(points) - 2):
        point0, point1, point2 = points[i : i + 3]
        if not collinear(point0, point1, point2):
            return False
        if not is_scalar_between(point0.x, point1.x, point2.x):
            return False
        if not is_scalar_between(point0.y, point1.y, point2.y):
            return False
    return True


def collinear_and_not_between(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> bool:
    """
    Checks whether three points are on the same line, and *not* in that order.
    """
    return collinear(point0, point1, point2) and not between(point0, point1, point2)


def is_scalar_between(x: mpf, y: mpf, z: mpf) -> bool:
    """
    Checks whether three scalars are ordered monotonically.
    """
    return x - EPSILON <= y <= z + EPSILON or x + EPSILON >= y >= z - EPSILON
