from decimal import Decimal

from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from .projection import project


def reflect(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedPoint:
    projection = project(point, line)
    return projection + projection - point
