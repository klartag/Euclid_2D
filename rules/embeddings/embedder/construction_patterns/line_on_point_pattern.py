from typing import Type, TypeVar, List, Optional, Tuple
from dataclasses import dataclass


from ....rule_utils import POINT, LINE
from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.implementations.in_predicate import InPredicate

from ..embedded_constructions import LineOnPoint

from .construction_pattern import ConstructionPattern


class LineOnPointPattern(ConstructionPattern):
    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[LineOnPoint]:
        if object_.type != LINE:
            return None
        if len(predicates) != 1:
            return None
        predicate = predicates[0]

        if not (isinstance(predicate, InPredicate) and len(predicate.components) == 2):
            return None

        if not (predicate.components[0].type == POINT and predicate.components[1] == object_):
            return None

        return LineOnPoint((predicate.components[0].name,), object_.name)
