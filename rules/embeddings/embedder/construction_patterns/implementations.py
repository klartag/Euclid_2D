from typing import List

from ....rule_utils import POINT, LINE, CIRCLE

from ...constructions import (
    internal_angle_bisector,
    external_angle_bisector,
    center,
    line_circle_other_intersection,
    circle_circle_other_intersection,
    circumcircle,
    line_intersection,
    line,
    midpoint,
    new_point,
    new_line,
    new_circle,
    point_on_line,
    line_on_point,
    point_on_circle,
    parallel_line,
    perpendicular_bisector,
    projection,
    reflection
)

from .construction_pattern import ConstructionPattern
from .explicit_construction_pattern import ExplicitConstructionPattern
from .intersection_pattern import IntersectionPattern
from .line_on_point_pattern import LineOnPointPattern
from .empty_pattern import EmptyPattern


CONSTRUCTION_PATTERNS: List[ConstructionPattern] = [
    EmptyPattern(POINT, new_point),
    EmptyPattern(LINE, new_line),
    EmptyPattern(CIRCLE, new_circle),
    IntersectionPattern((LINE,), point_on_line),
    IntersectionPattern((CIRCLE,), point_on_circle),
    IntersectionPattern((LINE, LINE), line_intersection),
    IntersectionPattern((LINE, CIRCLE), line_circle_other_intersection),
    IntersectionPattern((CIRCLE, CIRCLE), circle_circle_other_intersection),
    LineOnPointPattern(),
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
    ExplicitConstructionPattern('projection', projection),
    ExplicitConstructionPattern('midpoint', midpoint),
]
