from typing import List, Optional

from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


DECONSTRUCTABLE_CONSTRUCTION_NAMES = ['Line', 'Circle']


class CurveEqualityDeconstructor(PredicatePreprocessingPattern):
    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name != 'equals':
            return None
        if len(predicate.components) != 2:
            return None
        
        lhs, rhs = predicate.components
        if isinstance(rhs, ConstructionObject) and rhs.constructor.name in DECONSTRUCTABLE_CONSTRUCTION_NAMES:
            lhs, rhs = rhs, lhs
        
        if not isinstance(lhs, ConstructionObject):
            return None
        if lhs.constructor.name not in DECONSTRUCTABLE_CONSTRUCTION_NAMES:
            return None

        return [predicate_from_args('in', (point, rhs)) for point in lhs.components]
