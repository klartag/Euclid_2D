from ..embedded_objects import EmbeddedPoint

from .midpoint import midpoint
from .circle import circumcircle


def nine_point_circle(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the nine-point circle of triangle ABC.
    """
    midpoint0 = midpoint(B, C)
    midpoint1 = midpoint(C, A)
    midpoint2 = midpoint(A, B)

    return circumcircle(midpoint0, midpoint1, midpoint2)
