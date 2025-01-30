from decimal import Decimal

from ..embedded_objects import EmbeddedPoint

def midpoint(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedPoint:
    return (point0 + point1).scale(Decimal('0.5'))
