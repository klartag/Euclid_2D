from typing import Type, List, Optional, Tuple

from ....rule_utils import POINT
from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate

from ...types import ConstructionMethod, ExtendedConstructionMethod, normalize_return_type

from ..embedded_constructions.embedded_construction import EmbeddedConstruction
from ..embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

from .construction_pattern import ConstructionPattern
from .locus_patterns.implementations import LOCUS_PATTERNS


class ContainmentPattern(ConstructionPattern):
    intersection_types: Tuple[str]
    construction_type: Type[EmbeddedConstruction]
    construction_method: ConstructionMethod


    def __init__(
        self,
        intersection_types: Tuple[str],
        construction_type: Type[EmbeddedConstruction],
        construction_method: ExtendedConstructionMethod
    ):
        self.intersection_types = intersection_types
        self.construction_type = construction_type
        self.construction_method = normalize_return_type(construction_method)

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        if object_.type != POINT:
            return None

        containing_objects: List[ExtendedGeoObject] = []
        for predicate in predicates:
            locus = self.parse_containment_predicate(object_, predicate)
            if locus is None:
                return None
            containing_objects.append(locus)

        sorted_objects: List[ExtendedGeoObject] = []

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

    def parse_containment_predicate(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]:
        for locus_pattern in LOCUS_PATTERNS:
            locus = locus_pattern.match(object_, predicate)
            if locus is not None:
                return locus
        else:
            return None
