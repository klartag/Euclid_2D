from typing import List, Optional

from .....rule_utils import POINT
from .....predicates.predicate import Predicate
from .....predicates.predicate_factory import predicate_from_args

from ..pattern import PredicatePreprocessingPattern


COLLINEAR_INEQUALITY_PREDICATE_NAMES = ['between', 'collinear_and_not_between']


class CollinearInequalityRemover(PredicatePreprocessingPattern):
    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        if predicate.name in COLLINEAR_INEQUALITY_PREDICATE_NAMES:
            return predicate_from_args('collinear', [component.clone() for component in predicate.components])
        else:
            return None
