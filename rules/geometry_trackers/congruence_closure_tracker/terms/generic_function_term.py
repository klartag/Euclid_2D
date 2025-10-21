from dataclasses import dataclass
from typing import Optional, Sequence

from ..terms.basic_function_term import BasicFunctionTerm


@dataclass
class GenericFunctionTerm[T]:
    function: str
    parameters: Sequence['GenericFunctionTerm[T]' | T]
    
    def try_to_basic_term(self) -> Optional[BasicFunctionTerm[T]]:
        parameters: list[T] = []
        for parameter in self.parameters:
            if isinstance(parameter, GenericFunctionTerm):
                return None
            else:
                parameters.append(parameter)
        return BasicFunctionTerm(self.function, parameters)
        
    
    @staticmethod
    def from_basic_term(term: BasicFunctionTerm[T]) -> 'GenericFunctionTerm[T]':
        return GenericFunctionTerm(term.function, term.parameters)
