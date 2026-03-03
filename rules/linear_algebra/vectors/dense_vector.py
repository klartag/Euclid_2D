from fractions import Fraction
from typing import Literal, Optional, Self, Sequence

from .abstract_iterable_vector import AbstractIterableVector


class DenseVector(AbstractIterableVector):
    """A vector whose values are held in a list."""

    type_name: Literal['Dense'] = 'Dense'

    inner: list[Fraction]

    def __init__(self, values: Sequence[int | Fraction]):
        self.inner = [Fraction(x) for x in values]

    def __len__(self) -> int:
        return len(self.inner)

    def __getitem__(self, i: int) -> Fraction:
        return self.inner[i]
    
    def __setitem__(self, i: int, value: Fraction):
        self.inner[i] = value

    def __mul__(self, x: Fraction) -> 'DenseVector':
        return DenseVector([x * f for f in self.inner])

    def __truediv__(self, x: Fraction) -> 'DenseVector':
        return DenseVector([f / x for f in self.inner])

    def __add__(self, other: Self) -> 'DenseVector':
        return DenseVector([self[i] + other[i] for i in range(len(self))])

    def __sub__(self, other: Self) -> 'DenseVector':
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
        self.inner.extend([Fraction(0) for _ in range(amount)])

    def permute(self, permutation: list[int]) -> 'DenseVector':
        return DenseVector([self.inner[permutation[i]] for i in range(len(self))])

    def clone(self) -> 'DenseVector':
        return DenseVector(self.inner)

    def inner_repr(self) -> str:
        rational_reprs = [str(x) for x in self.inner]
        return f'[{', '.join(rational_reprs)}]'

    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        return sum([abs(x) for x in self.inner[:max_index]], Fraction(0))

    def __hash__(self) -> int:
        return hash((self.type_name, tuple(self.inner)))
    
    @classmethod
    def create_empty(cls: type[Self], length: int) -> Self:
        return cls([Fraction(0)] * length)

    @classmethod
    def create_single(cls: type[Self], index: int, length: int) -> Self:
        values = [Fraction(0)] * length
        values[index] = Fraction(1)
        return cls(values)
