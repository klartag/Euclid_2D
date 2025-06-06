from typing import List, Optional

from .....geometry_objects.construction_object import ConstructionObject
from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


class RectangleSplitter(PredicatePreprocessingPattern):
    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name != 'rectangle':
            return None
        
        lines = [ConstructionObject.from_args('Line', (predicate.components[i], predicate.components[(i + 1) % 4])) for i in range(4)]
        
        return [predicate_from_args('perpendicular', (lines[i], lines[(i + 1) % 4])) for i in range(4)]
