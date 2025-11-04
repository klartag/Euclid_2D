from dataclasses import dataclass
from typing import Optional, Self, Sequence

from ..terms.basic_function_term import BasicFunctionTerm


@dataclass(frozen=True)
class GenericFunctionTerm[T]:
    function: str
    parameters: Sequence[Self | T]
    
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

    def __eq__(self, other: Self):
        return self.function == other.function and \
            len(self.parameters) == len(other.parameters) and \
            all([p == q for (p, q) in zip(self.parameters, other.parameters)])