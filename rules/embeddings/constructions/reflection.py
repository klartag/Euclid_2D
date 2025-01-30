from decimal import Decimal

from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from .projection import project

def reflection(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedPoint:
    projection = project(point, line)
    return point + (projection - point).scale(Decimal(2))
