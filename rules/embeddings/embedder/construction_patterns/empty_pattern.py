from typing import Type, TypeVar, List, Optional
from dataclasses import dataclass

from .construction_pattern import ConstructionPattern

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ..embedded_constructions.embedded_construction import EmbeddedConstruction
from ..embedded_constructions.explicit_embedded_construction import ExplicitEmbeddedConstruction


C = TypeVar('C', bound=EmbeddedConstruction)


@dataclass
class EmptyPattern[C](ConstructionPattern):
    object_type: str
    construction_method: Type[C]

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        if len(predicates) != 0 or object_.type != self.object_type:
            return None
        return ExplicitEmbeddedConstruction((), object_.name, self.construction_method)
