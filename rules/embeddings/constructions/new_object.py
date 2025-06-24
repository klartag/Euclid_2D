from mpmath import mpf
from random import uniform
from math import sin, cos

from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, PI


def new_point() -> EmbeddedPoint:
    """
    Returns a random new point.
    """
    radius = 10 * uniform(0, 1) ** 0.5
    angle = 2 * PI * uniform(0, 1)
    return EmbeddedPoint(mpf(radius * cos(angle)), mpf(radius * sin(angle)))


def new_line() -> EmbeddedLine:
    """
    Returns a random new line.
    """
    return EmbeddedLine(new_point(), new_point())


def new_circle() -> EmbeddedCircle:
    """
    Returns a random new circle.
    """
    return EmbeddedCircle(new_point(), mpf(uniform(2, 7) ** 2))
