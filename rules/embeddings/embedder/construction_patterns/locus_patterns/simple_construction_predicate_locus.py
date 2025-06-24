from dataclasses import dataclass
from typing import List, Optional, Sequence, Union

from .....geometry_objects.geo_object import GeoObject
from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate

from ...embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

from .unpacking_predicate_locus import UnpackingPredicateLocus, unpack_index_options


@dataclass
class SimplePredicateConstructionLocus(UnpackingPredicateLocus):
    """
    TODO: Document
    """

    construction_name: str
    construction_index_options: Union[int, Sequence[int], None]

    def match_predicate_parameter_option(
        self, object_: GeoObject, predicate: Predicate, parameter_index: int
    ) -> Optional[ExtendedGeoObject]:
        if predicate.name != self.predicate_name:
            return None

        rest_of_components = [predicate.components[i] for i in range(len(predicate.components)) if i != parameter_index]

        if any([object_ in component.involved_objects() for component in rest_of_components]):
            return None

        construction_object = predicate.components[parameter_index]
        if not isinstance(construction_object, ConstructionObject):
            return None

        construction_index_options = unpack_index_options(
            self.construction_index_options, len(construction_object.components)
        )
        for construction_index in construction_index_options:
            locus = self.match_predicate_construction_parameter_options(
                object_, rest_of_components, construction_object, construction_index
            )
            if locus is not None:
                return locus
        else:
            return None

    def match_predicate_construction_parameter_options(
        self,
        object_: GeoObject,
        rest_of_predicate_components: List[GeoObject],
        construction_object: ConstructionObject,
        construction_index: int,
    ) -> Optional[ExtendedGeoObject]:
        """
        TODO: Document
        """
        if construction_object.constructor.name != self.construction_name:
            return None

        if object_ != construction_object.components[construction_index]:
            return None

        rest_of_construction_components = [
            construction_object.components[i]
            for i in range(len(construction_object.components))
            if i != construction_index
        ]

        if any([object_ in component.involved_objects() for component in rest_of_construction_components]):
            return None

        return self.locus_construction_method(*rest_of_construction_components, *rest_of_predicate_components)
