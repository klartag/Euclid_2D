from mpmath import mpf

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine
from ..predicates.collinear import collinear

from .line import line

def midpoint(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedPoint:
    return (point0 + point1).scale(mpf('0.5'))


def median(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedLine:
    if collinear(point0, point1, point2):
        raise UndefinedEmbeddingError("Cannot calculate median of triangle with collinear vertices.")
    return line(point0, midpoint(point1, point2))


def centroid(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedPoint:
    if collinear(point0, point1, point2):
        raise UndefinedEmbeddingError("Cannot calculate centroid of triangle with collinear vertices.")
    return (point0 + point1 + point2).scale(mpf('1/3'))
