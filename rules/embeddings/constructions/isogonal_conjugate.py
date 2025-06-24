from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint
from ..predicates.collinear import collinear

from .line import line
from .line_intersection import line_intersection
from .angle_bisectors import internal_angle_bisector
from .reflection import reflect_point


def isogonal_conjugate(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint, P: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the point isogonally conjugate to P in the triangle ABC.
    """
    if collinear(B, C, P):
        raise UndefinedEmbeddingError(
            "Cannot calculate isogonal conjugate where the triangle's vertices are collinear."
        )
    if collinear(A, B, C) or collinear(A, B, P) or collinear(A, C, P):
        raise UndefinedEmbeddingError("Cannot calculate isogonal conjugate of point on a triangle's side.")

    bisector1 = internal_angle_bisector(C, B, P)
    bisector2 = internal_angle_bisector(B, C, P)

    line1 = line(B, reflect_point(A, bisector1))
    line2 = line(C, reflect_point(A, bisector2))

    if line1.direction.is_proportional(line2.direction):
        raise UndefinedEmbeddingError("Isogonal conjugate ended up being a point at infinity.")

    return line_intersection(line1, line2)
