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
class ReverseContainmentPattern[C](ConstructionPattern):
    contained_point_count: int
    return_type: str
    construction_type: Type[C]
    construction_method: Callable[[Unpack[InputArgs]], Output]

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[C]:
        if object_.type != self.return_type:
            return None

        contained_points: List[GeoObject] = []
        for predicate in predicates:
            if not isinstance(predicate, InPredicate):
                return None
            if predicate.components[-1] != object_:
                return None
            for contained_point in predicate.components[:-1]:
                if contained_point.type == POINT:
                    contained_points.append(contained_point)
                else:
                    return None
                
        if len(contained_points) != self.contained_point_count:
            return None

        return self.construction_type(tuple(contained_points), object_.name, self.construction_method)
