from typing import Literal, Mapping, Optional, Self

from itertools import chain
from fractions import Fraction

from .abstract_iterable_vector import AbstractIterableVector
from .dense_vector import DenseVector


class SparseVector(AbstractIterableVector):
    """
    A vector where values are held in a dictionary.
    For each index in the vector, the dictionary at that index holds the value of the vector.
    If the dictionary does not have the index as a key, the value is 0.
    
    Useful in holding vectors with very few nonzero indices.
    """

    type_name: Literal['Sparse'] = 'Sparse'

    inner: dict[int, Fraction]

    _length: int

    def __init__(self, values: Mapping[int, int | Fraction], length: int):
        self.inner = {k: Fraction(v) for (k, v) in values.items() if v != 0}
        self._length = length

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, i: int) -> Fraction:
        return self.inner.get(i, Fraction(0))
    
    def __setitem__(self, i: int, value: Fraction):
        if value != 0:
            self.inner[i] = value

    def __mul__(self, x: Fraction) -> 'SparseVector':
        if x == 0:
            return SparseVector({}, self._length)
        return SparseVector({k: v * x for (k, v) in self.inner.items()}, len(self))

    def __truediv__(self, x: Fraction) -> 'SparseVector':
        return SparseVector({k: v / x for (k, v) in self.inner.items()}, len(self))

    def __add__(self, other: Self) -> 'SparseVector':
        return SparseVector(
            {k: self[k] + other[k] for k in chain(self.inner.keys(), other.inner.keys()) if self[k] + other[k] != 0},
            len(self),
        )

    def __sub__(self, other: Self) -> 'SparseVector':
        return SparseVector(
            {k: self[k] - other[k] for k in chain(self.inner.keys(), other.inner.keys()) if self[k] - other[k] != 0},
            len(self),
        )

    def __eq__(self, other: Self) -> bool:
        return all([self[i] == other[i] for i in chain(self.inner.keys(), other.inner.keys())])

    def first_nonzero_index(self) -> Optional[int]:
        return min(self.inner.keys()) if len(self.inner) > 0 else None

    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        return len([index for index in self.inner.keys() if max_index is None or index < max_index])

    def extend_length(self, amount: int):
        self._length += amount

    def permute(self, permutation: list[int]) -> 'SparseVector':
        return SparseVector({permutation[k]: v for (k, v) in self.inner.items()}, len(self))

    def clone(self) -> 'SparseVector':
        return SparseVector(self.inner, len(self))

    def to_dense_vector(self) -> DenseVector:
        return DenseVector(list(self))

    def inner_repr(self) -> str:
        rational_reprs = [f'{k}: {str(v)}' for (k, v) in self.inner.items()]
        return f'{{{', '.join(rational_reprs)}}}'

    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        return sum([abs(v) for (k, v) in self.inner.items() if max_index is None or k < max_index], Fraction(0))

    def __str__(self) -> str:
        return f'Sparse[{self.inner}]'

    def __hash__(self) -> int:
        signature = tuple(sorted((key, self.inner[key]) for key in self.inner.keys() if self.inner[key] != 0))
        return hash((self.type_name, signature))

    @classmethod
    def create_empty(cls: type[Self], length: int) -> Self:
        return cls({}, length)
    
    @classmethod
    def create_single(cls: type[Self], index: int, length: int) -> Self:
        return cls({index: Fraction(1)}, length)
