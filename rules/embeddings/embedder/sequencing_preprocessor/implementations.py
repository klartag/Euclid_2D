from typing import List

from .pattern import PredicatePreprocessingPattern
from .pattern_implementations.open_predicate_remover import OpenPredicateRemovalPattern
from .pattern_implementations.distinct_splitter import DistinctPredicateSplitter
from .pattern_implementations.in_predicate_splitter import InPredicateSplitter
from .pattern_implementations.curve_equality_deconstruction import CurveEqualityDeconstructor
from .pattern_implementations.collinear_inequality_remover import CollinearInequalityRemover
from .pattern_implementations.explicit_intersection_splitter import ExplicitIntersectionSplitter

SPLITTING_PATTERNS: List[PredicatePreprocessingPattern] = [
    DistinctPredicateSplitter(),
    InPredicateSplitter(),
    CurveEqualityDeconstructor(),
    ExplicitIntersectionSplitter()
]

INEQUALITY_REMOVAL_PATTERNS: List[PredicatePreprocessingPattern] = [
    OpenPredicateRemovalPattern(),
    CollinearInequalityRemover(),
]
