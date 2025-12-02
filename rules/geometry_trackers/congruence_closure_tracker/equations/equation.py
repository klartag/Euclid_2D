from dataclasses import dataclass

from .abstract_equation import AbstractEquation

@dataclass
class Equation[TermLeft, TermRight, Predicate](AbstractEquation[TermLeft, TermRight, Predicate]):
    def __str__(self) -> str:
        return f'{self.left} = {self.right}' if self.predicate is None else f'{self.predicate}'
