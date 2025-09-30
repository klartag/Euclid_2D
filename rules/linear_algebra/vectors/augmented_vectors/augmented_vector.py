from fractions import Fraction
from typing import Generic, Literal, Optional, Self, TypeVar

from ..abstract_vector import AbstractVector


V0 = TypeVar('V0', bound=AbstractVector)
V1 = TypeVar('V1', bound=AbstractVector)


class AugmentedVector(Generic[V0, V1], AbstractVector):
    type_name: Literal['Augmented'] = 'Augmented'

    vector0: V0
    vector1: V1

    def __init__(self, vector0: V0, vector1: V1):
        self.vector0 = vector0
        self.vector1 = vector1

    def clone(self) -> 'AugmentedVector[V0, V1]':
        return AugmentedVector(self.vector0.clone(), self.vector1.clone())

    def __len__(self) -> int:
        return len(self.vector)

    def __getitem__(self, i: int) -> Fraction:
        return self.vector[i]

    def __mul__(self, x: Fraction) -> 'AugmentedVector[V0, V1]':
        return AugmentedVector(self.vector0 * x, self.vector1 * x)

    def __truediv__(self, x: Fraction) -> 'AugmentedVector[V0, V1]':
        return AugmentedVector(self.vector0 / x, self.vector1 / x)

    def __add__(self, other: Self) -> 'AugmentedVector[V0, V1]':
        return AugmentedVector(self.vector0 + other.vector0, self.vector1 + other.vector1)

    def __sub__(self, other: Self) -> 'AugmentedVector[V0, V1]':
        return AugmentedVector(self.vector0 - other.vector0, self.vector1 - other.vector1)

    def __eq__(self, other: Self) -> bool:
        return self.vector == other.vector and self.vector1 == other.vector1

    def __bool__(self) -> str:
        return self.first_nonzero_index() is not None or not self.constant

    def first_nonzero_index(self) -> Optional[int]:
        return self.vector.first_nonzero_index()

    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        return self.vector.count_nonzero_indices(max_index)

    def extend_length(self, amount: int):
        self.vector.extend_length(amount)

    def permute(self, permutation: list[int]) -> 'AugmentedVector[V0, V1]':
        self.vector = self.vector.permute(permutation)

    def inner_repr(self) -> str:
        return f'{self.vector.inner_repr()}, {self.constant}'

    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        return self.vector.taxicab_norm(max_index)
    
    def __str__(self) -> str:
        return f'Augmented[{self.vector} | {self.constant}]'
