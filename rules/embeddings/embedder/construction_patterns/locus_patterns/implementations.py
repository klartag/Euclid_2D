from typing import Callable, List, Optional, Tuple, Unpack

from .locus_pattern_matcher import LocusPattern
from .explicit_locus import ExplicitLocus
from .simple_predicate_locus import SimplePredicateLocus
from .simple_construction_predicate_locus import SimplePredicateConstructionLocus

from .....geometry_objects.geo_object import GeoObject
from .....geometry_objects.construction_object import ConstructionObject

construct = ConstructionObject.from_args

def construction_generator(construction_name: str, parameter_order: Optional[Tuple[int]]=None) -> Callable[[Unpack[Tuple[GeoObject, ...]]], GeoObject]:
    if parameter_order is None:
        return lambda *args: construct(construction_name, args)
    else:
        return lambda *args: construct(construction_name, tuple(args[i] for i in parameter_order))

LOCUS_PATTERNS: List[LocusPattern] = [
    ExplicitLocus(),
    SimplePredicateLocus(construction_generator('Line'), 'collinear', None),
    SimplePredicateLocus(construction_generator('Line'), 'between', None),
    SimplePredicateLocus(construction_generator('Line'), 'collinear_and_not_between', None),
    SimplePredicateLocus(construction_generator('Circle'), 'concyclic', None),
    SimplePredicateLocus(construction_generator('perpendicular_bisector'), 'isosceles_triangle', 0),
    SimplePredicateLocus(construction_generator('circle_from_center_and_point'), 'isosceles_triangle', [1, 2]),
    SimplePredicateConstructionLocus(
        construction_generator('perpendicular_line'),
        'perpendicular', None, 'Line', None
     ),
    SimplePredicateConstructionLocus(
        construction_generator('point_circle_tangent_line'),
        'tangent', 0, 'Line', None
    ),
    SimplePredicateConstructionLocus(
        construction_generator('circle_from_center_and_radius'),
        'equals', None, 'distance', None
    ),
    SimplePredicateConstructionLocus(
        lambda point1, point2, angle: construct('Line', (point1, construct('rotate_point', (point1, point2, -angle)))),
        'equals_mod_360', None, 'angle', 0
    ),
    SimplePredicateConstructionLocus(
        construction_generator('circle_from_two_points_and_angle'),
        'equals_mod_360', None, 'angle', 1
    ),
    SimplePredicateConstructionLocus(
        lambda point0, point1, angle: construct('Line', (point1, construct('rotate_point', (point1, point0, angle)))),
        'equals_mod_360', None, 'angle', 2
    ),
]
