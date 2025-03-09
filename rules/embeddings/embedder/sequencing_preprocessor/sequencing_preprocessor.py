from typing import List, Optional

from ....geometry_objects.construction_object import ConstructionObject

from ....predicates.predicate import Predicate
from ....predicates.predicate_factory import predicate_from_args

from .implementations import PREPROCESSING_PATTERNS


class SequencingPreprocessor:
    def preprocess_assumptions(self, predicates: List[Predicate]) -> List[Predicate]:
        processed_predicates = []
        for predicate in predicates:
            for preprocess_pattern in PREPROCESSING_PATTERNS:
                pattern_match_attempt = preprocess_pattern.try_match(predicate)
                if pattern_match_attempt is not None:
                    processed_predicates.extend(pattern_match_attempt)
                    break
            else:
                processed_predicates.append(predicate)
        return processed_predicates
