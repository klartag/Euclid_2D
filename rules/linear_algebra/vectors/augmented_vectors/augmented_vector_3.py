from fractions import Fraction
from typing import Generic, Literal, Self, TypeVar

from ..abstract_vector import AbstractVector


V0 = TypeVar('V0', bound=AbstractVector)
V1 = TypeVar('V1', bound=AbstractVector)
V2 = TypeVar('V2', bound=AbstractVector)


class AugmentedVector3(Generic[V0, V1, V2], AbstractVector):
    type_name: Literal['Augmented3'] = 'Augmented3'

    vector0: V0
    vector1: V1
    vector2: V2

    def __init__(self, vector0: V0, vector1: V1, vector2: V2):
        self.vector0 = vector0
        self.vector1 = vector1
        self.vector2 = vector2

    def __mul__(self, x: Fraction) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.vector0 * x, self.vector1 * x, self.vector2 * x)

    def __truediv__(self, x: Fraction) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.vector0 / x, self.vector1 / x, self.vector2 / x)

    def __add__(self, other: Self) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.vector0 + other.vector0, self.vector1 + other.vector1, self.vector2 + other.vector2)

    def __sub__(self, other: Self) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.vector0 - other.vector0, self.vector1 - other.vector1, self.vector2 - other.vector2)

    def __eq__(self, other: Self) -> bool:
        return self.vector0 == other.vector0 and self.vector1 == other.vector1 and self.vector2 == other.vector2

    def __bool__(self) -> bool:
        return bool(self.vector0) or bool(self.vector1) or bool(self.vector2)

    def inner_repr(self) -> str:
        return f'{self.vector0.inner_repr()} | {self.vector1.inner_repr()} | {self.vector2.inner_repr()}'

    def clone(self) -> 'AugmentedVector3[V0, V1, V2]':
        return AugmentedVector3(self.vector0.clone(), self.vector1.clone(), self.vector2.clone())
