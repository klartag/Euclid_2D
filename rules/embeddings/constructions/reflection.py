from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from .projection import project


def reflect_point(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedPoint:
    """
    TODO: Document
    """
    projection = project(point, line)
    return projection + projection - point


def reflect_line(line0: EmbeddedLine, line1: EmbeddedLine) -> EmbeddedLine:
    """
    TODO: Document
    """
    reflected_point0 = reflect_point(line0.point, line1)
    reflected_point1 = reflect_point(line0.point + line0.direction, line1)
    return EmbeddedLine(reflected_point0, reflected_point1 - reflected_point0)
