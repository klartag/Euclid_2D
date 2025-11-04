from dataclasses import dataclass

from ..terms.basic_function_term import BasicFunctionTerm

from .abstract_equation import AbstractEquation

@dataclass
class EquationPair[T](AbstractEquation[T, T]):
    left_term: BasicFunctionTerm[T]
    right_term: BasicFunctionTerm[T]
