from typing import List

from ....rule_utils import POINT, LINE, CIRCLE

from ... import CONSTRUCTION_METHOD_DICTIONARY

from ...method_dictionaries import (
    line_circle_other_intersection,
    circle_circle_other_intersection,
    circumcircle,
    line,
    line_intersection,
    line_on_point,
    new_point,
    new_line,
    new_circle,
    point_on_line,
    point_on_circle,
)

from .construction_pattern import ConstructionPattern
from .explicit_construction_pattern import ExplicitConstructionPattern
from .containment_pattern import ContainmentPattern
from .reverse_containment_pattern import ReverseContainmentPattern
from .simple_symmetric_predicate_pattern import SimpleSymmetricPredicatePattern

from .empty_pattern import EmptyPattern

from ..embedded_constructions.explicit_embedded_construction import ExplicitEmbeddedConstruction
from ..embedded_constructions.other_intersection_embedded_construction import OtherIntersectionEmbeddedConstruction


CONSTRUCTION_PATTERNS: List[ConstructionPattern] = [
    EmptyPattern(POINT, new_point),
    EmptyPattern(LINE, new_line),
    EmptyPattern(CIRCLE, new_circle),
    ReverseContainmentPattern(1, LINE, ExplicitEmbeddedConstruction, line_on_point),
    ReverseContainmentPattern(2, LINE, ExplicitEmbeddedConstruction, line),
    ReverseContainmentPattern(3, CIRCLE, ExplicitEmbeddedConstruction, circumcircle),
    SimpleSymmetricPredicatePattern(
        ExplicitEmbeddedConstruction,
        lambda line0, line1: line_on_point(line_intersection(line0, line1)),
        'concurrent'
    ),
] + [
    ExplicitConstructionPattern(construction_name, construction_method)
    for (construction_name, construction_method) in CONSTRUCTION_METHOD_DICTIONARY.items()
] + [
    ContainmentPattern((LINE,), ExplicitEmbeddedConstruction, point_on_line),
    ContainmentPattern((CIRCLE,), ExplicitEmbeddedConstruction, point_on_circle),
    ContainmentPattern((LINE, LINE), ExplicitEmbeddedConstruction, line_intersection),
    ContainmentPattern((LINE, CIRCLE), OtherIntersectionEmbeddedConstruction, line_circle_other_intersection),
    ContainmentPattern((CIRCLE, CIRCLE), OtherIntersectionEmbeddedConstruction, circle_circle_other_intersection),
]
