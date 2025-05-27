from typing import Type, List, Optional

from ....geometry_objects.geo_type import GeoType

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.implementations.in_predicate import InPredicate

from ...types import ConstructionMethod, ExtendedConstructionMethod, normalize_return_type

from ..embedded_constructions.embedded_construction import EmbeddedConstruction

from .construction_pattern import ConstructionPattern


class ReverseContainmentPattern(ConstructionPattern):
    contained_point_count: int
    return_type: str
    construction_type: Type[EmbeddedConstruction]
    construction_method: ConstructionMethod

    def __init__(
        self,
        contained_point_count: int,
        return_type: str,
        construction_type: Type[EmbeddedConstruction],
        construction_method: ExtendedConstructionMethod,
    ):
        self.contained_point_count = contained_point_count
        self.return_type = return_type
        self.construction_type = construction_type
        self.construction_method = normalize_return_type(construction_method)

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        if object_.type != self.return_type:
            return None

        contained_points: List[GeoObject] = []
        for predicate in predicates:
            if not isinstance(predicate, InPredicate):
                return None
            if len(predicate.components) != 2:
                return None
            if predicate.components[0].type != GeoType.POINT:
                return None
            if predicate.components[1] != object_:
                return None
            if object_ in predicate.components[0].involved_objects():
                return None
            contained_points.append(predicate.components[0])

        if len(contained_points) != self.contained_point_count:
            return None

        return self.construction_type(tuple(contained_points), object_.name, self.construction_method)
