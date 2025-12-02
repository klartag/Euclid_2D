from dataclasses import dataclass
from typing import Optional, Self

from ..terms.basic_function_term import BasicFunctionTerm


@dataclass(frozen=True)
class GenericFunctionTerm[Function, Term]:
    function: Function
    parameters: tuple[Self | Term, ...]
    
    def try_to_basic_term(self) -> Optional[BasicFunctionTerm[Function, Term]]:
        parameters: list[Term] = []
        for parameter in self.parameters:
            if isinstance(parameter, GenericFunctionTerm):
                return None
            else:
                parameters.append(parameter)
        return BasicFunctionTerm(self.function, tuple(parameters))
        
    
    @staticmethod
    def from_basic_term(term: BasicFunctionTerm[Function, Term]) -> 'GenericFunctionTerm[Function, Term]':
        return GenericFunctionTerm(term.function, term.parameters)

    def __eq__(self, other: Self):
        return isinstance(other, GenericFunctionTerm) and \
            self.function == other.function and \
            len(self.parameters) == len(other.parameters) and \
            all([p == q for (p, q) in zip(self.parameters, other.parameters)])
            
    def __hash__(self) -> int:
        return hash((self.function, tuple(self.parameters)))

    def __str__(self) -> str:
        return f'{self.function}{self.parameters}'
