from typing import Literal, Optional, Self, Union

from .abstract_vector import AbstractVector, Rational
from .dense_vector import DenseVector
from .sparse_vector import SparseVector


DENSE_THRESHOLD = 1 / 4
SPARSE_THRESHOLD = 1 / 20


class DynamicVector(AbstractVector):
    type_name: Literal['Dynamic'] = 'Dynamic'

    inner: Union[DenseVector, SparseVector]

    def __init__(self, vector: Union[DenseVector, SparseVector]):
        self.inner = vector

    def normalize(self) -> Self:
        vector = self.inner.clone()
        if vector.type_name == 'Sparse':
            vector = SparseVector({k: v for (k, v) in vector.inner.items() if v != 0}, vector.length)
        match vector.type_name:
            case 'Sparse':
                if len(vector.inner) > DENSE_THRESHOLD * len(vector):
                    vector = DenseVector(list(iter(vector)))
            case 'Dense':
                if len(vector) - vector.inner.count(0) < SPARSE_THRESHOLD * len(vector):
                    vector = SparseVector({i: vector[i] for i in range(len(vector)) if vector[i] != 0}, len(vector))
        return DynamicVector(vector)

    def clone(self) -> Self:
        return DynamicVector(self.inner.clone())

    def __len__(self) -> int:
        return len(self.inner)

    def __getitem__(self, i: int) -> Rational:
        return self.inner[i]

    def __mul__(self, x: Rational) -> Self:
        return DynamicVector(self.inner * x)

    def __add__(self, other: Self) -> Self:
        if self.inner.type_name == other.inner.type_name:
            return DynamicVector(self.inner + other.inner).normalize()
        inner0 = self.inner if self.inner.type_name == 'Dense' else self.inner.to_dense_vector()
        inner1 = other.inner if other.inner.type_name == 'Dense' else other.inner.to_dense_vector()
        return DynamicVector(inner0 + inner1).normalize()

    def __sub__(self, other: Self) -> Self:
        if self.inner.type_name == other.inner.type_name:
            return DynamicVector(self.inner - other.inner).normalize()
        inner0 = self.inner if self.inner.type_name == 'Dense' else self.inner.to_dense_vector()
        inner1 = other.inner if other.inner.type_name == 'Dense' else other.inner.to_dense_vector()
        return DynamicVector(inner0 - inner1).normalize()

    def __eq__(self, other: Self) -> bool:
        if self.inner.type_name == other.inner.type_name:
            return self.inner == other.inner
        inner0 = self.inner if self.inner.type_name == 'Dense' else self.inner.to_dense_vector()
        inner1 = other.inner if other.inner.type_name == 'Dense' else other.inner.to_dense_vector()
        return inner0 == inner1

    def first_nonzero_index(self) -> Optional[int]:
        return self.inner.first_nonzero_index()

    def extend_length(self, amount: int):
        self.inner.extend_length(amount)
        self.normalize()

    def permute(self, permutation: list[int]) -> Self:
        self.inner = self.inner.permute(permutation)

    def inner_repr(self) -> str:
        return self.inner.inner_repr()
