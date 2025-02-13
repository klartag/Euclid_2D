from typing import Optional
    
from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, EPSILON

from .projection import project


def tangent_point(line: EmbeddedLine, circle: EmbeddedCircle) -> Optional[EmbeddedPoint]:
    projection = project(circle.center, line)
    if abs((projection - circle.center).length_squared() - circle.radius_squared) > EPSILON**2:
        return None
    return projection
