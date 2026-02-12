from typing import List, Optional

from .....geometry_objects.geo_object import GeoObject
from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


DECONSTRUCTABLE_CONSTRUCTION_NAMES = ['Line', 'Circle']


class CurveEqualityDeconstructor(PredicatePreprocessingPattern):
    '''
    Turns equalities of two objects where one of them is a `Line` or `Circle` construction,
    into a list of `in` predicates.
    
    For example, turns the predicate
    `Circle(A, B, C) == nine_point_circle(X, Y, Z)`
    into the three predicates
    `A in nine_point_circle(X, Y, Z)`, `B in nine_point_circle(X, Y, Z)`, `C in nine_point_circle(X, Y, Z)`.
    '''
    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name != 'equals' or len(predicate.components) != 2:
            return None
        
        lhs, rhs = predicate.components

        if self.is_deconstructable_object(rhs):
            lhs, rhs = rhs, lhs
        if not self.is_deconstructable_object(lhs):
            return None

        return [predicate_from_args('in', (point, rhs)) for point in lhs.components]
    
    def is_deconstructable_object(self, obj: GeoObject) -> bool:
        '''
        Checks whether an object is a construction object of a type that defines a curve passing through the points in its parameters.
        (i.e., an object whose name is in `DECONSTRUCTABLE_CONSTRUCTION_NAMES`.)
        '''
        return isinstance(obj, ConstructionObject) and obj.constructor.name in DECONSTRUCTABLE_CONSTRUCTION_NAMES
