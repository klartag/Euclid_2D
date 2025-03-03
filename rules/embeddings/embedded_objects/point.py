from dataclasses import dataclass

from decimal import Decimal
from typing import Self

from .embedded_object import EmbeddedObject, EPSILON


@dataclass
class EmbeddedPoint(EmbeddedObject):
    '''
    Represents the point (x, y).
    '''

    x: Decimal
    y: Decimal

    def is_equal(self, other: 'EmbeddedPoint') -> bool:
        return abs(self.x - other.x) < EPSILON and abs(self.y - other.y) < EPSILON

    def __add__(self, other: 'EmbeddedPoint') -> 'EmbeddedPoint':
        return EmbeddedPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'EmbeddedPoint') -> 'EmbeddedPoint':
        return EmbeddedPoint(self.x - other.x, self.y - other.y)

    def __neg__(self) -> 'EmbeddedPoint':
        return EmbeddedPoint(-self.x, -self.y)

    def is_proportional(self, other: 'EmbeddedPoint') -> bool:
        if abs(self.x) < EPSILON or abs(other.x) < EPSILON:
            return abs(self.x) < EPSILON and abs(other.x) < EPSILON

        if abs(self.y) < EPSILON or abs(other.y) < EPSILON:
            return abs(self.y) < EPSILON and abs(other.y) < EPSILON

        return abs(self.x * other.y - self.y * other.x) < EPSILON**2

    def scalar_product(self, other: 'EmbeddedPoint') -> Decimal:
        return self.x * other.x + self.y * other.y

    def length_squared(self) -> Decimal:
        return self.scalar_product(self)

    def length(self) -> Decimal:
        return self.length_squared().sqrt()

    def scale(self, ratio: Decimal) -> 'EmbeddedPoint':
        return EmbeddedPoint(self.x * ratio, self.y * ratio)

    def normalize(self) -> 'EmbeddedPoint':
        return self.scale(1 / self.length())
    
    def to_dict(self) -> dict:
        return {
            'x': str(self.x),
            'y': str(self.y)
        }
    
    def from_dict(data: dict) -> Self:
        return EmbeddedPoint(Decimal(data['x']), Decimal(data['y']))
