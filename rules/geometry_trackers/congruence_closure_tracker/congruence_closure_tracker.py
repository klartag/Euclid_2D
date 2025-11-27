from ...predicates.global_predicates import get_constructions
from ...predicates.predicate import Predicate

from ...geometry_objects.atom import Atom
from ...geometry_objects.literal import Literal
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_objects.geo_object import GeoObject

from .abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker
from .terms.basic_function_term import BasicFunctionTerm
from .terms.generic_function_term import GenericFunctionTerm


class CongruenceClosureTracker(AbstractCongruenceClosureTracker[Atom | Literal, GeoObject, Predicate]):
    def deconstruct_predicate(self, predicate: Predicate) -> tuple[GeoObject, GeoObject]:
        if predicate.name != 'equals':
            raise ValueError('Can only merge equality predicates.')
        if len(predicate.components) != 2:
            raise ValueError('Can only merge equality predicates between two objects.')
        left, right = predicate.components[0], predicate.components[1]
        return (left, right)

    def deconstruct(self, value: GeoObject) -> Atom | Literal | GenericFunctionTerm[Atom | Literal]:
        if isinstance(value, (Atom, Literal)):
            return value
        elif isinstance(value, ConstructionObject):
            function = value.constructor.name
            parameters = value.components
            deconsructed_parameters = tuple([self.deconstruct(parameter) for parameter in parameters])
            return GenericFunctionTerm(function, deconsructed_parameters)
        else:
            raise ValueError("Cannot deconstruct an object that isn't an Atom, Literal, or ConstructionObject.")

    def post_process_token_addition(self, term: BasicFunctionTerm[int]):
        symmetrical_orders = get_constructions()[term.function].symmetry.all_orders(term.parameters)
        symmetrical_terms = [BasicFunctionTerm(term.function, order) for order in symmetrical_orders]
        symmetrical_terms.remove(term)
        term_atom = self._flatten(term)
        for symmetrical_term in symmetrical_terms:
            self._merge(term_atom, symmetrical_term, None)

    def reconstruct_function(self, function: str, parameters: list[Atom | Literal | GeoObject]) -> Atom | Literal | GeoObject:
        return ConstructionObject.from_args(function, tuple(parameters))
