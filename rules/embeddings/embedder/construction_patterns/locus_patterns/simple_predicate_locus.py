from dataclasses import dataclass
from typing import Callable, Optional, Sequence, Tuple, Unpack, Union

from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate

from .unpacking_predicate_locus import UnpackingPredicateLocus


@dataclass
class SimplePredicateLocus(UnpackingPredicateLocus):
    def match_predicate_parameter_option(self, object_: GeoObject, predicate: Predicate, parameter_index: int) -> Optional[GeoObject]:
        if predicate.name != self.predicate_name:
            return None

        if object_ != predicate.components[parameter_index]:
            return None

        rest_of_components = [predicate.components[i] for i in range(len(predicate.components)) if i != parameter_index]

        if any([object_ in component.involved_objects() for component in rest_of_components]):
            return None

        return self.locus_construction_method(*rest_of_components)
