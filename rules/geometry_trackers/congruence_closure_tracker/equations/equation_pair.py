from dataclasses import dataclass

from ..terms.basic_function_term import BasicFunctionTerm

from .abstract_equation import AbstractEquation

@dataclass(kw_only=True)
class EquationPair[T, P](AbstractEquation[T, T, P]):
    left_term: BasicFunctionTerm[T]
    right_term: BasicFunctionTerm[T]
    second_predicate: P | None

    def __str__(self) -> str:
        return f'({self.left_term} = {self.left}, {self.right_term} = {self.right})' if self.predicate is None else f'{self.predicate}'
