from typing import Never

from ...expression_parse_utils import split_args

from .abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker
from .terms.generic_function_term import GenericFunctionTerm


class TextCongruenceClosureTracker(AbstractCongruenceClosureTracker[str, Never, str, str]):    
    def deconstruct_predicate(self, predicate: str) -> tuple[str, str]:
        if predicate.count('=') != 1:
            raise ValueError('Predicate must contain precisely one equals ("=") symbol.')
        components = predicate.split('=')
        left, right = components[0].strip(), components[1].strip()
        return (left, right)
        

    def deconstruct(self, value: str) -> str | GenericFunctionTerm[str, str]:
        assert value.count('(') == value.count(')')
        if '(' not in value:
            return value
        assert value.endswith(')')
        position = value.index('(')
        function = value[:position]
        unparsed_parameters = split_args(value[position + 1:-1])
        assert unparsed_parameters is not None
        parsed_parameters = [self.deconstruct(parameter) for parameter in unparsed_parameters]
        return GenericFunctionTerm(function, tuple(parsed_parameters))

    def reconstruct_function(self, function: str, parameters: list[str]) -> str:
        return f'{function}{tuple(parameters)}'
