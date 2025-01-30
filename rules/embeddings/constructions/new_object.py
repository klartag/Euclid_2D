from decimal import Decimal
from random import normalvariate

from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle


def new_point() -> EmbeddedPoint:
    return EmbeddedPoint(Decimal(normalvariate()), Decimal(normalvariate()))

def new_line() -> EmbeddedLine:
    return EmbeddedLine(new_point(), new_point())

def new_circle() -> EmbeddedCircle:
    return EmbeddedCircle(new_point(), Decimal(normalvariate() ** 2))
