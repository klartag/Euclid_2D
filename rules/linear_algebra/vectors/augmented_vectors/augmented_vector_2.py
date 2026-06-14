from fractions import Fraction
from typing import Generic, Literal, Self, TypeVar

from ..abstract_vector import AbstractVector


V0 = TypeVar('V0', bound=AbstractVector)
V1 = TypeVar('V1', bound=AbstractVector)


class AugmentedVector2(Generic[V0, V1], AbstractVector):
    """A vector that holds a tuple of two vector types."""

    type_name: Literal['Augmented2'] = 'Augmented2'

    inner0: V0
    inner1: V1

    def __init__(self, vector0: V0, vector1: V1):
        self.inner0 = vector0
        self.inner1 = vector1

    def __mul__(self, x: Fraction) -> 'AugmentedVector2[V0, V1]':
        return AugmentedVector2(self.inner0 * x, self.inner1 * x)

    def __truediv__(self, x: Fraction) -> 'AugmentedVector2[V0, V1]':
        return AugmentedVector2(self.inner0 / x, self.inner1 / x)

    def __add__(self, other: Self) -> 'AugmentedVector2[V0, V1]':
        return AugmentedVector2(self.inner0 + other.inner0, self.inner1 + other.inner1)

    def __sub__(self, other: Self) -> 'AugmentedVector2[V0, V1]':
        return AugmentedVector2(self.inner0 - other.inner0, self.inner1 - other.inner1)

    def __eq__(self, other: Self) -> bool:
        return self.inner0 == other.inner0 and self.inner1 == other.inner1

    def __bool__(self) -> bool:
        return bool(self.inner0) or bool(self.inner1)

    def inner_repr(self) -> str:
        return f'{self.inner0.inner_repr()} | {self.inner1.inner_repr()}'

    def clone(self) -> 'AugmentedVector2[V0, V1]':
        return AugmentedVector2(self.inner0.clone(), self.inner1.clone())

    def __str__(self) -> str:
        return f'Augmented[{self.inner0} | {self.inner1}]'

    def __hash__(self) -> int:
        return hash((self.type_name, self.inner0, self.inner1))
