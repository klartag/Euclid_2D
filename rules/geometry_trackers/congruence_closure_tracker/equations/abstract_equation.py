from abc import ABC
from dataclasses import dataclass

@dataclass
class AbstractEquation[S, T, P](ABC):
    left: S
    right: T
    predicate: P | None = None
