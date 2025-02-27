from typing import Optional

from ..embedded_objects import EmbeddedPoint

from .midpoint import midpoint
from .circle import circumcircle

def nine_point_circle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedPoint]:
    midpoint0 = midpoint(point1, point2)
    midpoint1 = midpoint(point2, point0)
    midpoint2 = midpoint(point0, point1)
    
    return circumcircle(midpoint0, midpoint1, midpoint2)
