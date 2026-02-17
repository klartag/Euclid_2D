from dataclasses import dataclass
from typing import Optional

from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate

from .unpacking_predicate_locus import UnpackingPredicateLocus

from ...embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

@dataclass
class SimplePredicateLocus(UnpackingPredicateLocus):
    '''
    Knows to identify locii of objects defined by a predicate,
    where the object whose locus we are looking for is *equal* to one of the arguments of the predicate,
    and *does not at all appear* in any of the other arguments of the predicate.
    
    For example, instances of this class would know that
    *   The locus of all points `X` that satisfy `concyclic(A, B, C, X)`
        is the circumcircle of ABC.
    *   The locus of all points `X` that satisfy `isosceles_triangle(A, B, X)`
        is the circle whose center is A and that passes through B.
    '''

    def match_predicate_parameter_option(self, object_: GeoObject, predicate: Predicate, parameter_index: int) -> Optional[ExtendedGeoObject]:
        if predicate.name != self.predicate_name:
            return None

        if object_ != predicate.components[parameter_index]:
            return None

        rest_of_components = [predicate.components[i] for i in range(len(predicate.components)) if i != parameter_index]

        if any([object_ in component.involved_objects() for component in rest_of_components]):
            return None

        return self.locus_construction_method(*rest_of_components)
