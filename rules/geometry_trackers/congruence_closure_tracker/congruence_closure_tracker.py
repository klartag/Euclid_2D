from ...indexed_set import IndexedSet

from .equations.equation import Equation
from .equations.equation_pair import EquationPair
from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm


Constant = int
Term = Constant | GenericFunctionTerm[Constant]


class CongruenceClosureTracker[T]:
    tokens: IndexedSet[T | BasicFunctionTerm[Constant]]
    pending: list[Equation[Constant, Constant] | EquationPair[Constant]]
    representatives: dict[Constant, Constant]
    class_lists: dict[Constant, list[Constant]]
    use_lists: dict[Constant, list[tuple[BasicFunctionTerm[Constant], Constant]]]
    lookup_table: dict[tuple[Constant, ...], Equation[BasicFunctionTerm[Constant], Constant]]
    proof_forest: list[tuple[Constant, Constant, Equation[BasicFunctionTerm[Constant], Constant]]] # Replace this with a proper data structure later.

    def __init__(self):
        self.tokens = IndexedSet()
        self.pending = []
        self.representatives = {}
        self.class_lists = {}
        self.use_lists = {}
        self.lookup_table = {}
        self.proof_forest = []

    def merge(self, left: Term, right: Term):
        '''
        Adds the equation `left == right` to the Congruence Closure Tracker.
        '''
        if isinstance(left, Constant):
            if isinstance(right, Constant):
                equation = Equation(left, right)
                self.pending.append(equation)
                self.propogate()
            else:
                self.merge_complex_equation(right, left)
        else:
            self.merge_complex_equation(left, right)
    
    def merge_complex_equation(self, left: GenericFunctionTerm[Constant], right: Term):
        '''
        Adds the equation `left == right` to the Congruence Closure Tracker,
        where the equation is of the form `function(a1, a2, ...) = a`.
        '''
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

    def are_congruent(self, left: Term, right: Term) -> bool:
        '''
        Returns whether `left == right` can be deduced from the equations input so far.
        '''
        left_normalized = self.normalize(left)
        right_normalized = self.normalize(right)
        return left_normalized == right_normalized
    
    def propogate(self):
        '''
        TODO: Document
        '''
        while len(self.pending) > 0:
            pending_equation = self.pending.pop()
            raise NotImplementedError()
        
    def flatten(self, term: GenericFunctionTerm[Constant]) -> BasicFunctionTerm[Constant]:
        '''
        TODO: Do we need this? Maybe this should immediately output a `Token`?
        
        Makes sure there is a `BasicFunctionTerm` equivalent to the given `GenericFunctionTerm`
        (introducing new constants if necessary),
        then returns the equivalent `BasicFunctionTerm`.
        '''
        raise NotImplementedError()
    
    def normalize(self, value: Term) -> Term:
        '''
        TODO: Document
        '''
        if isinstance(value, Constant):
            return self.representatives[value]
        normalized_parameters = [self.normalize(p) for p in value.parameters]
        if all([isinstance(p, Constant) for p in normalized_parameters]):
            normalized_parameters = cast(list[Constant], normalized_parameters)
            lookup = self.lookup_table.get(tuple(normalized_parameters))
            if lookup is not None:
                return self.representatives[lookup[1]]
        return GenericFunctionTerm(value.function, normalized_parameters)

    def explain(self, left: Term, right: Term) -> list[object]:
        '''
        Returns an explanation as to why `left == right` is true.
        '''
        raise NotImplementedError()

    def explain_along_path(self, left: Term, right: Term) -> list[object]:
        '''
        TODO: Document
        '''
        raise NotImplementedError()
