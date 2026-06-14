from typing import List, Optional
from .....predicates.predicate import Predicate

from ..pattern import PredicatePreprocessingPattern


class OpenPredicateRemovalPattern(PredicatePreprocessingPattern):
    """
    If a predicate is open, removes it.
    """

    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.is_open():
            return []
        else:
            return None
