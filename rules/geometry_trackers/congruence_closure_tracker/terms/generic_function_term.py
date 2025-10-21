from dataclasses import dataclass
from typing import Optional, Sequence

from ..terms.basic_function_term import BasicFunctionTerm

from .abstract_term import AbstractTerm
from .constant_term import ConstantTerm


@dataclass
class GenericFunctionTerm[T](AbstractTerm[T]):
    function: str
    parameters: Sequence['GenericFunctionTerm[T]' | ConstantTerm[T]]
    
    def try_to_basic_term(self) -> Optional[BasicFunctionTerm[T]]:
        parameters: list[ConstantTerm[T]] = []
        for parameter in self.parameters:
            if isinstance(parameter, GenericFunctionTerm):
                return None
            else:
                parameters.append(parameter)
        return BasicFunctionTerm(self.function, parameters)
        
    
    @staticmethod
    def from_basic_term(term: BasicFunctionTerm[T]) -> 'GenericFunctionTerm[T]':
        return GenericFunctionTerm(term.function, term.parameters)
