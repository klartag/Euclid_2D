from dataclasses import dataclass

from mpmath import mpf
from typing import Self

from .embedded_object import EmbeddedObject, EPSILON


@dataclass
class EmbeddedScalar(EmbeddedObject):
    '''
    Represents the point (x, y).
    '''

    value: mpf

    def is_equal(self, other: 'EmbeddedScalar') -> bool:
        return abs(self.value - other.value) < EPSILON

    def to_dict(self) -> dict:
        return { 'value': str(self.value) }
    
    def from_dict(data: dict) -> Self:
        return EmbeddedScalar(mpf(data['value']))
