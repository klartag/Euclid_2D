from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedCircle
from ..predicates.collinear import collinear

from .line import line
from .projection import project
from .line_intersection import line_intersection
from .angle_bisectors import internal_angle_bisector, external_angle_bisector


def incenter(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the incenter of triangle ABC.
    """
    if collinear(A, B, C):
        raise UndefinedEmbeddingError("Cannot calculate incenter of collinear points.")
    angle_bisector0 = internal_angle_bisector(A, B, C)
    angle_bisector1 = internal_angle_bisector(B, C, A)
    return line_intersection(angle_bisector0, angle_bisector1)


def excenter(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the excenter of triangle ABC in front of the vertex A.
    """
    if collinear(A, B, C):
        raise UndefinedEmbeddingError("Cannot calculate excenter of collienar points.")
    angle_bisector0 = external_angle_bisector(A, B, C)
    angle_bisector1 = external_angle_bisector(B, C, A)
    return line_intersection(angle_bisector0, angle_bisector1)


def incircle(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedCircle:
    """
    Returns the incircle of triangle ABC.
    """
    center = incenter(A, B, C)
    radius_squared = (project(center, line(B, C)) - center).length_squared()
    return EmbeddedCircle(center, radius_squared)


def excircle(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedCircle:
    """
    Returns the excircle of triangle ABC in front of the vertex A.
    """
    center = excenter(A, B, C)
    radius_squared = (project(center, line(B, C)) - center).length_squared()
    return EmbeddedCircle(center, radius_squared)
