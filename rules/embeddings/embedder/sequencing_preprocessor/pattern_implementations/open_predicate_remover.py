from typing import List, Optional
from .....predicates.predicate import Predicate

from ..pattern import PredicatePreprocessingPattern


class OpenPredicateRemovalPattern(PredicatePreprocessingPattern):
    """
    TODO: Document
    """

    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.is_open():
            return []
        else:
            return None
