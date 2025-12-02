from ...predicates.global_predicates import get_constructions
from ...predicates.predicate import Predicate

from ...geometry_objects.atom import Atom
from ...geometry_objects.literal import Literal
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_objects.equation_object import EquationObject
from ...geometry_objects.eq_op import EqOp
from ...geometry_objects.geo_object import GeoObject

from .abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker
from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm


Function = str | EqOp

class CongruenceClosureTracker(AbstractCongruenceClosureTracker[Atom | Literal, GeoObject, Function, Predicate]):
    def deconstruct_predicate(self, predicate: Predicate) -> tuple[GeoObject, GeoObject]:
        if predicate.name != 'equals':
            raise ValueError('Can only merge equality predicates.')
        if len(predicate.components) != 2:
            raise ValueError('Can only merge equality predicates between two objects.')
        left, right = predicate.components[0], predicate.components[1]
        return (left, right)

    def deconstruct(self, value: GeoObject) -> Atom | Literal | GenericFunctionTerm[Function, Atom | Literal]:
        if isinstance(value, (Atom, Literal)):
            return value
        elif isinstance(value, ConstructionObject):
            function = value.constructor.name
            parameters = value.components
            deconsructed_parameters = tuple([self.deconstruct(parameter) for parameter in parameters])
            return GenericFunctionTerm(function, deconsructed_parameters)
        elif isinstance(value, EquationObject):
            deconsructed_parameters = (self.deconstruct(value.left), self.deconstruct(value.right))
            return GenericFunctionTerm(value.op, deconsructed_parameters)
        else:
            raise ValueError("Cannot deconstruct an object that isn't an Atom, Literal, or ConstructionObject.")

    def post_process_token_addition(self, term: BasicFunctionTerm[Function, int]):
        if isinstance(term.function, EqOp):
            return
        symmetrical_orders = get_constructions()[term.function].symmetry.all_orders(term.parameters)
        symmetrical_orders.remove(term.parameters)
        symmetrical_terms = [BasicFunctionTerm(term.function, order) for order in symmetrical_orders]
        term_atom = self._flatten(term)
        for symmetrical_term in symmetrical_terms:
            self._merge(term_atom, symmetrical_term, None)

    def reconstruct_function(self, function: str, parameters: list[Atom | Literal | GeoObject]) -> Atom | Literal | GeoObject:
        return ConstructionObject.from_args(function, tuple(parameters))

    def clone(self) -> 'CongruenceClosureTracker':
        clone = CongruenceClosureTracker()
        clone.tokens = self.tokens.clone()
        clone.pending = self.pending[:]
        
        for (k, v) in self.representatives.items():
            clone.representatives[k] = v

        for (k, v) in self.class_lists.items():
            clone.class_lists[k] = v[:]
            
        for (k, v) in self.use_lists.items():
            clone.use_lists[k] = v[:]
            
        for (k, v) in self.lookup_table.items():
            clone.lookup_table[k] = v
        
        clone.proof_forest = self.proof_forest.clone()
        
        return clone
