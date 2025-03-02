from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EPSILON, EmbeddedPoint, EmbeddedCircle, EmbeddedScalar

from .line_intersection import line_intersection
from .parallels_and_perpendiculars import perpendicular_bisector
from .rotation import rotate_point
from .line import line


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

def circle_from_two_points_and_angle(point0: EmbeddedPoint, point1: EmbeddedPoint, angle: EmbeddedScalar) -> EmbeddedCircle:
    if point0.is_equal(point1):
        raise UndefinedEmbeddingError("Cannot create circle given two identical points")
    if angle.value % 180 < EPSILON or (-angle.value) % 180 < EPSILON:
        raise UndefinedEmbeddingError("Cannot create circle with arc of size 180 degrees")
    base_angle = EmbeddedScalar(90 - angle.value / 2)
    point_on_circle = line_intersection(
        line(point0, rotate_point(point0, point1, base_angle)),
        line(point1, rotate_point(point1, point0, -base_angle))
    )
    return circumcircle(point0, point1, point_on_circle)
