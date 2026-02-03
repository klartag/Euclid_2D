from abc import ABC, abstractmethod
from typing import Optional, Self

from fractions import Fraction


class AbstractVector(ABC):
    # TODO: Document

    @property
    @abstractmethod
    def type_name(self) -> str:
        # TODO: Document
        ...

    @abstractmethod
    def __mul__(self, x: Fraction) -> Self:
        # TODO: Document
        ...

    @abstractmethod
    def __truediv__(self, x: Fraction) -> Self:
        # TODO: Document
        ...

    @abstractmethod
    def __add__(self, other: Self) -> Self: ...

    @abstractmethod
    def __sub__(self, other: Self) -> Self: ...

    @abstractmethod
    def clone(self) -> Self: ...

    @abstractmethod
    def __eq__(self, other: Self) -> bool: ...

    @abstractmethod
    def inner_repr(self) -> str:
        # TODO: Document
        ...

    def __str__(self) -> str:
        return f'{self.type_name}({self.inner_repr()})'

    @abstractmethod
    def __hash__(self) -> int: ...
