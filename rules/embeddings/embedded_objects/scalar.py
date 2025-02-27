from dataclasses import dataclass

from mpmath import mpf
from typing import Self

from ...rule_utils import SCALAR

from .embedded_object import EmbeddedObject, EPSILON


@dataclass
class EmbeddedScalar(EmbeddedObject):
    '''
    Represents the point (x, y).
    '''

    value: mpf
    
    def _type(self) -> str:
        return SCALAR

    def is_equal(self, other: 'EmbeddedScalar') -> bool:
        return abs(self.value - other.value) < EPSILON

    def __add__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value + other.value)

    def __sub__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value - other.value)
    
    def __neg__(self) -> Self:
        return EmbeddedScalar(-self.value)
    
    def __mul__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value * other.value)
    
    def __div__(self, other: Self) -> Self:
        return EmbeddedScalar(self.value / other.value)
    
    def to_dict(self) -> dict:
        return { 'value': str(self.value) }
    
    def from_dict(data: dict) -> Self:
        return EmbeddedScalar(mpf(data['value']))
