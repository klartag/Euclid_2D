from mpmath import mpf
from random import normalvariate

from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle


def new_point() -> EmbeddedPoint:
    return EmbeddedPoint(mpf(normalvariate()), mpf(normalvariate()))

def new_line() -> EmbeddedLine:
    return EmbeddedLine(new_point(), new_point())

def new_circle() -> EmbeddedCircle:
    return EmbeddedCircle(new_point(), mpf(normalvariate() ** 2))
