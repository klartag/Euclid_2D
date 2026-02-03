from abc import abstractmethod
from typing import Iterator, Optional, Self

from fractions import Fraction

from .abstract_vector import AbstractVector

class AbstractIterableVector(AbstractVector):
    # TODO: Document

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __getitem__(self, i: int) -> Fraction: ...
    
    @abstractmethod
    def __setitem__(self, i: int, value: Fraction): ...

    @abstractmethod
    def extend_length(self, amount: int):
        # TODO: Document
        ...

    @abstractmethod
    def permute(self, permutation: list[int]) -> Self:
        # TODO: Document
        ...

    def __iter__(self) -> Iterator[Fraction]:
        return (self[i] for i in range(len(self)))

    @abstractmethod
    def first_nonzero_index(self) -> Optional[int]:
        # TODO: Document
        ...

    @abstractmethod
    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int:
        # TODO: Document
        ...

    def __bool__(self) -> bool:
        return self.first_nonzero_index() is not None

    @abstractmethod
    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction:
        # TODO: Document
        ...
    
    @classmethod
    @abstractmethod
    def create_empty(cls: type[Self], length: int) -> Self:
        # TODO: Document
        ...
    
    @classmethod
    @abstractmethod
    def create_single(cls: type[Self], index: int, length: int) -> Self:
        # TODO: Document
        ...
