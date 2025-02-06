from dataclasses import dataclass
from mpmath import mp, mpf
from typing import Optional, Self

from ...rule_utils import LINE

from .embedded_object import EPSILON, EmbeddedObject
from .embedded_curve import EmbeddedCurve
from .point import EmbeddedPoint


@dataclass
class EmbeddedLine(EmbeddedCurve):
    '''
    Represents a line, going through `point`,
    and looking towards the direction `direction`.
    '''

    point: EmbeddedPoint
    direction: EmbeddedPoint

    def _type(self) -> str:
        return LINE

    @staticmethod
    def from_equation(a: mpf, b: mpf, c: mpf) -> Optional['EmbeddedLine']:
        '''
        Creates a line that satisfies the equation `a*x + b*y + c == 0`.
        '''
        if abs(a) < EPSILON and abs(b) < EPSILON:
            return None

        point: EmbeddedPoint
        if abs(a) / abs(b) < 0.1:
            point = EmbeddedPoint(mpf('0'), -c / b)
        elif abs(b) / abs(a) < 0.1:
            point = EmbeddedPoint(-c / a, mpf('0'))
        else:
            point = EmbeddedPoint(mpf('1') * mp.sign(a), mpf('1') * mp.sign(b)).scale(-c / (a + b))

        direction = EmbeddedPoint(-b, a)

        return EmbeddedLine(point, direction)

    def is_equal(self, other: EmbeddedObject):
        if other._type() != LINE:
            return False

        if self.point.is_equal(other.point):
            return self.direction.is_proportional(other.direction)

        delta = self.point - other.point
        return delta.is_proportional(self.direction) and delta.is_proportional(other.direction)

    def contains_point(self, point: EmbeddedPoint) -> bool:
        return self.point.is_equal(point) or (point - self.point).is_proportional(self.direction)

    def to_dict(self) -> dict:
        return {'point': self.point.to_dict(), 'direction': self.direction.to_dict()}

    def from_dict(data: dict) -> Self:
        return EmbeddedLine(EmbeddedPoint.from_dict(data['point']), EmbeddedPoint.from_dict(data['direction']))
