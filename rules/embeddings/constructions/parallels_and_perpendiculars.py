from mpmath import mpf

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine
from ..predicates.collinear import collinear

from .line_intersection import line_intersection
from .line import line


def parallel_line(A: EmbeddedPoint, l: EmbeddedLine) -> EmbeddedLine:
    """
    Returns a line through A and parallel to l.
    """
    return EmbeddedLine(A, l.direction)


def perpendicular_line(A: EmbeddedPoint, l: EmbeddedLine) -> EmbeddedLine:
    """
    Returns a line through A and perpendicular to l.
    """
    orthogonal_direction = EmbeddedPoint(l.direction.y, -l.direction.x)
    return EmbeddedLine(A, orthogonal_direction)


def perpendicular_bisector(A: EmbeddedPoint, B: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns the perpendicular bisector of the segment AB.
    """
    if A.is_equal(B):
        raise UndefinedEmbeddingError("Cannot calculate perpendicular bisector of two identical points.")
    midpoint = (A + B).scale(mpf('0.5'))
    direction = B - A
    orthogonal_direction = EmbeddedPoint(direction.y, -direction.x)
    return EmbeddedLine(midpoint, orthogonal_direction)


def altitude(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns the altitude from A of the triangle ABC.
    """
    if collinear(A, B, C):
        raise UndefinedEmbeddingError("Cannot calculate altitude of triangle with collinear vertices.")
    return perpendicular_line(A, line(B, C))


def orthocenter(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the orthocenter of triangle ABC.
    """
    if collinear(A, B, C):
        raise UndefinedEmbeddingError("Cannot calculate orthocenter of triangle with collinear vertices.")
    altitude0 = altitude(A, B, C)
    altitude1 = altitude(B, C, A)
    return line_intersection(altitude0, altitude1)
