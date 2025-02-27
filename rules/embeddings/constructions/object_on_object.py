from mpmath import mpf
from random import uniform

from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle

from .new_object import new_point

def point_on_line(line: EmbeddedLine) -> EmbeddedPoint:
    return line.point + line.direction.scale(mpf(uniform(-1, 2)))

def line_on_point(point: EmbeddedPoint) -> EmbeddedLine:
    return EmbeddedLine(point, new_point())

def point_on_circle(circle: EmbeddedCircle) -> EmbeddedPoint:
    return circle.center + new_point().normalize().scale(circle.radius_squared.sqrt())
