from ..embedded_objects import EmbeddedPoint
from ..embedded_objects.embedded_curve import EmbeddedCurve


def _in(point: EmbeddedPoint, curve: EmbeddedCurve) -> bool:
    return curve.contains_point(point)


def not_in(point: EmbeddedPoint, curve: EmbeddedCurve) -> bool:
    return not _in(point, curve)
