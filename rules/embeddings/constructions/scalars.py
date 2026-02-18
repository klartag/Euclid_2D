from mpmath import mp, mpf, pi

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedScalar, EmbeddedCircle


def distance(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedScalar:
    '''Returns the distance between two points.'''
    return EmbeddedScalar((point0 - point1).length())


def direction(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedScalar:
    '''Returns the direction (in degrees, mod 360) from `point0` to `point1`.'''
    if point0.is_equal(point1):
        raise UndefinedEmbeddingError("Cannot calculate direction between two identical points.")
    diff = (point1 - point0)
    return EmbeddedScalar((mp.atan2(diff.y, diff.x) * 180 / pi) % 360)


def angle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedScalar:
    '''
    Returns the angle defined by `point0`-`point1`-`point2`.
    (I.e., the amount the ray from `point1` to `point0` must be rotated (counterclockwise)
    to identify with the ray from `point1` to `point2`.)
    '''
    direction0 = direction(point1, point0)
    direction2 = direction(point1, point2)
    angle = (direction2.value - direction0.value) % 360
    if angle > 180:
        angle -= 360
    return EmbeddedScalar(angle)


def orientation(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedScalar:
    '''
    Rounds the angle `point0`-`point1`-`point2` to the nearest out of +90 and -90 degrees.
    Angles with values 0 and 180 default to rounding to 90.
    '''
    embedded_angle = angle(point0, point1, point2)
    if embedded_angle.value >= 0 and embedded_angle.value <= 180:
        return EmbeddedScalar(mpf(90))
    else:
        return EmbeddedScalar(mpf(-90))


def power_of_a_point(point: EmbeddedPoint, circle: EmbeddedCircle) -> EmbeddedScalar:
    '''Returns the power of a point with respect to a circle.'''
    return EmbeddedScalar(abs((point - circle.center).length_squared() - circle.radius_squared))


def radius(circle: EmbeddedCircle) -> EmbeddedScalar:
    '''Returns the radius of a circle.'''
    return EmbeddedScalar(circle.radius_squared.sqrt())


def log(scalar: EmbeddedScalar) -> EmbeddedScalar:
    '''Returns the log of a value.'''
    if scalar.value <= 0:
        raise UndefinedEmbeddingError("Cannot calculate log of negative scalar")
    return EmbeddedScalar(mp.log(scalar.value))
