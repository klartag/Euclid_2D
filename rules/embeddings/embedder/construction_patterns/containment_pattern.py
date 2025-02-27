from typing import Callable, Type, TypeVar, List, Optional, Tuple, Unpack
from dataclasses import dataclass

from ....rule_utils import POINT

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.implementations.in_predicate import InPredicate

from ..embedded_constructions.embedded_construction import EmbeddedConstruction, InputArgs, Output

from .construction_pattern import ConstructionPattern
from .locus_patterns.implementations import LOCUS_PATTERNS

C = TypeVar('C', bound=EmbeddedConstruction)


@dataclass
class ContainmentPattern[C](ConstructionPattern):
    intersection_types: Tuple[str]
    construction_type: Type[C]
    construction_method: Callable[[Unpack[InputArgs]], Output]

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[C]:
        if object_.type != POINT:
            return None

        containing_objects: List[GeoObject] = []
        for predicate in predicates:
            locus = self.parse_containment_predicate(object_, predicate)
            if locus is None:
                return None
            containing_objects.append(locus)

        sorted_objects = []

        for intersection_type in self.intersection_types:
            for containing_object in list(containing_objects):
                if containing_object.type == intersection_type:
                    containing_objects.remove(containing_object)
                    sorted_objects.append(containing_object)
                    break
            else:
                return None

        if len(containing_objects) > 0:
            return None

        return self.construction_type(tuple(sorted_objects), object_.name, self.construction_method)

    def parse_containment_predicate(self, object_: GeoObject, predicate: Predicate) -> Optional[GeoObject]:
        for locus_pattern in LOCUS_PATTERNS:
            locus = locus_pattern.match(object_, predicate)
            if locus is not None:
                return locus
        else:
            return None
