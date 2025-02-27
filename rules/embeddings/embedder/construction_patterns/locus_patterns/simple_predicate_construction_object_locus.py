from dataclasses import dataclass
from typing import Callable, Optional, Tuple, Unpack

from rules.geometry_objects.construction_object import ConstructionObject

from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate

from .locus_pattern_matcher import LocusPattern


@dataclass
class SimplePredicateConstructionObjectLocus(LocusPattern):
    predicate_name: str
    predicate_parameter_index: int
    construction_name: str
    construction_parameter_index: int
    locus_construction_method: Callable[[Unpack[Tuple[GeoObject, ...]]], GeoObject]

    def match(self, object_: GeoObject, predicate: Predicate) -> Optional[GeoObject]:
        if predicate.name != self.predicate_name:
            return None
        if len(predicate.components) <= self.predicate_parameter_index:
            return None
        construction_object = predicate.components[self.parameter_index]
        if not isinstance(construction_object, ConstructionObject):
            return None
        if len(construction_object.components) <= self.construction_parameter_index:
            return None
        if object_ != construction_object.components[self.construction_parameter_index]:
            return None
        
        rest_of_predicate_components = [predicate.components[i] for i in range(len(predicate.components)) if i != self.predicate_parameter_index]
        rest_of_construction_components = [predicate.components[i] for i in range(len(construction_object.components)) if i != self.construction_parameter_index]

        if any([object_ in component.involved_objects() for component in [rest_of_predicate_components + rest_of_construction_components]]):
            return None

        return self.locus_construction_method(*rest_of_construction_components, *rest_of_predicate_components)
