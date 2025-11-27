from dataclasses import dataclass

from ..terms.basic_function_term import BasicFunctionTerm

from .abstract_equation import AbstractEquation

@dataclass(kw_only=True)
class EquationPair[T, L](AbstractEquation[T, T, L]):
    left_term: BasicFunctionTerm[T]
    right_term: BasicFunctionTerm[T]

    def __str__(self) -> str:
        return f'({self.left_term} = {self.left}, {self.right_term} = {self.right})' if self.label is None else f'{self.label}'
