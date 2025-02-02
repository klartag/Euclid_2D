from typing import List

from ....rule_utils import POINT, LINE, CIRCLE

from ...constructions import (
    internal_angle_bisector,
    external_angle_bisector,
    center,
    line_circle_other_intersection,
    circle_circle_other_intersection,
    circumcircle,
    line,
    line_intersection,
    line_on_point,
    midpoint,
    new_point,
    new_line,
    new_circle,
    point_on_line,
    point_on_circle,
    parallel_line,
    perpendicular_bisector,
    project,
)

from .construction_pattern import ConstructionPattern
from .explicit_construction_pattern import ExplicitConstructionPattern
from .containment_pattern import ContainmentPattern
from .reverse_containment_pattern import ReverseContainmentPattern

from .empty_pattern import EmptyPattern

from ..embedded_constructions.explicit_embedded_construction import ExplicitEmbeddedConstruction
from ..embedded_constructions.other_intersection_embedded_construction import OtherIntersectionEmbeddedConstruction


CONSTRUCTION_PATTERNS: List[ConstructionPattern] = [
    EmptyPattern(POINT, new_point),
    EmptyPattern(LINE, new_line),
    EmptyPattern(CIRCLE, new_circle),
    ContainmentPattern((LINE,), ExplicitEmbeddedConstruction, point_on_line),
    ContainmentPattern((CIRCLE,), ExplicitEmbeddedConstruction, point_on_circle),
    ContainmentPattern((LINE, LINE), ExplicitEmbeddedConstruction, line_intersection),
    ContainmentPattern((LINE, CIRCLE), OtherIntersectionEmbeddedConstruction, line_circle_other_intersection),
    ContainmentPattern((CIRCLE, CIRCLE), OtherIntersectionEmbeddedConstruction, circle_circle_other_intersection),
    ReverseContainmentPattern(1, LINE, ExplicitEmbeddedConstruction, line_on_point),
    ReverseContainmentPattern(2, LINE, ExplicitEmbeddedConstruction, line),
    ReverseContainmentPattern(3, CIRCLE, ExplicitEmbeddedConstruction, circumcircle),
    ExplicitConstructionPattern('Line', line),
    ExplicitConstructionPattern('Circle', circumcircle),
    ExplicitConstructionPattern('line_intersection', line_intersection),
    ExplicitConstructionPattern('line_circle_other_intersection', line_circle_other_intersection),
    ExplicitConstructionPattern('circle_circle_other_intersection', circle_circle_other_intersection),
    ExplicitConstructionPattern('internal_angle_bisector', internal_angle_bisector),
    ExplicitConstructionPattern('external_angle_bisector', external_angle_bisector),
    ExplicitConstructionPattern('perpendicular_bisector', perpendicular_bisector),
    ExplicitConstructionPattern('center', center),
    ExplicitConstructionPattern('parallel_line', parallel_line),
    ExplicitConstructionPattern('projection', project),
    ExplicitConstructionPattern('midpoint', midpoint),
]
