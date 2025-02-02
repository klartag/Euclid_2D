from abc import ABC, abstractmethod

from decimal import Decimal, getcontext
from typing import Dict, Self

getcontext().prec = 2000
EPSILON = Decimal('0.1') ** 20


class EmbeddedObject(ABC):
    @abstractmethod
    def to_dict(self) -> str: ...

    @abstractmethod
    def from_dict(data: dict) -> Self: ...


Embedding = Dict[str, EmbeddedObject]
