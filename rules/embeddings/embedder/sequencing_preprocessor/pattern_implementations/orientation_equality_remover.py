from typing import List, Optional

from rules.geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate

from ..pattern import PredicatePreprocessingPattern


class OrientationEqualityRemover(PredicatePreprocessingPattern):
    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name not in ['equals', 'equals_mod_360', 'identical']:
            return None
        for component in predicate.components:
            if not isinstance(component, ConstructionObject):
                return None
            if component.constructor.name != 'orientation':
                return None
        return []
