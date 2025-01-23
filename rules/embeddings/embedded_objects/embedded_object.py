from abc import ABC

from decimal import Decimal, getcontext
from typing import Dict, Self

getcontext().prec = 2000
EPSILON = Decimal('0.1') ** 20


class EmbeddedObject(ABC):
    def to_dict(self) -> str: ...
    
    def from_dict(data: dict) -> Self: ...


Embedding = Dict[str, EmbeddedObject]
