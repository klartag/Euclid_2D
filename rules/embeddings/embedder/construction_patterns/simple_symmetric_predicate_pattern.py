from typing import Callable, Type, TypeVar, List, Optional, Tuple, Unpack
from dataclasses import dataclass

from ....rule_utils import POINT

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.implementations.in_predicate import InPredicate

from ..embedded_constructions.embedded_construction import EmbeddedConstruction, InputArgs, Output

from .construction_pattern import ConstructionPattern

C = TypeVar('C', bound=EmbeddedConstruction)


@dataclass
class SimpleSymmetricPredicatePattern[C](ConstructionPattern):
    construction_type: Type[C]
    construction_method: Callable[[Unpack[InputArgs]], Output]
    predicate_name: str

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[C]:
        if len(predicates) != 1:
            return None

        predicate = predicates[0]

        if predicate.name != self.predicate_name:
            return None
        
        if object_ not in predicate.components:
            return None
        
        object_index = predicate.components.index(object_)
        
        rest_of_components = [predicate.components[i] for i in range(len(predicate.components)) if i != object_index]
        
        if any([object_ in component.involved_objects() for component in rest_of_components]):
            return None

        return self.construction_type(tuple(rest_of_components), object_.name, self.construction_method)
