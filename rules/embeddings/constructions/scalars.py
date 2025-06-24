from mpmath import mp, mpf, pi

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedScalar, EmbeddedCircle


def distance(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedScalar:
    """
    TODO: Document
    """
    return EmbeddedScalar((point0 - point1).length())


def direction(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedScalar:
    """
    TODO: Document
    """
    if point0.is_equal(point1):
        raise UndefinedEmbeddingError("Cannot calculate direction between two identical points.")
    diff = point1 - point0
    return EmbeddedScalar((mp.atan2(diff.y, diff.x) * 180 / pi) % 360)


def angle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedScalar:
    """
    TODO: Document
    """
    direction0 = direction(point1, point0)
    direction2 = direction(point1, point2)
    angle = (direction2.value - direction0.value) % 360
    if angle > 180:
        angle -= 360
    return EmbeddedScalar(angle)


def orientation(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedScalar:
    """
    TODO: Document
    """
    embedded_angle = angle(point0, point1, point2)
    if embedded_angle.value >= 0 and embedded_angle.value <= 180:
        return EmbeddedScalar(mpf(90))
    else:
        return EmbeddedScalar(mpf(-90))


def power_of_a_point(point: EmbeddedPoint, circle: EmbeddedCircle) -> EmbeddedScalar:
    """
    TODO: Document
    """
    return EmbeddedScalar(abs((point - circle.center).length_squared() - circle.radius_squared))


def radius(circle: EmbeddedCircle) -> EmbeddedScalar:
    """
    TODO: Document
    """
    return EmbeddedScalar(circle.radius_squared.sqrt())


def log(scalar: EmbeddedScalar) -> EmbeddedScalar:
    """
    TODO: Document
    """
    if scalar.value <= 0:
        raise UndefinedEmbeddingError("Cannot calculate log of negative scalar")
    return EmbeddedScalar(mp.log(scalar.value))
