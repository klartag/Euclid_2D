from fractions import Fraction
from typing import Literal, Optional, Self, Union

from .abstract_iterable_vector import AbstractIterableVector
from .dense_vector import DenseVector
from .sparse_vector import SparseVector


DENSE_THRESHOLD = 1 / 4
SPARSE_THRESHOLD = 1 / 20


class DynamicVector(AbstractIterableVector):
    type_name: Literal['Dynamic'] = 'Dynamic'

    inner: Union[DenseVector, SparseVector]

    def __init__(self, vector: Union[DenseVector, SparseVector]):
        self.inner = vector

    def normalize(self) -> 'DynamicVector':
        vector = self.inner.clone()
        if vector.type_name == 'Sparse':
            vector = SparseVector({k: v for (k, v) in vector.inner.items() if v != 0}, len(vector))
        match vector.type_name:
            case 'Sparse':
                if len(vector.inner) > DENSE_THRESHOLD * len(vector):
                    vector = DenseVector(list(iter(vector)))
            case 'Dense':
                if len(vector) - vector.inner.count(Fraction(0)) < SPARSE_THRESHOLD * len(vector):
                    vector = SparseVector({i: vector[i] for i in range(len(vector)) if vector[i] != 0}, len(vector))
        return DynamicVector(vector)

    def clone(self) -> 'DynamicVector':
        return DynamicVector(self.inner.clone())

    def __len__(self) -> int:
        return len(self.inner)

    def __getitem__(self, i: int) -> Fraction:
        return self.inner[i]
    
    def __setitem__(self, i: int, value: Fraction):
        self.inner[i] = value

    def __mul__(self, x: Fraction) -> 'DynamicVector':
        return DynamicVector(self.inner * x)

    def __truediv__(self, x: Fraction) -> 'DynamicVector':
        return DynamicVector(self.inner / x)

    def __add__(self, other: Self) -> 'DynamicVector':        
        if self.inner.type_name == 'Dense' and other.inner.type_name == 'Dense':
            return DynamicVector(self.inner + other.inner).normalize()
        if self.inner.type_name == 'Sparse' and other.inner.type_name == 'Sparse':
            return DynamicVector(self.inner + other.inner).normalize()
        inner0 = self.inner if self.inner.type_name == 'Dense' else self.inner.to_dense_vector()
        inner1 = other.inner if other.inner.type_name == 'Dense' else other.inner.to_dense_vector()
        return DynamicVector(inner0 + inner1).normalize()

    def __sub__(self, other: Self) -> 'DynamicVector':
        if self.inner.type_name == 'Dense' and other.inner.type_name == 'Dense':
            return DynamicVector(self.inner - other.inner).normalize()
        if self.inner.type_name == 'Sparse' and other.inner.type_name == 'Sparse':
            return DynamicVector(self.inner - other.inner).normalize()
        inner0 = self.inner if self.inner.type_name == 'Dense' else self.inner.to_dense_vector()
        inner1 = other.inner if other.inner.type_name == 'Dense' else other.inner.to_dense_vector()
        return DynamicVector(inner0 - inner1).normalize()

    def __eq__(self, other: Self) -> bool:
        if self.inner.type_name == 'Dense' and other.inner.type_name == 'Dense':
            return self.inner == other.inner
        if self.inner.type_name == 'Sparse' and other.inner.type_name == 'Sparse':
            return self.inner == other.inner
        inner0 = self.inner if self.inner.type_name == 'Dense' else self.inner.to_dense_vector()
        inner1 = other.inner if other.inner.type_name == 'Dense' else other.inner.to_dense_vector()
        return inner0 == inner1

    def first_nonzero_index(self) -> Optional[int]:
        return self.inner.first_nonzero_index()

    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        return self.inner.count_nonzero_indices(max_index)

    def extend_length(self, amount: int):
        self.inner.extend_length(amount)
        self.normalize()

    def permute(self, permutation: list[int]) -> 'DynamicVector':
        return DynamicVector(self.inner.permute(permutation))

    def inner_repr(self) -> str:
        return self.inner.inner_repr()

    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        return self.inner.taxicab_norm(max_index)

    def __hash__(self) -> int:
        return hash((self.type_name, self.inner))

    @classmethod
    def create_empty(cls: type[Self], length: int) -> Self:
        return cls(SparseVector.create_empty(length))
    
    @classmethod
    def create_single(cls: type[Self], index: int, length: int) -> Self:
        return cls(SparseVector.create_single(index, length))
