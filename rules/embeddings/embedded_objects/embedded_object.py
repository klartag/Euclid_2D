from abc import ABC, abstractmethod

from mpmath import mp, mpf
from typing import Self

mp.dps = 2000
EPSILON = mpf('0.1') ** 20
PI = mpf(mp.pi)


class EmbeddedObject(ABC):
    @abstractmethod
    def _type(self) -> str:
        """
        The `GeoType` this object represents.
        """
        ...

    @abstractmethod
    def is_equal(self, other: Self) -> bool:
        """
        Returns whether two objects are equal.
        (An error of `EPSILON` is allowed.)
        """
        ...

    @abstractmethod
    def to_dict(self) -> dict:
        """
        TODO: Document
        """
        ...

    @abstractmethod
    def from_dict(data: dict) -> Self:
        """
        TODO: Document
        """
        ...

    @abstractmethod
    def to_str(self, accuracy: int) -> str:
        """
        TODO: Document
        """
        ...
