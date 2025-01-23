from typing import Type, TypeVar, List, Optional
from dataclasses import dataclass

from .construction_pattern import ConstructionPattern

from ....geometry_objects.geo_object import GeoObject
from ....geometry_objects.construction_object import ConstructionObject
from ....predicates.predicate import Predicate
from ..embedded_constructions import EmbeddedConstruction


C = TypeVar('C', bound=EmbeddedConstruction)


@dataclass
class EmptyPattern[C](ConstructionPattern):
    object_type: str
    construction_type: Type[C]

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        if len(predicates) != 0 or object_.type != self.object_type:
            return None
        return self.construction_type((), object_.name)
