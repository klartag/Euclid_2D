from typing import cast
from ...indexed_set import IndexedSet

from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm


Token = int
GenericToken = Token | GenericFunctionTerm[Token]


class CongruenceClosureTracker[T]:
    tokens: IndexedSet[T | BasicFunctionTerm[Token]]
    pending: list[tuple[Token, Token] | tuple[BasicFunctionTerm[Token], Token, BasicFunctionTerm[Token], Token]]
    representatives: dict[Token, Token]
    class_lists: dict[Token, list[Token]]
    use_lists: dict[Token, list[tuple[BasicFunctionTerm[Token], Token]]]
    lookup_table: dict[tuple[Token, ...], tuple[BasicFunctionTerm[Token], Token]]
    proof_forest: list[tuple[Token, Token, object]] # Replace this with a proper data structure later.

    def __init__(self):
        self.tokens = IndexedSet()
        self.pending = []
        self.representatives = {}
        self.class_lists = {}
        self.use_lists = {}
        self.lookup_table = {}
        self.proof_forest = []

    def merge(self, left: GenericToken, right: GenericToken):
        if isinstance(left, Token):
            if isinstance(right, Token):
                self.pending.append((left, right))
                self.propogate()
            else:
                self.merge_complex_equation(right, left)
        else:
            self.merge_complex_equation(left, right)
    
    def merge_complex_equation(self, left: GenericFunctionTerm[Token], right: GenericToken):
        lookup_key = tuple([self.representatives[x] for x in left.parameters])
        if lookup_key in self.lookup_table:
            (lookup_function_term, lookup_result) = self.lookup_table[lookup_key]
            self.pending.append((left, right, lookup_function_term, lookup_result))
            self.propogate()
        else:
            self.lookup_table[lookup_key] = (left, right)
            for parameter in lookup_key:
                if parameter not in self.use_lists:
                    self.use_lists[parameter] = []
                self.use_lists[parameter].append((left, right))

    def are_congruent(self, left: GenericToken, right: GenericToken) -> bool:
        raise NotImplementedError()
    
    def propogate(self):
        while len(self.pending) > 0:
            pending_equation = self.pending.pop()
            raise NotImplementedError()
    
    def normalize(self, value: GenericToken) -> GenericToken:
        if isinstance(value, Token):
            return self.representatives[value]
        normalized_parameters = [self.normalize(p) for p in value.parameters]
        if all([isinstance(p, Token) for p in normalized_parameters]):
            normalized_parameters = cast(list[Token], normalized_parameters)
            lookup = self.lookup_table.get(tuple(normalized_parameters))
            if lookup is not None:
                return self.representatives[lookup[1]]
        return GenericFunctionTerm(value.function, normalized_parameters)

    def explain(self, left: GenericToken, right: GenericToken):
        raise NotImplementedError()

    def explain_along_path(self, left: GenericToken, right: GenericToken):
        raise NotImplementedError()
