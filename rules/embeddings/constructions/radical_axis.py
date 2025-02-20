from typing import Optional
    
from ..embedded_objects import EmbeddedLine, EmbeddedCircle

from .line import line
from .parallels_and_perpendiculars import perpendicular_line


def radical_axis(circle0: EmbeddedCircle, circle1: EmbeddedCircle) -> Optional[EmbeddedLine]:
    center_line = line(circle0.center, circle1.center)
    if center_line is None:
        return None
    
    ratio = (1 + (circle0.radius_squared - circle1.radius_squared) / (circle0.center - circle1.center).length_squared()) / 2
    point_on_radical_axis = circle0.center + (circle1.center - circle0.center).scale(ratio)
    return perpendicular_line(point_on_radical_axis, center_line)
