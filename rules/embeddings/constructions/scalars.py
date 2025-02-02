from typing import Optional

from mpmath import mp, mpf

from ..embedded_objects import EmbeddedPoint, EmbeddedScalar, EmbeddedCircle


def distance(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedScalar:
    return EmbeddedScalar((point0 - point1).length())


def direction(point0: EmbeddedPoint, point1: EmbeddedPoint) -> Optional[EmbeddedScalar]:
    if point0.is_equal(point1):
        return None

    diff = (point1 - point0)
    return EmbeddedScalar(mp.atan2(diff.y, diff.x) % 360)


def angle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedScalar]:
    direction0 = direction(point1, point0)
    direction2 = direction(point1, point2)
    if direction0 is None or direction2 is None:
        return None
    return EmbeddedScalar((direction2.value - direction0.value) % 360)


def orientation(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> Optional[EmbeddedScalar]:
    embedded_angle = angle(point0, point1, point2)
    if embedded_angle is None:
        return None
    if embedded_angle.value >= 0 and embedded_angle.value <= 180:
        return EmbeddedScalar(mpf(90))
    else:
        return EmbeddedScalar(mpf(-90))


def power_of_a_point(point: EmbeddedPoint, circle: EmbeddedCircle) -> EmbeddedScalar:
    return EmbeddedScalar((point - circle.center).length_squared() - circle.radius_squared)


def radius(circle: EmbeddedCircle) -> EmbeddedScalar:
    return EmbeddedScalar(circle.radius_squared.sqrt())
