from dataclasses import dataclass

from decimal import Decimal
from typing import Self

from .embedded_object import EPSILON
from .embedded_curve import EmbeddedCurve
from .point import EmbeddedPoint


@dataclass
class EmbeddedCircle(EmbeddedCurve):
    '''
    Represents a circle given a center
    and the square of its radius.
    '''

    center: EmbeddedPoint
    radius_squared: Decimal

    def is_equal(self, other: 'EmbeddedCircle') -> bool:
        return self.center.is_equal(other.center) and abs(self.radius_squared - other.radius_squared) < EPSILON**2

    def contains_point(self, point: EmbeddedPoint) -> bool:
        return abs((point - self.center).length_squared() - self.radius_squared) < EPSILON**2

    def to_dict(self) -> dict:
        return {'center': self.center.to_dict(), 'radius_squared': str(self.radius_squared)}

    def from_dict(data: dict) -> Self:
        return EmbeddedCircle(EmbeddedPoint.from_dict(data['center']), Decimal(data['radius_squared']))
