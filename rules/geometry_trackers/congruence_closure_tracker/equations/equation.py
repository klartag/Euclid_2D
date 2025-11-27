from dataclasses import dataclass

from .abstract_equation import AbstractEquation

@dataclass
class Equation[S, T, L](AbstractEquation[S, T, L]):
    def __str__(self) -> str:
        return f'{self.left} = {self.right}' if self.label is None else f'{self.label}'
