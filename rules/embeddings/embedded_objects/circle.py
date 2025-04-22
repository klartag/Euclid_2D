from dataclasses import dataclass

from mpmath import mpf
from typing import Self

from ...rule_utils import CIRCLE

from .embedded_object import EPSILON, EmbeddedObject
from .embedded_curve import EmbeddedCurve
from .point import EmbeddedPoint


@dataclass
class EmbeddedCircle(EmbeddedCurve):
    '''
    Represents a circle given a center
    and the square of its radius.
    '''

    center: EmbeddedPoint
    radius_squared: mpf
    
    def _type(self) -> str:
        return CIRCLE

    def is_equal(self, other: EmbeddedObject) -> bool:
        return other._type() == CIRCLE and self.center.is_equal(other.center) and abs(self.radius_squared - other.radius_squared) < EPSILON**2

    def contains_point(self, point: EmbeddedPoint) -> bool:
        return abs((point - self.center).length_squared() - self.radius_squared) < EPSILON**2

    def to_dict(self) -> dict:
        return {'center': self.center.to_dict(), 'radius_squared': str(self.radius_squared)}

    def from_dict(data: dict) -> Self:
        return EmbeddedCircle(EmbeddedPoint.from_dict(data['center']), mpf(data['radius_squared']))

    def to_str(self, accuracy: int) -> str:
        return f'Circle({self.center.to_str(accuracy)}, {round(self.radius_squared ** 0.5, accuracy)})'
