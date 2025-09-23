from fractions import Fraction
from typing import Literal, Optional, Self

from .abstract_vector import AbstractVector


class DenseVector(AbstractVector):
    type_name: Literal['Dense'] = 'Dense'

    inner: list[Fraction]

    def __init__(self, values: list[int | Fraction]):
        self.inner = [Fraction(x) for x in values]

    def __len__(self) -> int:
        return len(self.inner)

    def __getitem__(self, i: int) -> Fraction:
        return self.inner[i]

    def __mul__(self, x: Fraction) -> Self:
        return DenseVector([x * f for f in self.inner])

    def __truediv__(self, x: Fraction) -> Self:
        return DenseVector([f / x for f in self.inner])

    def __add__(self, other: Self) -> Self:
        return DenseVector([self[i] + other[i] for i in range(len(self))])

    def __sub__(self, other: Self) -> Self:
        return DenseVector([self[i] - other[i] for i in range(len(self))])

    def __eq__(self, other: Self) -> bool:
        return all([self[i] == other[i] for i in range(len(self))])

    def first_nonzero_index(self) -> Optional[int]:
        for i in range(len(self)):
            if self[i] != 0:
                return i
        return None

    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        return sum([1 for value in self.inner[:max_index] if value != 0])

    def extend_length(self, amount: int):
        self.inner.extend([0 for _ in range(amount)])

    def permute(self, permutation: list[int]) -> Self:
        return DenseVector([self.inner[permutation[i]] for i in range(len(Self))])

    def clone(self) -> Self:
        return DenseVector(self.inner)

    def inner_repr(self) -> str:
        rational_reprs = [str(x) for x in self.inner]
        return f'[{', '.join(rational_reprs)}]'

    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        return sum([abs(x) for x in self.inner[:max_index]])
