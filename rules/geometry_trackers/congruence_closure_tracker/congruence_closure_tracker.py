from typing import Tuple, cast

from ...symmetry import Symmetry

from ...predicates.global_predicates import get_constructions
from ...predicates.predicate import Predicate
from ...predicates.predicate_factory import predicate_from_args

from ...geometry_objects.atom import Atom as GeometryAtom
from ...geometry_objects.literal import Literal as GeometryLiteral
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_objects.equation_object import EquationObject
from ...geometry_objects.eq_op import EqOp
from ...geometry_objects.geo_object import GeoObject

from .abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker, Constant
from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm


Atom = GeometryAtom | GeometryLiteral | bool
NonAtom = GeoObject | Predicate
Function = Tuple[str, Symmetry] | EqOp

class CongruenceClosureTracker(AbstractCongruenceClosureTracker[Atom, NonAtom, Function, Predicate]):
    def merge(self, predicate: Predicate):
        if predicate.name == 'equals':
            super().merge(predicate)
        else:
            super().merge_atoms(predicate, True, predicate)

    def deconstruct_predicate(self, predicate: Predicate) -> tuple[Atom | NonAtom, Atom | NonAtom]:
        if predicate.name != 'equals':
            raise ValueError('Can only merge equality predicates.')
        if len(predicate.components) != 2:
            raise ValueError('Can only merge equality predicates between two objects.')
        left, right = predicate.components[0], predicate.components[1]
        return (left, right)

    def deconstruct(self, value: Atom | NonAtom) -> Atom | GenericFunctionTerm[Function, Atom]:
        if isinstance(value, GeoObject):
            if isinstance(value, (GeometryAtom, GeometryLiteral)):
                return value
            elif isinstance(value, ConstructionObject):
                function = (value.constructor.name, value.constructor.symmetry)
                parameters = value.components
                deconstructed_parameters = tuple([self.deconstruct(parameter) for parameter in parameters])
                return GenericFunctionTerm(function, deconstructed_parameters)
            elif isinstance(value, EquationObject):
                deconsructed_parameters = (self.deconstruct(value.left), self.deconstruct(value.right))
                return GenericFunctionTerm(value.op, deconsructed_parameters)
            else:
                raise ValueError("Encountered an unknown type of GeoObject.")
        elif isinstance(value, Predicate):
            function = (value.name, value.symmetry)
            parameters = value.components
            deconstructed_parameters = tuple([self.deconstruct(parameter) for parameter in parameters])
            return GenericFunctionTerm(function, deconstructed_parameters)
        else:
            return value

    def post_process_token_addition(self, term: BasicFunctionTerm[Function, Constant]):
        if isinstance(term.function, EqOp):
            return
        symmetrical_orders = term.function[1].all_orders(term.parameters)
        symmetrical_orders.remove(term.parameters)
        symmetrical_terms = [BasicFunctionTerm(term.function, order) for order in symmetrical_orders]
        term_atom = self._flatten(term)
        for symmetrical_term in symmetrical_terms:
            self._merge(term_atom, symmetrical_term, None)

    def reconstruct_function(self, function: Function, parameters: list[Atom | NonAtom]) -> Atom | NonAtom:
        cast_parameters = cast(list[GeoObject], parameters)
        if isinstance(function, EqOp):
            return EquationObject(cast_parameters[0], cast_parameters[1], function)
        else:
            tuple_parameters = tuple(cast_parameters)
            if function[0] in get_constructions():
                return ConstructionObject.from_args(function[0], tuple_parameters)
            else:
                return predicate_from_args(function[0], tuple_parameters) 


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
