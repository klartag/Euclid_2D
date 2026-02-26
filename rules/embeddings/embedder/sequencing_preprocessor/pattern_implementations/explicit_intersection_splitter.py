from typing import List, Optional, cast

from .....geometry_objects.geo_object import GeoObject
from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


EXPLICIT_INTERSECTION_PREDICATE_NAMES = [
    'line_intersection',
    'line_line_intersection',
    'line_circle_intersection'
]

EXPLICIT_OTHER_INTERSECTION_PREDICATE_NAMES = [
    'line_line_other_intersection',
    'line_circle_other_intersection'
]


class ExplicitIntersectionSplitter(PredicatePreprocessingPattern):
    """
    Splits an equality between a Point object and an intersection between curves,
    into `in` predicates that define the intersection.
    
    For example, splits the predicate
    `A == line_circle_other_intersection(B, l, c)`
    into
    `A in l` and `A in c`.
    """

    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name != 'equals' or len(predicate.components) != 2:
            return None

        lhs, rhs = predicate.components
        if self.is_explicit_intersection_object(lhs):
            lhs, rhs = rhs, lhs
        if not self.is_explicit_intersection_object(rhs):
            return None
        
        containing_components = self.extract_containing_components(cast(ConstructionObject, rhs))
        return [predicate_from_args('in', (lhs, component)) for component in containing_components]

    def is_explicit_intersection_object(self, obj: GeoObject) -> bool:
        """Returns whether a construction object is defined as an intersection of some other GeoObjects."""
        if not isinstance(obj, ConstructionObject):
            return False
        return obj.constructor.name in EXPLICIT_INTERSECTION_PREDICATE_NAMES or \
            obj.constructor.name in EXPLICIT_OTHER_INTERSECTION_PREDICATE_NAMES

    def extract_containing_components(self, obj: ConstructionObject) -> List[GeoObject]:
        """
        Given a construction object that is defined as an intersection of some other GeoObjects,
        returns the objects whose intersection it is defining.
        
        (This is pretty much just the list of parameters of the construction,
        but in the case of the constructions whose names are in `EXPLICIT_OTHER_INTERSECTION_PREDICATE_NAMES`,
        the first parameter must be ignored.)
        """
        if obj.constructor.name in EXPLICIT_OTHER_INTERSECTION_PREDICATE_NAMES:
            return obj.components[1:]
        else:
            return obj.components
