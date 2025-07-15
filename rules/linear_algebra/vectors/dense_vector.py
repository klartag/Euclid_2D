from fractions import Fraction
from typing import Literal, Optional, Self

from .abstract_vector import AbstractVector, Rational


class DenseVector(AbstractVector):
    type_name: Literal['Dense'] = 'Dense'

    inner: list[Rational]

    def __init__(self, values: list[Rational]):
        self.inner = list(values)

    def __len__(self) -> int:
        return len(self.inner)

    def __getitem__(self, i: int) -> Rational:
        return self.inner[i]

    def __mul__(self, x: Rational) -> Self:
        return DenseVector([x * f for f in self.inner])

    def __truediv__(self, x: Rational) -> Self:
        return DenseVector([Fraction(1, x) * f for f in self.inner])

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

    def extend_length(self, amount: int):
        self.inner.extend([0 for _ in range(amount)])

    def permute(self, permutation: list[int]) -> Self:
        return DenseVector([self.inner[permutation[i]] for i in range(len(Self))])

    def clone(self) -> Self:
        return DenseVector(self.inner)

    def inner_repr(self) -> str:
        rational_reprs = [str(x) for x in self.inner]
        return f'[{', '.join(rational_reprs)}]'
