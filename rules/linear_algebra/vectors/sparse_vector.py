from typing import Literal, Optional, Self

from itertools import chain
from fractions import Fraction

from .abstract_vector import AbstractVector, Rational
from .dense_vector import DenseVector


class SparseVector(AbstractVector):
    type_name: Literal['Sparse'] = 'Sparse'

    inner: dict[int, Rational]

    _length: int

    def __init__(self, values: dict[int, Rational], length: int):
        self.inner = {k: v for (k, v) in values.items() if v != 0}
        self._length = length

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, i: int) -> Rational:
        return self.inner.get(i, 0)

    def __mul__(self, x: Rational) -> Self:
        if x == 0:
            return SparseVector({}, self._length)
        return SparseVector({k: v * x for (k, v) in self.inner.items()}, len(self))

    def __truediv__(self, x: Rational) -> Self:
        return SparseVector({k: v * Fraction(1, x) for (k, v) in self.inner.items()}, len(self))

    def __add__(self, other: Self) -> Self:
        return SparseVector(
            {k: self[k] + other[k] for k in chain(self.inner.keys(), other.inner.keys()) if self[k] + other[k] != 0},
            len(self),
        )

    def __sub__(self, other: Self) -> Self:
        return SparseVector(
            {k: self[k] - other[k] for k in chain(self.inner.keys(), other.inner.keys()) if self[k] - other[k] != 0},
            len(self),
        )

    def __eq__(self, other: Self) -> bool:
        return all([self[i] == other[i] for i in chain(self.inner.keys(), other.inner.keys())])

    def first_nonzero_index(self) -> Optional[int]:
        return min(self.inner.keys()) if len(self.inner) > 0 else None

    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        return len([index for index in self.inner.keys() if index < max_index])

    def extend_length(self, amount: int):
        self._length += amount

    def permute(self, permutation: list[int]) -> Self:
        return SparseVector({permutation[k]: v for (k, v) in self.inner.items()}, len(self))

    def clone(self) -> Self:
        return SparseVector(self.inner, len(self))

    def to_dense_vector(self) -> DenseVector:
        return DenseVector(iter(self))

    def inner_repr(self) -> str:
        rational_reprs = [f'{k}: {str(v)}' for (k, v) in self.inner.items()]
        return f'{{{', '.join(rational_reprs)}}}'

    def taxicab_norm(self, max_index: Optional[int] = None) -> Rational:
        return sum([abs(v) for (k, v) in self.inner.items() if max_index is None or k < max_index])
