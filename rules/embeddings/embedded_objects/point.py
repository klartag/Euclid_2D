from dataclasses import dataclass

from mpmath import mpf
from typing import Self

from ...geometry_objects.geo_type import GeoType
from .embedded_object import EmbeddedObject, EPSILON


@dataclass
class EmbeddedPoint(EmbeddedObject):
    '''
    Represents the point (x, y).
    '''

    x: mpf
    y: mpf

    def _type(self) -> str:
        return GeoType.POINT

    def is_equal(self, other: EmbeddedObject) -> bool:
        return other._type() == GeoType.POINT and abs(self.x - other.x) < EPSILON and abs(self.y - other.y) < EPSILON

    def __add__(self, other: 'EmbeddedPoint') -> 'EmbeddedPoint':
        return EmbeddedPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'EmbeddedPoint') -> 'EmbeddedPoint':
        return EmbeddedPoint(self.x - other.x, self.y - other.y)

    def __neg__(self) -> 'EmbeddedPoint':
        return EmbeddedPoint(-self.x, -self.y)

    def is_proportional(self, other: 'EmbeddedPoint') -> bool:
        """
        Returns whether two points lie on the same line through the origin.
        (If any of the points equals the origin, returns whether both points equal the origin.)
        """
        if self.length_squared() < EPSILON**2 or other.length_squared() < EPSILON**2:
            return self.length_squared() < EPSILON**2 and other.length_squared() < EPSILON**2

        if abs(self.x) < EPSILON or abs(other.x) < EPSILON:
            return abs(self.x) < EPSILON and abs(other.x) < EPSILON

        if abs(self.y) < EPSILON or abs(other.y) < EPSILON:
            return abs(self.y) < EPSILON and abs(other.y) < EPSILON

        return abs(self.x * other.y - self.y * other.x) < EPSILON**2

    def scalar_product(self, other: 'EmbeddedPoint') -> mpf:
        """
        Returns the dot product of two points.
        """
        return self.x * other.x + self.y * other.y

    def length_squared(self) -> mpf:
        """
        Returns the square of the distance of this point to the origin.
        """
        return self.scalar_product(self)

    def length(self) -> mpf:
        """
        Returns the distance from this point to the origin.
        """
        return self.length_squared().sqrt()

    def scale(self, ratio: mpf) -> 'EmbeddedPoint':
        """
        Scales the point by a scalar with respect to the origin.
        """
        return EmbeddedPoint(self.x * ratio, self.y * ratio)

    def normalize(self) -> 'EmbeddedPoint':
        """
        Scales this point with respect to the origin so that it lies on the unit circle.
        """
        return self.scale(1 / self.length())

    def to_dict(self) -> dict:
        return {'x': str(self.x), 'y': str(self.y)}

    def from_dict(data: dict) -> Self:
        return EmbeddedPoint(mpf(data['x']), mpf(data['y']))

    def to_str(self, accuracy: int) -> str:
        return f'({round(self.x, accuracy)}, {round(self.y, accuracy)})'
