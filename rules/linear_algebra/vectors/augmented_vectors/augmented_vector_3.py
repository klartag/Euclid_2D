from fractions import Fraction
from typing import Generic, Literal, Self, TypeVar

from ..abstract_vector import AbstractVector


V0 = TypeVar('V0', bound=AbstractVector)
V1 = TypeVar('V1', bound=AbstractVector)
V2 = TypeVar('V2', bound=AbstractVector)


class AugmentedVector3(Generic[V0, V1, V2], AbstractVector):
    """A vector that holds a tuple of three vector types."""

    type_name: Literal['Augmented3'] = 'Augmented3'

    inner0: V0
    inner1: V1
    inner2: V2

    def __init__(self, vector0: V0, vector1: V1, vector2: V2):
        self.inner0 = vector0
        self.inner1 = vector1
        self.inner2 = vector2

    def __mul__(self, x: Fraction) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.inner0 * x, self.inner1 * x, self.inner2 * x)

    def __truediv__(self, x: Fraction) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.inner0 / x, self.inner1 / x, self.inner2 / x)

    def __add__(self, other: Self) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.inner0 + other.inner0, self.inner1 + other.inner1, self.inner2 + other.inner2)

    def __sub__(self, other: Self) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.inner0 - other.inner0, self.inner1 - other.inner1, self.inner2 - other.inner2)

    def __eq__(self, other: Self) -> bool:
        return self.inner0 == other.inner0 and self.inner1 == other.inner1 and self.inner2 == other.inner2

    def __bool__(self) -> bool:
        return bool(self.inner0) or bool(self.inner1) or bool(self.inner2)

    def inner_repr(self) -> str:
        return f'{self.inner0.inner_repr()} | {self.inner1.inner_repr()} | {self.inner2.inner_repr()}'

    def clone(self) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.inner0.clone(), self.inner1.clone(), self.inner2.clone())
    
    def __str__(self) -> str:
        return f'Augmented[{self.inner0} | {self.inner1} | {self.inner2}]'

    def __hash__(self) -> int:
        return hash((self.type_name, self.inner0, self.inner1, self.inner2))
