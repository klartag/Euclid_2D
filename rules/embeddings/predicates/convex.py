from ..embedded_objects import EmbeddedPoint

from ..constructions.scalars import orientation
from .equality import identical


def convex(*points: EmbeddedPoint) -> bool:
    """
    TODO: Document
    """
    if len(points) <= 3:
        return True
    return identical(*[orientation(points[i - 2], points[i - 1], points[i]) for i in range(len(points))])
