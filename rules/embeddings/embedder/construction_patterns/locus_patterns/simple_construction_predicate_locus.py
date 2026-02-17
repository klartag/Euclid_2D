from dataclasses import dataclass
from typing import List, Optional, Sequence, Union

from .....geometry_objects.geo_object import GeoObject
from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate

from ...embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

from .unpacking_predicate_locus import UnpackingPredicateLocus, unpack_index_options


@dataclass
class SimplePredicateConstructionLocus(UnpackingPredicateLocus):
    '''
    Knows to identify locii of objects defined by a predicate,
    where the object whose locus we are looking for
    *does not at all appear* in every arguments of the predicate except for one.
    
    And that last argument is a `ConstructionObject`, where the object whose locus we are looking for
    *does not at all appear* in every arguments of the predicate except for one,
    and is *equal* to that last argument of the predicate.
    
    For example, instances of this class would know that
    *   The locus of all points `X` that satisfy `parallel(l, Line(A, X))`
        is the line passing through A parallel to l.
    *   The locus of all points `X` that satisfy `angle(A, X, B) == a mod 360`,
        is some circle passing through A and B (where the circle depends on the angle `a`).
    '''

    construction_name: str
    construction_index_options: Union[int, Sequence[int], None]

    def match_predicate_parameter_option(self, object_: GeoObject, predicate: Predicate, parameter_index: int) -> Optional[ExtendedGeoObject]:
        if predicate.name != self.predicate_name:
            return None

        rest_of_components = [predicate.components[i] for i in range(len(predicate.components)) if i != parameter_index]

        if any([object_ in component.involved_objects() for component in rest_of_components]):
            return None
        
        construction_object = predicate.components[parameter_index]
        if not isinstance(construction_object, ConstructionObject):
            return None
        
        construction_index_options = unpack_index_options(self.construction_index_options, len(construction_object.components))
        for construction_index in construction_index_options:
            locus = self.match_predicate_construction_parameter_options(object_, rest_of_components, construction_object, construction_index)
            if locus is not None:
                return locus
        else:
            return None


    def match_predicate_construction_parameter_options(
        self,
        object_: GeoObject,
        rest_of_predicate_components: List[GeoObject],
        construction_object: ConstructionObject,
        construction_index: int
    ) -> Optional[ExtendedGeoObject]:
        '''
        Identical to `match_predicate_parameter_option`, but attempts to match a specific case for the
        index of the ConstructionObject that `object_` exists in.
        
        object_:                        The object whose locus we want to find.
        rest_of_predicate_components:   The rest of the arguments to the `self.predicate_name` predicate defining the locus.
        construction_object:            The ConstructionObject in the last argument of the predicate.
        construction_index:             The index in which we are checking whether `object_` appears in `construction_object`.
        
        Returns:                        If there is a match for the pattern, calls `self.locus_construction_method`,
                                        inputting as parameters
                                        * The rest of the components in the ConstructionObject
                                        * The rest of the components in the predicate
                                        (in that order).
        '''
        if construction_object.constructor.name != self.construction_name:
            return None
        
        if object_ != construction_object.components[construction_index]:
            return None
        
        rest_of_construction_components = [construction_object.components[i] for i in range(len(construction_object.components)) if i != construction_index]
        
        if any([object_ in component.involved_objects() for component in rest_of_construction_components]):
            return None
        
        return self.locus_construction_method(*rest_of_construction_components, *rest_of_predicate_components)
