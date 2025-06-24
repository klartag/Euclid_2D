from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from .projection import project


def reflect_point(A: EmbeddedPoint, l: EmbeddedLine) -> EmbeddedPoint:
    """
    Returns the reflection of the point A around the line l.
    """
    projection = project(A, l)
    return projection + projection - A


def reflect_line(l: EmbeddedLine, m: EmbeddedLine) -> EmbeddedLine:
    """
    Returns the reflection of the line l around the line m.
    """
    reflected_point0 = reflect_point(l.point, m)
    reflected_point1 = reflect_point(l.point + l.direction, m)
    return EmbeddedLine(reflected_point0, reflected_point1 - reflected_point0)
