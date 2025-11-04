from abc import ABC
from dataclasses import dataclass

@dataclass
class AbstractEquation[S, T](ABC):
    left: S
    right: T
