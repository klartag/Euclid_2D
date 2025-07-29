from abc import ABC, abstractmethod
from typing import Iterator, Optional, Self

from fractions import Fraction


class AbstractVector(ABC):
    @property
    @abstractmethod
    def type_name(self) -> str: ...

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __getitem__(self, i: int) -> Fraction: ...

    @abstractmethod
    def __mul__(self, x: Fraction) -> Self: ...

    @abstractmethod
    def __truediv__(self, x: Fraction) -> Self: ...

    @abstractmethod
    def __add__(self, other: Self) -> Self: ...

    @abstractmethod
    def __sub__(self, other: Self) -> Self: ...

    @abstractmethod
    def extend_length(self, amount: int): ...

    @abstractmethod
    def clone(self) -> Self: ...

    @abstractmethod
    def permute(self, permutation: list[int]) -> Self: ...

    @abstractmethod
    def __eq__(self, other: Self) -> bool: ...

    def __iter__(self) -> Iterator[Fraction]:
        return (self[i] for i in range(len(self)))

    @abstractmethod
    def first_nonzero_index(self) -> Optional[int]: ...

    @abstractmethod
    def count_nonzero_indices(self, max_index: Optional[int] = None) -> int: ...

    @abstractmethod
    def __str__(self) -> str: ...

    def __bool__(self) -> str:
        return self.first_nonzero_index() is not None

    @abstractmethod
    def inner_repr(self) -> str: ...

    def __str__(self) -> str:
        return f'{self.type_name}({self.inner_repr()})'

    @abstractmethod
    def taxicab_norm(self, max_index: Optional[int] = None) -> Fraction: ...
