from typing import List

from ....rule_utils import POINT, LINE, CIRCLE

from .construction_pattern import ConstructionPattern
from .explicit_construction_pattern import ExplicitConstructionPattern
from .intersection_pattern import IntersectionPattern
from .line_on_point_pattern import LineOnPointPattern
from .empty_pattern import EmptyPattern

from ..embedded_constructions import (
    Center,
    CircleCircleOtherIntersection,
    Circumcircle,
    ExternalAngleBisector,
    InternalAngleBisector,
    Line,
    LineCircleOtherIntersection,
    LineIntersection,
    Midpoint,
    NewCircle,
    NewLine,
    NewPoint,
    ParallelLine,
    PerpendicularBisector,
    PointOnCircle,
    PointOnLine,
    Projection,
)

CONSTRUCTION_PATTERNS: List[ConstructionPattern] = [
    EmptyPattern(POINT, NewPoint),
    EmptyPattern(LINE, NewLine),
    EmptyPattern(CIRCLE, NewCircle),
    IntersectionPattern((LINE,), PointOnLine),
    IntersectionPattern((CIRCLE,), PointOnCircle),
    IntersectionPattern((LINE, LINE), LineIntersection),
    IntersectionPattern((LINE, CIRCLE), LineCircleOtherIntersection),
    IntersectionPattern((CIRCLE, CIRCLE), CircleCircleOtherIntersection),
    LineOnPointPattern(),
    ExplicitConstructionPattern('Line', Line),
    ExplicitConstructionPattern('Circle', Circumcircle),
    ExplicitConstructionPattern('line_intersection', LineIntersection),
    ExplicitConstructionPattern('line_circle_other_intersection', LineCircleOtherIntersection),
    ExplicitConstructionPattern('circle_circle_other_intersection', CircleCircleOtherIntersection),
    ExplicitConstructionPattern('internal_angle_bisector', InternalAngleBisector),
    ExplicitConstructionPattern('external_angle_bisector', ExternalAngleBisector),
    ExplicitConstructionPattern('perpendicular_bisector', PerpendicularBisector),
    ExplicitConstructionPattern('center', Center),
    ExplicitConstructionPattern('parallel_line', ParallelLine),
    ExplicitConstructionPattern('projection', Projection),
    ExplicitConstructionPattern('midpoint', Midpoint),
]
