from dataclasses import dataclass

from ..terms.basic_function_term import BasicFunctionTerm

from .abstract_equation import AbstractEquation

@dataclass(kw_only=True)
class EquationPair[Function, Term, Predicate](AbstractEquation[Term, Term, Predicate]):
    left_term: BasicFunctionTerm[Function, Term]
    right_term: BasicFunctionTerm[Function, Term]
    second_predicate: Predicate | None

    def __str__(self) -> str:
        return f'({self.left_term} = {self.left}, {self.right_term} = {self.right})' if self.predicate is None else f'{self.predicate}'
