from typing import List, Optional

from .....geometry_objects.geo_object import GeoObject
from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


# TODO: Document
DECONSTRUCTABLE_CONSTRUCTION_NAMES = ['Line', 'Circle']


class CurveEqualityDeconstructor(PredicatePreprocessingPattern):
    """
    TODO: Document
    """

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
        """
        TODO: Document
        """
        return isinstance(obj, ConstructionObject) and obj.constructor.name in DECONSTRUCTABLE_CONSTRUCTION_NAMES
