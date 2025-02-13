from typing import Optional

from ..embedded_objects import EmbeddedPoint, EmbeddedCircle
from ..predicates.collinear import collinear

from .line import line
from .projection import project
from .line_intersection import line_intersection
from .angle_bisectors import internal_angle_bisector, external_angle_bisector

def incenter(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedPoint]:
    if collinear(point0, point1, point2):
        return None
    angle_bisector0 = internal_angle_bisector(point0, point1, point2)
    angle_bisector1 = internal_angle_bisector(point1, point2, point0)
    if angle_bisector0 is None or angle_bisector1 is None:
        return None
    return line_intersection(angle_bisector0, angle_bisector1)

def excenter(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedPoint]:
    if collinear(point0, point1, point2):
        return None
    angle_bisector0 = external_angle_bisector(point0, point1, point2)
    angle_bisector1 = external_angle_bisector(point1, point2, point0)
    if angle_bisector0 is None or angle_bisector1 is None:
        return None
    return line_intersection(angle_bisector0, angle_bisector1)

def incircle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedCircle]:
    center = incenter(point0, point1, point2)
    if center is None:
        return None
    radius_squared = (project(center, line(point1, point2)) - center).length_squared()
    return EmbeddedCircle(center, radius_squared)

def excircle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedCircle]:
    center = excenter(point0, point1, point2)
    if center is None:
        return None
    radius_squared = (project(center, line(point1, point2)) - center).length_squared()
    return EmbeddedCircle(center, radius_squared)
