from abc import ABC
from dataclasses import dataclass

@dataclass(kw_only=True)
class AbstractEquation[TermLeft, TermRight, Predicate](ABC):
    left: TermLeft
    right: TermRight
    predicate: Predicate | None
