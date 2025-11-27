from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast, overload
from collections import defaultdict

from ...extended_default_dict import ExtendedDefaultDict
from ...indexed_set import IndexedSet

from .equations.equation import Equation
from .equations.equation_pair import EquationPair
from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm

from .proof_forest import ProofForest


Atom = TypeVar('Atom')
NonAtom = TypeVar('NonAtom')
Predicate = TypeVar('Predicate')

Constant = int
BasicFunctionEquation = Equation[BasicFunctionTerm[Constant], Constant, Predicate]
SimpleTerm = Constant | BasicFunctionTerm[Constant]

class AbstractCongruenceClosureTracker(ABC, Generic[Atom, NonAtom, Predicate]):
    tokens: IndexedSet[Atom | BasicFunctionTerm[Constant]]
    pending: list[Equation[Constant, Constant, Predicate] | EquationPair[Constant, Predicate]]
    representatives: ExtendedDefaultDict[Constant, Constant]
    class_lists: ExtendedDefaultDict[Constant, list[Constant]]
    use_lists: defaultdict[Constant, list[BasicFunctionEquation]]
    lookup_table: dict[tuple[str, tuple[Constant, ...]], BasicFunctionEquation]
    proof_forest: ProofForest[Constant, Predicate]

    def __init__(self):
        self.tokens = IndexedSet()
        self.pending = []
        self.representatives = ExtendedDefaultDict(lambda c: c)
        self.class_lists = ExtendedDefaultDict(lambda c: [c])
        self.use_lists = defaultdict(list)
        self.lookup_table = {}
        self.proof_forest = ProofForest()

    @abstractmethod
    def deconstruct_predicate(self, predicate: Predicate) -> tuple[Atom | NonAtom, Atom | NonAtom]:
        '''
        TODO: Document
        '''
        ...
        
    @abstractmethod
    def deconstruct(self, value: Atom | NonAtom) -> Atom | GenericFunctionTerm[Atom]:
        '''
        TODO: Document
        '''
        ...
        
    @abstractmethod
    def reconstruct_function(self, function: str, parameters: list[Atom | NonAtom]) -> Atom | NonAtom:
        '''
        TODO: Document
        '''
        ...

    def reconstruct(self, value: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]) -> Atom | NonAtom:
        '''
        TODO: Document
        '''
        if isinstance(value, Constant):
            token = self.tokens[value]
            if isinstance(token, BasicFunctionTerm):
                return self.reconstruct(token)
            else:
                return token
            
        if isinstance(value, BasicFunctionTerm):
            value = GenericFunctionTerm.from_basic_term(value)
            
        constructed_parameters = [self.reconstruct(parameter) for parameter in value.parameters]
        return self.reconstruct_function(value.function, constructed_parameters)

    @overload
    def project_atom_type(self, value: Atom) -> Constant: ...
    
    @overload
    def project_atom_type(self, value: BasicFunctionTerm[Atom]) -> BasicFunctionTerm[Constant]: ...
    
    @overload
    def project_atom_type(self, value: GenericFunctionTerm[Atom]) -> GenericFunctionTerm[Constant]: ...

    def project_atom_type(self, value: Atom | BasicFunctionTerm[Atom] | GenericFunctionTerm[Atom]) -> Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]:
        '''
        TODO: Document
        '''
        if isinstance(value, BasicFunctionTerm):
            parameters = [self.project_atom_type(atom) for atom in value.parameters]
            return BasicFunctionTerm(value.function, tuple(parameters))
        elif isinstance(value, GenericFunctionTerm):
            parameters = [
                self.project_atom_type(parameter)
                if isinstance(parameter, GenericFunctionTerm)
                else self.project_atom_type(parameter) 
                for parameter in value.parameters
            ]
            return GenericFunctionTerm(value.function, tuple(parameters))
        else:
            self.tokens.add(value)
            return self.tokens.index(value)
        
    def merge(self, predicate: Predicate):
        left, right = self.deconstruct_predicate(predicate)
        self.merge_atoms(left, right, predicate)

    def merge_atoms(self, left: Atom | NonAtom, right: Atom | NonAtom, predicate: Predicate | None=None):
        '''
        TODO: Document
        '''
        deconstructed_left = self.deconstruct(left)
        deconstructed_right = self.deconstruct(right)
        _left = self._flatten(self.project_atom_type(deconstructed_left))
        _right = self._flatten(self.project_atom_type(deconstructed_right))
        self._merge(_left, _right, predicate)

    def _merge(self, left: SimpleTerm, right: SimpleTerm, predicate: Predicate | None):
        '''
        Adds the equation `left == right` to the Congruence Closure Tracker.
        '''
        if isinstance(left, Constant):
            if isinstance(right, Constant):
                self.pending.append(Equation(left=left, right=right, predicate=predicate))
                self._propogate()
            else:
                self._merge_complex_equation(right, left, predicate)
        else:
            self._merge_complex_equation(left, self._flatten(right), predicate)
    
    def _merge_complex_equation(self, left: BasicFunctionTerm[Constant], right: Constant, predicate: Predicate | None):
        '''
        Adds the equation `left == right` to the Congruence Closure Tracker,
        where the equation is of the form `function(a1, a2, ...) = a`.
        '''
        lookup = self._lookup(left)
        if lookup is not None:
            self.pending.append(EquationPair(left=right, left_term=left, right=lookup.right, right_term=lookup.left, predicate=predicate, second_predicate=lookup.predicate))
            self._propogate()
        else:
            self._set_lookup(left, Equation(left=left, right=right, predicate=predicate))
            for parameter in self._get_lookup_key(left)[1]:
                self.use_lists[parameter].append(Equation(left=left, right=right, predicate=predicate))

    def are_congruent(self, left: Atom | NonAtom, right: Atom | NonAtom) -> bool:
        '''
        TODO: Document
        '''
        deconstructed_left = self.deconstruct(left)
        deconstructed_right = self.deconstruct(right)
        _left = self.project_atom_type(deconstructed_left)
        _right = self.project_atom_type(deconstructed_right)
        return self._are_congruent(_left, _right)

    def _are_congruent(
        self,
        left: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant],
        right: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]
    ) -> bool:
        '''
        Returns whether `left == right` can be deduced from the equations input so far.
        '''
        left_normalized = self._normalize(left)
        right_normalized = self._normalize(right)

        return left_normalized == right_normalized

    def _propogate(self):
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
            self.proof_forest.add(a, b, pending_equation)
            
            for c in self.class_lists[old_a_prime]:
                self.representatives[c] = b_prime
            self.class_lists[b_prime].extend(self.class_lists[old_a_prime])
            if old_a_prime in self.class_lists:
                del self.class_lists[old_a_prime]
            while len(self.use_lists[old_a_prime]) > 0:
                use = self.use_lists[old_a_prime].pop()
                lookup = self._lookup(use.left)
                if lookup is not None:
                    self.pending.append(EquationPair(left=use.right, left_term=use.left, right=lookup.right, right_term=lookup.left, predicate=use.predicate, second_predicate=lookup.predicate))
                else:
                    self._set_lookup(use.left, use)
                    self.use_lists[b_prime].append(use)
            del self.use_lists[old_a_prime]

    def _get_lookup_key(self, term: BasicFunctionTerm[Constant]) -> tuple[str, tuple[Constant, ...]]:
        '''
        TODO: Document
        '''
        representatives = tuple([self.representatives[parameter] for parameter in term.parameters])
        return (term.function, representatives)
        
    def _lookup(self, term: BasicFunctionTerm[Constant]) -> BasicFunctionEquation | None:
        '''
        TODO: Document
        '''
        return self.lookup_table.get(self._get_lookup_key(term), None)
    
    def _set_lookup(self, term: BasicFunctionTerm[Constant], equation: BasicFunctionEquation):
        '''
        TODO: Document
        '''
        self.lookup_table[self._get_lookup_key(term)] = equation        

    def _semi_flatten(self, term: GenericFunctionTerm[Constant]) -> BasicFunctionTerm[Constant]:
        '''
        TODO: Document
        '''
        parameters = [self._flatten(parameter) for parameter in term.parameters]
        return BasicFunctionTerm(term.function, tuple(parameters))

    def _flatten(self, term: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]) -> Constant:
        '''
        TODO: Document
        '''
        if isinstance(term, Constant):
            return term
        if isinstance(term, GenericFunctionTerm):
            term = self._semi_flatten(term)
        if self.tokens.add(term):
            self.post_process_token_addition(term)
            self._merge(term, self.tokens.index(term), None)
        return self.tokens.index(term)

    def post_process_token_addition(self, term: BasicFunctionTerm[Constant]):
        pass

    def normalize(self, value: Atom | NonAtom) -> Atom | NonAtom:
        '''
        TODO: Document
        '''
        deconstucted_value = self.deconstruct(value)
        _value = self.project_atom_type(deconstucted_value)
        normalized_token_value = self._normalize(_value)
        return self.reconstruct(normalized_token_value)

    def _normalize(self, value: Constant | BasicFunctionTerm[Constant] | GenericFunctionTerm[Constant]) -> SimpleTerm:
        '''
        TODO: Document
        '''
        
        '''
        TODO: In the `CongruenceClosureTracker` class, some functions have symmetries.
        This normalize method does not behave properly with the symmetries.
        
        Maybe reconstructing + deconstructing the object and calling normalize multiple times
        solves the issue?
        But quite possibly we will have to take care of the lookup_table and other properties
        in a more robust manner that takes possible symmetries into account.
        '''
        
        if isinstance(value, Constant):
            return self.representatives[value]
        
        if isinstance(value, BasicFunctionTerm):
            value = GenericFunctionTerm.from_basic_term(value)
        
        normalized_parameters = [self._normalize(p) for p in value.parameters]
        
        for (i, parameter) in enumerate(normalized_parameters):
            if isinstance(parameter, BasicFunctionTerm):
                normalized_parameters[i] = self._flatten(parameter)
                
        normalized_parameters = cast(list[Constant], normalized_parameters)

        lookup = self.lookup_table.get((value.function, tuple(normalized_parameters)))
        if lookup is not None:
            return self.representatives[lookup.right]
        
        return BasicFunctionTerm(value.function, tuple(normalized_parameters))

    def explain(self, left: Atom | NonAtom, right: Atom | NonAtom) -> list[Predicate]:
        '''
        Returns a minimal explanation as to why `left == right` is true.
        '''
        explanation = self._explain(left, right)
        minimal_explanation = self._minimize_explanation(left, right, explanation)
        return minimal_explanation


    def _explain(self, left: Atom | NonAtom, right: Atom | NonAtom) -> list[Predicate]:
        '''
        Returns an explanation as to why `left == right` is true.
        '''
        if not self.are_congruent(left, right):
            raise ValueError("Attempted to explain a false equality.")
        left_atom = self._flatten(self.project_atom_type(self.deconstruct(left)))
        right_atom = self._flatten(self.project_atom_type(self.deconstruct(right)))
        
        return self.proof_forest.explain(left_atom, right_atom)

    def _minimize_explanation(self, left: Atom | NonAtom, right: Atom | NonAtom, explanation: list[Predicate]) -> list[Predicate]:
        '''
        TODO: Document
        TODO: Check if the Fast Congruence Closure paper has anything to say on whether their algorithm should already output a minimal explanation.
        '''
        minimal_explanation = explanation[:]
        
        for i in range(len(explanation) - 1, -1, -1):
            test_explanation = minimal_explanation[:]
            del test_explanation[i]
            
            checker = type(self)()
            for predicate in test_explanation:
                checker.merge(predicate)
            
            if checker.are_congruent(left, right):
                del minimal_explanation[i]
        
        return minimal_explanation
