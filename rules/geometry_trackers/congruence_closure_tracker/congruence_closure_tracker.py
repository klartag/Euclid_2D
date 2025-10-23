from ...indexed_set import IndexedSet

from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm


Token = int


class CongruenceClosureTracker[T]:
    tokens: IndexedSet[T | BasicFunctionTerm[T]]
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

    def merge(self, left: Token, right: Token):
        raise NotImplementedError()

    def are_congruent(self, left: Token, right: Token) -> bool:
        raise NotImplementedError()
    
    def propogate(self):
        raise NotImplementedError()
    
    def normalize(self, value: Token) -> Token:
        raise NotImplementedError()

    def explain(self, left: Token, right: Token):
        raise NotImplementedError()

    def explain_along_path(self, left: Token, right: Token):
        raise NotImplementedError()
