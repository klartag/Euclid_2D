from abc import ABC, abstractmethod

from mpmath import mp, mpf
from typing import Dict, Self

mp.dps = 2000
EPSILON = mpf('0.1') ** 20


class EmbeddedObject(ABC):
    @abstractmethod
    def to_dict(self) -> str: ...

    @abstractmethod
    def from_dict(data: dict) -> Self: ...


Embedding = Dict[str, EmbeddedObject]
