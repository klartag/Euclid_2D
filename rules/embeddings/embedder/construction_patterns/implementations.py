from typing import List

from ....rule_utils import GeoType

from ...constructions.circle_intersection import line_circle_intersection, circle_circle_intersection
from ...method_dictionaries import (
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
from ..embedded_constructions.generalized_embedded_construction import GeneralizedEmbeddedConstruction


CONSTRUCTION_PATTERNS: List[ConstructionPattern] = [
    EmptyPattern(GeoType.POINT, new_point),
    EmptyPattern(GeoType.LINE, new_line),
    EmptyPattern(GeoType.CIRCLE, new_circle),
    # ReverseContainmentPattern(1, GeoType.LINE, GeneralizedEmbeddedConstruction, line_on_point),
    # ReverseContainmentPattern(2, GeoType.LINE, ExplicitEmbeddedConstruction, line),
    ReverseContainmentPattern(3, GeoType.CIRCLE, ExplicitEmbeddedConstruction, circumcircle),
    SimpleSymmetricPredicatePattern(
        GeneralizedEmbeddedConstruction,
        lambda objects, line0, line1: line_on_point(objects, line_intersection(line0, line1)),
        'concurrent',
    ),
    ExplicitConstructionPattern(),
    ContainmentPattern(),
]
