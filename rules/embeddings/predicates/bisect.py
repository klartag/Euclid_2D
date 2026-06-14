from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from ..constructions.midpoint import midpoint


def bisect(line: EmbeddedLine, point0: EmbeddedPoint, point1: EmbeddedPoint) -> bool:
    """
    Checks whether `line` passes by the midpoint of `point1` and `point2`.
    """
    return line.contains_point(midpoint(point0, point1))
