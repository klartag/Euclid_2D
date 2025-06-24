from typing import List, Optional

from ....geometry_objects.geo_object import GeoObject
from ....geometry_objects.construction_object import ConstructionObject
from ....predicates.predicate import Predicate

from ...method_dictionaries import CONSTRUCTION_METHOD_DICTIONARY

from ..embedded_constructions.explicit_embedded_construction import ExplicitEmbeddedConstruction

from .construction_pattern import ConstructionPattern


class ExplicitConstructionPattern(ConstructionPattern):
    """
    TODO: Document
    """

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[ExplicitEmbeddedConstruction]:
        if len(predicates) != 1:
            return None
        predicate = predicates[0]
        if predicate.name != 'equals':
            return None
        lhs = predicate.components[0]
        rhs = predicate.components[1]
        if not (lhs.name == object_.name and isinstance(rhs, ConstructionObject)):
            return None
        if rhs.constructor.name not in CONSTRUCTION_METHOD_DICTIONARY.keys():
            return None
        if any([involved_object.name == object_.name for involved_object in rhs.involved_objects()]):
            return None
        construction_method = CONSTRUCTION_METHOD_DICTIONARY[rhs.constructor.name]
        return ExplicitEmbeddedConstruction(rhs.components, object_.name, construction_method)
