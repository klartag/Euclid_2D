from typing import List

from .pattern import PredicatePreprocessingPattern

from .pattern_implementations.open_predicate_remover import OpenPredicateRemovalPattern
from .pattern_implementations.in_predicate_splitter import InPredicateSplitter
from .pattern_implementations.curve_equality_deconstruction import CurveEqualityDeconstructor


PREPROCESSING_PATTERNS: List[PredicatePreprocessingPattern] = [
    OpenPredicateRemovalPattern(),
    InPredicateSplitter(),
    CurveEqualityDeconstructor()
]
