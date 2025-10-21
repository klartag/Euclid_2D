from .terms.basic_function_term import BasicFunctionTerm
from .terms.constant_term import ConstantTerm
from .terms.generic_function_term import GenericFunctionTerm

class CongruenceClosureTracker[T]:
    pending: list[
        tuple[ConstantTerm[T], ConstantTerm[T]]
        | tuple[BasicFunctionTerm[T], ConstantTerm[T], BasicFunctionTerm[T], ConstantTerm[T]]
    ]
    representatives: dict[T, T]
    class_lists: dict[T, list[T]]
    use_lists: dict[T, list[FunctionalEquation[T]]]
    lookup_table: dict[tuple[T, T], FunctionalEquation[T]]

    def __init__(self):
        self.pending = []
        self.representatives = {}
        self.class_lists = {}
        self.use_lists = {}
        self.lookup_table = {}

    def merge(self, left: T, right: T):
        raise NotImplementedError()

    def are_congruent(self, left: T, right: T) -> bool:
        raise NotImplementedError()
    
    def propogate(self):
        raise NotImplementedError()
    
    def normalize(self, value: T) -> T:
        raise NotImplementedError()

    def explain(self, left: T, right: T):
        raise NotImplementedError()

    def explain_along_path(self, left: T, right: T):
        raise NotImplementedError()
