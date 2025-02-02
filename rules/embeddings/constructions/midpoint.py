from mpmath import mpf

from ..embedded_objects import EmbeddedPoint

def midpoint(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedPoint:
    return (point0 + point1).scale(mpf('0.5'))
