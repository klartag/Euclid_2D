from typing import Callable, List, Optional, Unpack
from dataclasses import dataclass

from ....geometry_objects.geo_object import GeoObject
from ....geometry_objects.construction_object import ConstructionObject
from ....predicates.predicate import Predicate

from ..embedded_constructions.embedded_construction import InputArgs, Output
from ..embedded_constructions.explicit_embedded_construction import ExplicitEmbeddedConstruction

from .construction_pattern import ConstructionPattern


@dataclass
class ExplicitConstructionPattern(ConstructionPattern):
    construction_name: str
    construction_method: Callable[[Unpack[InputArgs]], Output]

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[ExplicitEmbeddedConstruction]:
        if len(predicates) != 1:
            return None
        predicate = predicates[0]
        if predicate.name != 'equals':
            return None
        lhs = predicate.components[0]
        rhs = predicate.components[1]
        if not (lhs.name == object_.name and isinstance(rhs, ConstructionObject)):
            return None
        if rhs.constructor.name != self.construction_name:
            return None
        if any([involved_object.name == object_.name for involved_object in rhs.involved_objects()]):
            return None
        return ExplicitEmbeddedConstruction(rhs.components, object_.name, self.construction_method)
