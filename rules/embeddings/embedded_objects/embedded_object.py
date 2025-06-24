from abc import ABC, abstractmethod

from mpmath import mp, mpf
from typing import Self

mp.dps = 2000
EPSILON = mpf('0.1') ** 20
PI = mpf(mp.pi)


class EmbeddedObject(ABC):
    @abstractmethod
    def _type(self) -> str: ...

    @abstractmethod
    def is_equal(self, other: Self) -> bool: ...

    @abstractmethod
    def to_dict(self) -> str: ...

    @abstractmethod
    def from_dict(data: dict) -> Self: ...

    @abstractmethod
    def to_str(self, accuracy: int) -> str: ...
