from typing import Type, TypeVar, List, Optional
from dataclasses import dataclass

from .construction_pattern import ConstructionPattern

from ....geometry_objects.geo_object import GeoObject
from ....geometry_objects.construction_object import ConstructionObject
from ....predicates.predicate import Predicate
from ..embedded_constructions import EmbeddedConstruction


C = TypeVar('C', bound=EmbeddedConstruction)


@dataclass
class ExplicitConstructionPattern[C](ConstructionPattern):
    construction_name: str
    construction_type: Type[C]

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[C]:
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
        rhs_names = tuple([obj.name for obj in rhs.components])
        if not (object_.name not in rhs_names and all(name.isalnum() for name in rhs_names)):
            return None
        return self.construction_type(rhs_names, object_.name)
