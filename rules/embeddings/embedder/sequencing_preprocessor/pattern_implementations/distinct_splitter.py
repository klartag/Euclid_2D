from typing import List, Optional

from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


class DistinctPredicateSplitter(PredicatePreprocessingPattern):
    """
    TODO: Document
    """

    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name != 'distinct':
            return None

        inequality_predicates = []

        for i in range(len(predicate.components)):
            for j in range(i):
                inequality_predicates.append(
                    predicate_from_args('not_equals', (predicate.components[i], predicate.components[j]))
                )

        return inequality_predicates
