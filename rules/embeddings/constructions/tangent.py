from typing import Optional
    
from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, EPSILON

from .projection import project
from .parallels_and_perpendiculars import perpendicular_line
from .line import line


def tangent_point(line: EmbeddedLine, circle: EmbeddedCircle) -> Optional[EmbeddedPoint]:
    projection = project(circle.center, line)
    if not circle.contains_point(projection):
        return None
    return projection


def tangent_line(point: EmbeddedPoint, circle: EmbeddedCircle) -> Optional[EmbeddedLine]:
    if not circle.contains_point(point):
        return None
    center_line = line(point, circle.center)
    if center_line is None:
        return None
    return perpendicular_line(point, center_line)
