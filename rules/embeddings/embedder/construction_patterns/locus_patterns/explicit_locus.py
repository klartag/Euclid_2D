from typing import Optional

from .....rule_utils import POINT
from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate
from .....predicates.implementations.in_predicate import InPredicate

from ...embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

from .locus_pattern_matcher import LocusPattern


class ExplicitLocus(LocusPattern):
    def match(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]:
        if not isinstance(predicate, InPredicate):
            return None
        if len(predicate.components) != 2:
            return None
        if predicate.components[0] != object_:
            return None
        if predicate.components[1].type == POINT:
            return None
        if object_ in predicate.components[1].involved_objects():
            return None
        return predicate.components[1]
