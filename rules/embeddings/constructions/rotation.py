from mpmath import mp

from ..embedded_objects import EmbeddedPoint, EmbeddedScalar, PI

from .scalars import direction


def rotate_point(A: EmbeddedPoint, B: EmbeddedPoint, angle: EmbeddedScalar) -> EmbeddedPoint:
    """
    Returns a point C such that the segments AB and AC have the same length,
    and such that the directed angle ∠BAC equals `angle`.
    """
    new_angle = direction(A, B) + angle
    new_direction = EmbeddedPoint(mp.cos(new_angle.value * PI / 180), mp.sin(new_angle.value * PI / 180))
    return A + new_direction.scale((B - A).length())
