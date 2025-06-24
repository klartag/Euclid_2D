from mpmath import mpf

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine
from ..predicates.collinear import collinear

from .line import line


def midpoint(A: EmbeddedPoint, B: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the midpoint of the line segment `AB`.
    """
    return (A + B).scale(mpf('0.5'))


def median(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns the median through A in triangle ABC.
    """
    if collinear(A, B, C):
        raise UndefinedEmbeddingError("Cannot calculate median of triangle with collinear vertices.")
    return line(A, midpoint(B, C))


def centroid(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the centroid of triangle ABC.
    """
    if collinear(A, B, C):
        raise UndefinedEmbeddingError("Cannot calculate centroid of triangle with collinear vertices.")
    return (A + B + C).scale(mpf('1/3'))
