from typing import List, Optional

from .construction_pattern import ConstructionPattern

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate

from ...types import ConstructionMethod, ExtendedConstructionMethod, normalize_return_type

from ..embedded_constructions.embedded_construction import EmbeddedConstruction
from ..embedded_constructions.explicit_embedded_construction import ExplicitEmbeddedConstruction


class EmptyPattern(ConstructionPattern):
    """
    Describes a pattern in which an object can be embedded without restrictions.
    """

    object_type: str
    """
    The type of object this pattern represents.
    """
    construction_method: ConstructionMethod
    """
    A ConstructionMethod that knows to randomly sample an object of the type `object_type`.
    """

    def __init__(self, object_type: str, construction_method: ExtendedConstructionMethod):
        self.object_type = object_type
        self.construction_method = normalize_return_type(construction_method)

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        if len(predicates) != 0 or object_.type != self.object_type:
            return None
        return ExplicitEmbeddedConstruction((), object_.name, self.construction_method)
