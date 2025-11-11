
from ...geometry_objects.atom import Atom
from ...geometry_objects.literal import Literal
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_objects.geo_object import GeoObject

from .abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker
from .terms.generic_function_term import GenericFunctionTerm


class CongruenceClosureTracker(AbstractCongruenceClosureTracker[Atom | Literal, GeoObject]):
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
