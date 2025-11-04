from typing import cast, overload

from ...indexed_set import IndexedSet

from .equations.equation import Equation
from .equations.equation_pair import EquationPair
from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm


Constant = int
BasicFunctionEquation = Equation[BasicFunctionTerm[Constant], Constant]
Term = Constant | BasicFunctionTerm[Constant]

class CongruenceClosureTracker[T]:
    tokens: IndexedSet[T | BasicFunctionTerm[Constant]]
    pending: list[Equation[Constant, Constant] | EquationPair[Constant]]
    representatives: dict[Constant, Constant]
    class_lists: dict[Constant, list[Constant]]
    use_lists: dict[Constant, list[BasicFunctionEquation]]
    lookup_table: dict[tuple[str, tuple[Constant, ...]], BasicFunctionEquation]
    proof_forest: list[tuple[Constant, Constant, BasicFunctionEquation]] # Replace this with a proper data structure later.

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
    
    def merge_complex_equation(self, left: BasicFunctionTerm[Constant], right: Constant):
        '''
        Adds the equation `left == right` to the Congruence Closure Tracker,
        where the equation is of the form `function(a1, a2, ...) = a`.
        '''
        lookup_key = (left.function, tuple([self.representatives[x] for x in left.parameters]))
        if lookup_key in self.lookup_table:
            basic_function_equation = self.lookup_table[lookup_key]
            self.pending.append(EquationPair(left, right, basic_function_equation.left, basic_function_equation.right))
            self.propogate()
        else:
            self.lookup_table[lookup_key] = Equation(left, right)
            for parameter in lookup_key[1]:
                if parameter not in self.use_lists:
                    self.use_lists[parameter] = []
                self.use_lists[parameter].append(Equation(left, right))

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
    
    def as_token(self, term: BasicFunctionTerm[Constant]) -> Constant:
        self.tokens.add(term)
        return self.tokens.index(term)
    
    @overload
    def normalize(self, value: Constant) -> Term:
        ...
        
    @overload
    def normalize(self, value: BasicFunctionTerm[Constant]) -> Term:
        ...
        
    @overload
    def normalize(self, value: GenericFunctionTerm[Constant]) -> Term:
        ...

    def normalize(self, value: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]) -> Term:
        '''
        TODO: Document
        '''
        if isinstance(value, Constant):
            return self.representatives[value]
        
        if isinstance(value, BasicFunctionTerm):
            value = GenericFunctionTerm.from_basic_term(value)
        
        normalized_parameters = [self.normalize(p) for p in value.parameters]
        
        for (i, parameter) in enumerate(normalized_parameters):
            if isinstance(parameter, BasicFunctionTerm):
                normalized_parameters[i] = self.as_token(parameter)
                
        normalized_parameters = cast(list[Constant], normalized_parameters)

        lookup = self.lookup_table.get(tuple(normalized_parameters))
        if lookup is not None:
            return self.representatives[lookup[1]]
            
        for i in range(len(normalized_parameters)):
            if isinstance(normalized_parameters[i], BasicFunctionTerm):
                
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
