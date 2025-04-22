from dataclasses import dataclass
from typing import Callable, Optional, Sequence, Tuple, Union, Unpack

from .....geometry_objects.geo_object import GeoObject
from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate

from ...construction_patterns.locus_patterns.locus_pattern_matcher import LocusPattern
from ...embedded_geo_objects.embedded_geo_object import EmbeddedGeoObject, ExtendedGeoObject

from .unpacking_predicate_locus import unpack_index_options


@dataclass
class EqualConstructionsLocus(LocusPattern):
    locus_construction_method: Callable[[Unpack[Tuple[ExtendedGeoObject, ...]]], EmbeddedGeoObject]
    first_construction_name: str
    first_construction_index_options: Union[int, Sequence[int], None]
    second_construction_name: str
    second_construction_index_options: Union[int, Sequence[int], None]
    
    def match(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]:
        if predicate.name != 'equals':
            return None
        lhs, rhs = predicate.components
        if not isinstance(lhs, ConstructionObject) or not isinstance(rhs, ConstructionObject):
            return None
        if lhs.constructor.name != self.first_construction_name:
            lhs, rhs = rhs, lhs
        if lhs.constructor.name != self.first_construction_name or rhs.constructor.name != self.second_construction_name:
            return None
        
        for lhs_index in unpack_index_options(self.first_construction_index_options, len(lhs.components)):
            for rhs_index in unpack_index_options(self.second_construction_index_options, len(rhs.components)):
                result = self.match_construction_index_options(object_, lhs, lhs_index, rhs, rhs_index)
                if result is not None:
                    return result

        return None
        

    def match_construction_index_options(
        self,
        object_: GeoObject,
        lhs: ConstructionObject,
        lhs_index: int,
        rhs: ConstructionObject,
        rhs_index: int
    ) -> Optional[ExtendedGeoObject]:
        if lhs.constructor.name != self.first_construction_name:
            return None
        
        if rhs.constructor.name != self.second_construction_name:
            return None
        
        if object_ != lhs.components[lhs_index]:
            return None
        
        if object_ != rhs.components[rhs_index]:
            return None
        
        rest_of_lhs_components = [lhs.components[i] for i in range(len(lhs.components)) if i != lhs_index]
        rest_of_rhs_components = [rhs.components[i] for i in range(len(rhs.components)) if i != rhs_index]
        
        if any([object_ in component.involved_objects() for component in rest_of_lhs_components + rest_of_rhs_components]):
            return None
        
        return self.locus_construction_method(*rest_of_lhs_components, *rest_of_rhs_components)
