from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EPSILON, EmbeddedPoint, EmbeddedCircle, EmbeddedScalar

from .line_intersection import line_intersection
from .parallels_and_perpendiculars import perpendicular_bisector


def circumcenter(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedPoint:
    if point0.is_equal(point1) or point0.is_equal(point2) or point1.is_equal(point2):
        raise UndefinedEmbeddingError("Cannot calculate circumcenter when some of the points are identical.")

    if (point1 - point0).is_proportional(point2 - point0):
        raise UndefinedEmbeddingError("Cannot calculate circumcenter of collinear points.")

    perpendicular_bisector0 = perpendicular_bisector(point0, point1)
    perpendicular_bisector1 = perpendicular_bisector(point0, point2)

    return line_intersection(perpendicular_bisector0, perpendicular_bisector1)


def circumcircle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedCircle:
    center = circumcenter(point0, point1, point2)
    return EmbeddedCircle(center, (point0 - center).length_squared())

def circle_from_center_and_point(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedCircle:
    if point0.is_equal(point1):
        raise UndefinedEmbeddingError("Cannot create circle passing through its center.")
    return EmbeddedCircle(point0, (point0 - point1).length_squared())

def circle_from_center_and_radius(point: EmbeddedPoint, scalar: EmbeddedScalar) -> EmbeddedCircle:
    if scalar.value < EPSILON:
        raise UndefinedEmbeddingError("Cannot create circle of radius zero.")
    return EmbeddedCircle(point, scalar.value ** 2)
