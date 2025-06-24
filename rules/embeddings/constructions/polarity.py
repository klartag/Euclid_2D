from mpmath import mpf

from ..embedded_objects import EmbeddedPoint, EmbeddedLine
from ..undefined_embedding_error import UndefinedEmbeddingError

from .projection import project


ORIGIN = EmbeddedPoint(mpf(0), mpf(0))


def pole(line: EmbeddedLine) -> EmbeddedPoint:
    """
    Returns the pole point to a line with respect to the unit circle.
    """
    if line.contains_point(ORIGIN):
        raise UndefinedEmbeddingError("Poles are undefined for lines through the origin.")
    origin_projection = project(ORIGIN, line)
    return origin_projection.scale(origin_projection.length_squared())


def polar(point: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns the polar line to a point with respect to the unit circle.
    """
    if point.is_equal(ORIGIN):
        raise UndefinedEmbeddingError("Poles are undefined for lines through the origin.")
    inverted_point = point.scale(1 / point.length_squared())
    orthogonal_direction = EmbeddedPoint(point.y, -point.x)
    return EmbeddedLine(inverted_point, orthogonal_direction)


def line_from_origin(point: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns a line through the origin passing through a point.
    """
    if point.is_equal(ORIGIN):
        raise UndefinedEmbeddingError("Poles are undefined for lines through the origin.")
    return EmbeddedLine(ORIGIN, point)
