from mpmath import mpf
from random import uniform
from math import sin, cos

from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, PI


def new_point() -> EmbeddedPoint:
    radius = 10 * uniform(0, 1) ** 0.5
    angle = 2 * PI * uniform(0, 1)
    return EmbeddedPoint(mpf(cos(radius * angle)), mpf(sin(radius * angle)))

def new_line() -> EmbeddedLine:
    return EmbeddedLine(new_point(), new_point())

def new_circle() -> EmbeddedCircle:
    return EmbeddedCircle(new_point(), mpf(uniform(2, 7) ** 2))
