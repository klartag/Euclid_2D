from dataclasses import dataclass
from typing import Self

from ...rule_utils import GeoType

from .embedded_object import EmbeddedObject
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
        return GeoType.LINE

    def is_equal(self, other: EmbeddedObject):
        if other._type() != GeoType.LINE:
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

    def to_str(self, accuracy: int) -> str:
        return f'Line({self.point.to_str(accuracy)}, {(self.point + self.direction).to_str(accuracy)})'
