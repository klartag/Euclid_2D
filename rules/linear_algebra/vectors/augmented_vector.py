from fractions import Fraction
from typing import Generic, Literal, Optional, Self, TypeVar

from .abstract_vector import AbstractVector
from .proper_vector import ProperVector


DENSE_THRESHOLD = 1 / 4
SPARSE_THRESHOLD = 1 / 20

V = TypeVar('V', bound=ProperVector)
C = TypeVar('C')


class AugmentedVector(Generic[V, C], AbstractVector):
    type_name: Literal['Augmented'] = 'Augmented'

    vector: V
    constant: C

    def __init__(self, vector: V, constant: C):
        self.vector = vector
        self.constant = constant

    def clone(self) -> 'AugmentedVector[V, C]':
        return AugmentedVector(self.vector.clone(), self.constant)

    def __mul__(self, x: Fraction) -> 'AugmentedVector[V, C]':
        return AugmentedVector(self.vector * x, self.constant * x)

    def __truediv__(self, x: Fraction) -> 'AugmentedVector[V, C]':
        return AugmentedVector(self.vector / x, self.constant / x)

    def __add__(self, other: Self) -> 'AugmentedVector[V, C]':
        return AugmentedVector(self.vector + other.vector, self.constant + other.constant)

    def __sub__(self, other: Self) -> 'AugmentedVector[V, C]':
        return AugmentedVector(self.vector - other.vector, self.constant - other.constant)

    def __eq__(self, other: Self) -> bool:
        return self.vector == other.vector and self.constant == other.constant

    def inner_repr(self) -> str:
        return f'{self.vector.inner_repr()}, {self.constant}'

    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        return self.vector.taxicab_norm(max_index)
    
    def __str__(self) -> str:
        return f'Augmented[{self.vector} | {self.constant}]'

    def __hash__(self) -> int:
        return hash((self.type_name, self.vector, self.constant))
