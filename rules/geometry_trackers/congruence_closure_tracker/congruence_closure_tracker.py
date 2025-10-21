from .input_equations.simple_equation import SimpleEquation
from .input_equations.functional_equation import FunctionalEquation

class CongruenceClosureTracker[T]:
    pending: list[SimpleEquation[T] | tuple[FunctionalEquation[T], FunctionalEquation[T]]]
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
