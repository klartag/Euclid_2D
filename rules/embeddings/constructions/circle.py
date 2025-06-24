from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EPSILON, EmbeddedPoint, EmbeddedCircle, EmbeddedScalar

from .line_intersection import line_intersection
from .parallels_and_perpendiculars import perpendicular_bisector
from .rotation import rotate_point
from .line import line


def circumcenter(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedPoint:
    """
    Returns the circumcenter of triangle ABC.
    """
    if A.is_equal(B) or A.is_equal(C) or B.is_equal(C):
        raise UndefinedEmbeddingError("Cannot calculate circumcenter when some of the points are identical.")

    if (B - A).is_proportional(C - A):
        raise UndefinedEmbeddingError("Cannot calculate circumcenter of collinear points.")

    perpendicular_bisector0 = perpendicular_bisector(A, B)
    perpendicular_bisector1 = perpendicular_bisector(A, C)

    return line_intersection(perpendicular_bisector0, perpendicular_bisector1)


def circumcircle(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedCircle:
    """
    Returns the circumcircle of triangle ABC.
    """
    center = circumcenter(A, B, C)
    return EmbeddedCircle(center, (A - center).length_squared())


def circle_from_center_and_point(A: EmbeddedPoint, B: EmbeddedPoint) -> EmbeddedCircle:
    """
    Returns a circle with center A and radius AB.
    """
    if A.is_equal(B):
        raise UndefinedEmbeddingError("Cannot create circle passing through its center.")
    return EmbeddedCircle(A, (A - B).length_squared())


def circle_from_center_and_radius(A: EmbeddedPoint, r: EmbeddedScalar) -> EmbeddedCircle:
    """
    Returns a circle with center A and radius r.
    """
    if r.value < EPSILON:
        raise UndefinedEmbeddingError("Cannot create circle of radius zero.")
    return EmbeddedCircle(A, r.value**2)


def circle_from_two_points_and_angle(A: EmbeddedPoint, B: EmbeddedPoint, angle: EmbeddedScalar) -> EmbeddedCircle:
    """
    Returns a circle defined by all points X such that the directed angle ∠AXB equals `angle`.
    """
    if A.is_equal(B):
        raise UndefinedEmbeddingError("Cannot create circle given two identical points")
    if angle.value % 180 < EPSILON or (-angle.value) % 180 < EPSILON:
        raise UndefinedEmbeddingError("Cannot create circle with arc of size 180 degrees")
    base_angle = EmbeddedScalar(90 - angle.value / 2)
    point_on_circle = line_intersection(
        line(A, rotate_point(A, B, base_angle)), line(B, rotate_point(B, A, -base_angle))
    )
    return circumcircle(A, B, point_on_circle)
