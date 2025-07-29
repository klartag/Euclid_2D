from fractions import Fraction
from typing import Generic, Literal, Optional, Self, TypeVar

from .abstract_vector import AbstractVector


DENSE_THRESHOLD = 1 / 4
SPARSE_THRESHOLD = 1 / 20

V = TypeVar('V', bound=AbstractVector)
C = TypeVar('C')


class AugmentedVector(Generic[V, C], AbstractVector):
    type_name: Literal['Augmented'] = 'Augmented'

    vector: V
    constant: C

    def __init__(self, vector: V, constant: C):
        self.vector = vector
        self.constant = constant

    def clone(self) -> Self:
        return AugmentedVector(self.vector.clone(), self.constant)

    def __len__(self) -> int:
        return len(self.vector)

    def __getitem__(self, i: int) -> Fraction:
        return self.vector[i]

    def __mul__(self, x: Fraction) -> Self:
        return AugmentedVector(self.vector * x, self.constant * x)

    def __truediv__(self, x: Fraction) -> Self:
        return AugmentedVector(self.vector / x, self.constant / x)

    def __add__(self, other: Self) -> Self:
        return AugmentedVector(self.vector + other.vector, self.constant + other.constant)

    def __sub__(self, other: Self) -> Self:
        return AugmentedVector(self.vector - other.vector, self.constant - other.constant)

    def __eq__(self, other: Self) -> bool:
        return self.vector == other.vector and self.constant == other.constant

    def __bool__(self) -> str:
        return self.first_nonzero_index() is not None or not self.constant

    def first_nonzero_index(self) -> Optional[int]:
        return self.vector.first_nonzero_index()

    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        return self.vector.count_nonzero_indices(max_index)

    def extend_length(self, amount: int):
        self.vector.extend_length(amount)

    def permute(self, permutation: list[int]) -> Self:
        self.vector = self.vector.permute(permutation)

    def inner_repr(self) -> str:
        return f'{self.vector.inner_repr()}, {self.constant}'

    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        return self.vector.taxicab_norm(max_index)
