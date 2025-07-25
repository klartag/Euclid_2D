from dataclasses import dataclass

from mpmath import mpf
from typing import Self

from ...geometry_objects.geo_type import GeoType

from .embedded_object import EmbeddedObject, EPSILON


@dataclass
class EmbeddedScalar(EmbeddedObject):
    '''
    Represents the point (x, y).
    '''

    value: mpf

    def _type(self) -> str:
        return GeoType.SCALAR

    def is_equal(self, other: 'EmbeddedScalar') -> bool:
        return abs(self.value - other.value) < EPSILON

    def is_equal_mod(self, other: 'EmbeddedScalar', modulus: 'EmbeddedScalar') -> bool:
        return abs((self.value - other.value) % modulus.value) < EPSILON

    def __add__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value + other.value)

    def __sub__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value - other.value)

    def __neg__(self) -> Self:
        return EmbeddedScalar(-self.value)

    def __mul__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value * other.value)

    def __truediv__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value / other.value)

    def to_dict(self) -> dict:
        return {'value': str(self.value)}

    def from_dict(data: dict) -> Self:
        return EmbeddedScalar(mpf(data['value']))

    def to_str(self, accuracy: int) -> str:
        return f'Scalar({round(self.value, accuracy)})'
