from typing import List, Optional

from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


COLLINEAR_INEQUALITY_PREDICATE_NAMES = ['between', 'collinear_and_not_between']


class CollinearInequalityRemover(PredicatePreprocessingPattern):
    """
    If a predicate is an inequality predicate relating to collinear points,
    (i.e. those whose names are in `COLLINEAR_INEQUALITY_PREDICATE_NAMES`),
    removes them.
    """

    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name in COLLINEAR_INEQUALITY_PREDICATE_NAMES:
            return [
                predicate_from_args('collinear', tuple(predicate.components[i : i + 3]))
                for i in range(len(predicate.components) - 2)
            ]
        else:
            return None
