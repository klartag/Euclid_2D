from typing import Type, TypeVar, List, Optional, Tuple
from dataclasses import dataclass

from ....rule_utils import POINT

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.implementations.in_predicate import InPredicate

from ..embedded_constructions import EmbeddedConstruction

from .construction_pattern import ConstructionPattern


C = TypeVar('C', bound=EmbeddedConstruction)


@dataclass
class IntersectionPattern[C](ConstructionPattern):
    intersection_types: Tuple[str]
    construction_type: Type[C]

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[C]:
        if object_.type != POINT:
            return None

        containing_objects: List[GeoObject] = []
        for predicate in predicates:
            if not isinstance(predicate, InPredicate):
                return None
            if predicate.components[0] != object_:
                return None
            for containing_object in predicate.components[1:]:
                if containing_object.type == POINT:
                    return None
                containing_objects.append(containing_object)

        sorted_object_names = []

        for intersection_type in self.intersection_types:
            for containing_object in list(containing_objects):
                if containing_object.type == intersection_type:
                    containing_objects.remove(containing_object)
                    sorted_object_names.append(containing_object.name)
                    break
            else:
                return None

        if len(containing_objects) > 0:
            return None

        return self.construction_type(tuple(sorted_object_names), object_.name)
