from typing import cast
from collections import defaultdict

from ...extended_default_dict import ExtendedDefaultDict
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
    representatives: ExtendedDefaultDict[Constant, Constant]
    class_lists: ExtendedDefaultDict[Constant, list[Constant]]
    use_lists: defaultdict[Constant, list[BasicFunctionEquation]]
    lookup_table: dict[tuple[str, tuple[Constant, ...]], BasicFunctionEquation]
    proof_forest: list[tuple[Constant, Constant, BasicFunctionEquation]] # Replace this with a proper data structure later.

    def __init__(self):
        self.tokens = IndexedSet()
        self.pending = []
        self.representatives = ExtendedDefaultDict(lambda c: c)
        self.class_lists = ExtendedDefaultDict(lambda c: [c])
        self.use_lists = defaultdict(list)
        self.lookup_table = {}
        self.proof_forest = []

    def merge(self, left: Term, right: Term):
        '''
        Adds the equation `left == right` to the Congruence Closure Tracker.
        '''
        if isinstance(left, Constant):
            if isinstance(right, Constant):
                self.pending.append(Equation(left, right))
                self.propogate()
            else:
                self.merge_complex_equation(right, left)
        else:
            self.merge_complex_equation(left, self.flatten(right))
    
    def merge_complex_equation(self, left: BasicFunctionTerm[Constant], right: Constant):
        '''
        Adds the equation `left == right` to the Congruence Closure Tracker,
        where the equation is of the form `function(a1, a2, ...) = a`.
        '''
        lookup = self.lookup(left)
        if lookup is not None:
            self.pending.append(EquationPair(right, lookup.right, left, lookup.left))
            self.propogate()
        else:
            self.set_lookup(left, Equation(left, right))
            for parameter in self.get_lookup_key(left)[1]:
                self.use_lists[parameter].append(Equation(left, right))

    def are_congruent(
        self,
        left: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant],
        right: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]
    ) -> bool:
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
            a, b = pending_equation.left, pending_equation.right
            a_prime, b_prime = self.representatives[a], self.representatives[b]
            
            if a_prime == b_prime:
                continue
            if len(self.class_lists[a_prime]) > len(self.class_lists[b_prime]):
                a, b = b, a
                a_prime, b_prime = b_prime, a_prime
            
            old_a_prime = a_prime
            for c in self.class_lists[old_a_prime]:
                self.representatives[c] = b_prime
            self.class_lists[b_prime].extend(self.class_lists[old_a_prime])
            if old_a_prime in self.class_lists:
                del self.class_lists[old_a_prime]
            while len(self.use_lists[old_a_prime]) > 0:
                use = self.use_lists[old_a_prime].pop()
                lookup = self.lookup(use.left)
                if lookup is not None:
                    self.pending.append(EquationPair(use.right, lookup.right, use.left, lookup.left))
                else:
                    self.set_lookup(use.left, use)
                    self.use_lists[b_prime].append(use)
            del self.use_lists[old_a_prime]

    def get_lookup_key(self, term: BasicFunctionTerm[Constant]) -> tuple[str, tuple[Constant, ...]]:
        representatives = tuple([self.representatives[parameter] for parameter in term.parameters])
        return (term.function, representatives)
        
    def lookup(self, term: BasicFunctionTerm[Constant]) -> BasicFunctionEquation | None:
        return self.lookup_table.get(self.get_lookup_key(term), None)
    
    def set_lookup(self, term: BasicFunctionTerm[Constant], equation: BasicFunctionEquation):
        self.lookup_table[self.get_lookup_key(term)] = equation        

    def semi_flatten(self, term: GenericFunctionTerm[Constant]) -> BasicFunctionTerm[Constant]:
        parameters = [self.flatten(parameter) for parameter in term.parameters]
        return BasicFunctionTerm(term.function, tuple(parameters))

    def flatten(self, term: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]) -> Constant:
        if isinstance(term, Constant):
            return term
        if isinstance(term, GenericFunctionTerm):
            term = self.semi_flatten(term)
        self.tokens.add(term)
        return self.tokens.index(term)

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
                normalized_parameters[i] = self.flatten(parameter)
                
        normalized_parameters = cast(list[Constant], normalized_parameters)

        lookup = self.lookup_table.get((value.function, tuple(normalized_parameters)))
        if lookup is not None:
            return self.representatives[lookup.right]
        
        return BasicFunctionTerm(value.function, tuple(normalized_parameters))

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
