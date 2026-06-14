from ..embedded_objects import EmbeddedPoint

from ..constructions.scalars import orientation
from .equality import identical


def convex(*points: EmbeddedPoint) -> bool:
    """
    Checks whether a list of points are the vertices of a convex polygon,
    ordered either clockwise or counterclockwise.
    """
    if len(points) <= 3:
        return True
    return identical(*[orientation(points[i - 2], points[i - 1], points[i]) for i in range(len(points))])
