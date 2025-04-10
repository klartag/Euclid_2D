from typing import List, Optional

from ....rule_utils import POINT, LINE, CIRCLE
from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate

from ...constructions.line_intersection import line_intersection
from ...constructions.circle_intersection import circle_circle_intersection, line_circle_intersection
from ...constructions.object_on_object import point_on_circle, point_on_line
from ...types import normalize_return_type

from ..embedded_constructions.embedded_construction import EmbeddedConstruction
from ..embedded_constructions.explicit_embedded_construction import ExplicitEmbeddedConstruction
from ..embedded_constructions.generalized_embedded_construction import (
    GeneralizedEmbeddedConstruction,
)
from ..embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

from .construction_pattern import ConstructionPattern
from .locus_patterns.implementations import LOCUS_PATTERNS, DUAL_LOCUS_PATTERNS


SINGLE_LOCUS_TYPE_PATTERNS = {LINE: point_on_line, CIRCLE: point_on_circle}


LOCUS_INTERSECTION_TYPE_PATTERNS = {
    (LINE, LINE): line_intersection,
    (LINE, CIRCLE): line_circle_intersection,
    (CIRCLE, CIRCLE): circle_circle_intersection,
}


class ContainmentPattern(ConstructionPattern):
    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        if object_.type != POINT:
            return None

        containing_objects: List[ExtendedGeoObject] = []
        for predicate in predicates:
            locus = self.parse_containment_predicate(object_, predicate)
            if locus is None:
                return None
            containing_objects.append(locus)

        if len(containing_objects) == 1:
            (locus,) = containing_objects
            if locus.type in SINGLE_LOCUS_TYPE_PATTERNS:
                construction_method = normalize_return_type(SINGLE_LOCUS_TYPE_PATTERNS[locus.type])
                return GeneralizedEmbeddedConstruction((locus,), object_.name, construction_method)
        elif len(containing_objects) == 2:
            locus_0, locus_1 = containing_objects
            if (locus_1.type, locus_0.type) in LOCUS_INTERSECTION_TYPE_PATTERNS:
                locus_1, locus_0 = locus_0, locus_1
            if (locus_0.type, locus_1.type) in LOCUS_INTERSECTION_TYPE_PATTERNS:
                construction_method = normalize_return_type(
                    LOCUS_INTERSECTION_TYPE_PATTERNS[(locus_0.type, locus_1.type)]
                )
                return ExplicitEmbeddedConstruction((locus_0, locus_1), object_.name, construction_method)

        return None

    def parse_containment_predicate(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]:
        patterns = []
        if object_.type == POINT:
            patterns = LOCUS_PATTERNS
        elif object_.type == LINE:
            patterns = DUAL_LOCUS_PATTERNS

        for locus_pattern in patterns:
            locus = locus_pattern.match(object_, predicate)
            if locus is not None:
                return locus
        else:
            return None
