from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint
from ..predicates.collinear import collinear

from .line import line
from .line_intersection import line_intersection
from .angle_bisectors import internal_angle_bisector
from .reflection import reflect_point


def isogonal_conjugate(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> EmbeddedPoint:
    if collinear(point1, point2, point3):
        raise UndefinedEmbeddingError("Cannot calculate isogonal conjugate where the triangle's vertices are collinear.")
    if collinear(point0, point1, point2) or collinear(point0, point1, point3) or collinear(point0, point2, point3):
        raise UndefinedEmbeddingError("Cannot calculate isogonal conjugate of point on a triangle's side.")
    
    bisector1 = internal_angle_bisector(point2, point1, point3)
    bisector2 = internal_angle_bisector(point1, point2, point3)

    line1 = line(point1, reflect_point(point0, bisector1))
    line2 = line(point2, reflect_point(point0, bisector2))
    
    if line1.direction.is_proportional(line2.direction):
        raise UndefinedEmbeddingError("Isogonal conjugate ended up being a point at infinity.")

    return line_intersection(line1, line2)
