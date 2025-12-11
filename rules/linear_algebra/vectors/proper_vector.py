from typing import Iterator, Optional, Self

from abc import abstractmethod
from .abstract_vector import AbstractVector

from fractions import Fraction


class ProperVector(AbstractVector):
    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __getitem__(self, i: int) -> Fraction: ...

    @abstractmethod
    def extend_length(self, amount: int): ...

    @abstractmethod
    def permute(self, permutation: list[int]) -> Self: ...

    def __iter__(self) -> Iterator[Fraction]:
        return (self[i] for i in range(len(self)))

    def __bool__(self) -> bool:
        return self.first_nonzero_index() is not None

    @abstractmethod
    def first_nonzero_index(self) -> Optional[int]: ...

    @abstractmethod
    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int: ...
    
    @classmethod
    @abstractmethod
    def create_empty(cls: type[Self], length: int) -> Self: ...
    
    @classmethod
    @abstractmethod
    def create_single(cls: type[Self], index: int, length: int) -> Self: ...
