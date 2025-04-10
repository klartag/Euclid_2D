from typing import Optional
from mpmath import mpf

from ..embedded_objects import EmbeddedPoint, EmbeddedLine
from ..undefined_embedding_error import UndefinedEmbeddingError

from .projection import project


ORIGIN = EmbeddedPoint(mpf(0), mpf(0))


def pole(line: EmbeddedLine) -> EmbeddedPoint:
    origin_projection = project(ORIGIN, line)
    if origin_projection.is_equal(ORIGIN):
        raise UndefinedEmbeddingError("Poles are undefined for lines through the origin.")
    return origin_projection / origin_projection.length_squared()


def polar(point: EmbeddedPoint) -> EmbeddedLine:
    if point.is_equal(ORIGIN):
        raise UndefinedEmbeddingError("Poles are undefined for lines through the origin.")
    inverted_point = point / point.length_squared()
    orthogonal_direction = EmbeddedPoint(point.y, -point.x)
    return EmbeddedLine(inverted_point, orthogonal_direction)
