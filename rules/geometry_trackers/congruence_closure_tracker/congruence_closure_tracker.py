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

    def __init__(self):
        self.tokens = IndexedSet()
        self.pending = []
        self.representatives = {}
        self.class_lists = {}
        self.use_lists = {}
        self.lookup_table = {}

    def merge(self, left: GenericToken, right: GenericToken):
        if isinstance(left, Token) and isinstance(right, Token):
            self.pending.append((left, right))
            self.propogate()
            return
        
        if isinstance(right, Token):
            left, right = right, left
        
        raise NotImplementedError()

    def are_congruent(self, left: GenericToken, right: GenericToken) -> bool:
        raise NotImplementedError()
    
    def propogate(self):
        raise NotImplementedError()
    
    def normalize(self, value: GenericToken) -> GenericToken:
        raise NotImplementedError()

    def explain(self, left: GenericToken, right: GenericToken):
        raise NotImplementedError()

    def explain_along_path(self, left: GenericToken, right: GenericToken):
        raise NotImplementedError()
    
    def is_constant(self, term: GenericToken) -> bool:
        raise NotImplementedError()
