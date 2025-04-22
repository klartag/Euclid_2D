from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from ..constructions.midpoint import midpoint


def bisect(line: EmbeddedLine, point0: EmbeddedPoint, point1: EmbeddedPoint) -> bool:
    return line.contains_point(midpoint(point0, point1))
