from mpmath import mp, mpf, pi

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedScalar, EmbeddedCircle


def distance(A: EmbeddedPoint, B: EmbeddedPoint) -> EmbeddedScalar:
    """
    Returns the length of the segment AB.
    """
    return EmbeddedScalar((A - B).length())


def direction(A: EmbeddedPoint, B: EmbeddedPoint) -> EmbeddedScalar:
    """
    Returns the angle of the ray starting at A and passing through B.
    """
    if A.is_equal(B):
        raise UndefinedEmbeddingError("Cannot calculate direction between two identical points.")
    diff = B - A
    return EmbeddedScalar((mp.atan2(diff.y, diff.x) * 180 / pi) % 360)


def angle(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedScalar:
    """
    Returns the value of the angle ∠ABC.
    The value is in the range (-180°, 180°]
    """
    direction0 = direction(B, A)
    direction2 = direction(B, C)
    angle = (direction2.value - direction0.value) % 360
    if angle > 180:
        angle -= 360
    return EmbeddedScalar(angle)


def orientation(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedScalar:
    """
    Returns whichever of the values 90° and -90° is nearest the value of ∠ABC.
    (If A, B, C are collinear, returns 90°.)
    """
    embedded_angle = angle(A, B, C)
    if embedded_angle.value >= 0 and embedded_angle.value <= 180:
        return EmbeddedScalar(mpf(90))
    else:
        return EmbeddedScalar(mpf(-90))


def power_of_a_point(point: EmbeddedPoint, circle: EmbeddedCircle) -> EmbeddedScalar:
    """
    Returns the power of a point with respect to a circle.
    """
    return EmbeddedScalar(abs((point - circle.center).length_squared() - circle.radius_squared))


def radius(circle: EmbeddedCircle) -> EmbeddedScalar:
    """
    Returns the radius of a circle.
    """
    return EmbeddedScalar(circle.radius_squared.sqrt())


def log(scalar: EmbeddedScalar) -> EmbeddedScalar:
    """
    Returns the natural logarithm of a scalar.
    """
    if scalar.value <= 0:
        raise UndefinedEmbeddingError("Cannot calculate log of negative scalar")
    return EmbeddedScalar(mp.log(scalar.value))
