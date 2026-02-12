from typing import List, Optional

from .....geometry_objects.geo_type import GeoType
from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


class InPredicateSplitter(PredicatePreprocessingPattern):
    '''
    Splits an `in` predicate that contains multiple objects into a list of `in` predicates, each containing two parameters.
    
    For example, if A, B, C are points, and j, k, l are lines,
    splits the predicate
    A, B, C in j, k, l
    Into the nine predicates
    A in j, B in j, C in j,
    A in k, B in k, C in k,
    A in l, B in l, C in l.
    '''

    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name != 'in':
            return None

        for i in range(len(predicate.components) - 1):
            if predicate.components[i].type != GeoType.POINT and predicate.components[i + 1].type == GeoType.POINT:
                return None

        point_indices = [i for i in range(len(predicate.components)) if predicate.components[i].type == GeoType.POINT]
        curve_indices = [i for i in range(len(predicate.components)) if predicate.components[i].type != GeoType.POINT]

        containment_predicates = []
        for i in point_indices:
            for j in curve_indices:
                containment_predicates.append(
                    predicate_from_args('in', (predicate.components[i], predicate.components[j]))
                )
        return containment_predicates
