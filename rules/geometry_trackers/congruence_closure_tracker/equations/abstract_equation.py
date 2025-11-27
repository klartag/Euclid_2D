from abc import ABC
from dataclasses import dataclass

@dataclass
class AbstractEquation[S, T, L](ABC):
    left: S
    right: T
    label: L | None = None
