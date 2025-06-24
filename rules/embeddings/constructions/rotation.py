from mpmath import mp

from ..embedded_objects import EmbeddedPoint, EmbeddedScalar, PI

from .scalars import direction


def rotate_point(point0: EmbeddedPoint, point1: EmbeddedPoint, angle: EmbeddedScalar) -> EmbeddedPoint:
    new_angle = direction(point0, point1) + angle
    new_direction = EmbeddedPoint(mp.cos(new_angle.value * PI / 180), mp.sin(new_angle.value * PI / 180))
    return point0 + new_direction.scale((point1 - point0).length())
