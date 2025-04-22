from abc import abstractmethod
from dataclasses import dataclass
from typing import Callable, Optional, Sequence, Tuple, Unpack, Union

from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate

from ...embedded_geo_objects.embedded_geo_object import EmbeddedGeoObject, ExtendedGeoObject

from .locus_pattern_matcher import LocusPattern


@dataclass
class UnpackingPredicateLocus(LocusPattern):
    locus_construction_method: Callable[[Unpack[Tuple[ExtendedGeoObject, ...]]], EmbeddedGeoObject]
    predicate_name: str
    parameter_index_options: Union[int, Sequence[int], None]

    def match(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]:
        for parameter_index in unpack_index_options(self.parameter_index_options, len(predicate.components)):
            locus = self.match_predicate_parameter_option(object_, predicate, parameter_index)
            if locus is not None:
                return locus
        return None

    @abstractmethod
    def match_predicate_parameter_option(self, object_: GeoObject, predicate: Predicate, parameter_index: int) -> Optional[ExtendedGeoObject]: ...

def unpack_index_options(parameter_index_options: Union[int, Sequence[int], None], component_count: int) -> Sequence[int]:
    if parameter_index_options is None:
        return list(range(component_count))
    elif isinstance(parameter_index_options, Sequence):
        return [i for i in parameter_index_options if i < component_count]
    else:
        return [parameter_index_options] if parameter_index_options < component_count else []