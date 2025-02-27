from typing import Optional
from mpmath import mpf

from ..embedded_objects import EmbeddedPoint
from ..predicates.collinear import collinear

from .line import line
from .line_intersection import line_intersection
from .angle_bisectors import internal_angle_bisector
from .reflection import reflect_point


def isogonal_conjugate(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> Optional[EmbeddedPoint]:
    if collinear(point0, point1, point2):
        return None
    if collinear(point0, point1, point3):
        return None
    if collinear(point0, point2, point3):
        return None
    if collinear(point1, point2, point3):
        return None
    
    bisector1 = internal_angle_bisector(point2, point1, point3)
    bisector2 = internal_angle_bisector(point1, point2, point3)
    if bisector1 is None or bisector2 is None:
        return None
    
    line1 = line(point1, reflect_point(point0, bisector1))
    line2 = line(point2, reflect_point(point0, bisector2))
    if line1 is None or line2 is None:
        return None
    
    if line1.direction.is_proportional(line2.direction):
        return None

    return line_intersection(line1, line2)
