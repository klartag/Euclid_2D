from typing import Type, List, Optional

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate

from ...types import ConstructionMethod, ExtendedConstructionMethod, normalize_return_type

from ..embedded_constructions.embedded_construction import EmbeddedConstruction

from .construction_pattern import ConstructionPattern


class SimpleSymmetricPredicatePattern(ConstructionPattern):
    """
    TODO: Document
    """

    construction_type: Type[EmbeddedConstruction]
    construction_method: ConstructionMethod
    predicate_name: str

    def __init__(
        self,
        construction_type: Type[EmbeddedConstruction],
        construction_method: ExtendedConstructionMethod,
        predicate_name: str,
    ):
        self.construction_type = construction_type
        self.construction_method = normalize_return_type(construction_method)
        self.predicate_name = predicate_name

    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        if len(predicates) != 1:
            return None

        predicate = predicates[0]

        if predicate.name != self.predicate_name:
            return None

        if object_ not in predicate.components:
            return None

        object_index = predicate.components.index(object_)

        rest_of_components = [predicate.components[i] for i in range(len(predicate.components)) if i != object_index]

        if any([object_ in component.involved_objects() for component in rest_of_components]):
            return None

        return self.construction_type(tuple(rest_of_components), object_.name, self.construction_method)
