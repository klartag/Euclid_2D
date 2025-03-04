from typing import Dict

from .constructions.angle_bisectors import internal_angle_bisector, external_angle_bisector
from .constructions.center import center
from .constructions.circle import circumcenter, circumcircle, circle_from_center_and_point, circle_from_center_and_radius, circle_from_two_points_and_angle
from .constructions.circle_intersection import line_circle_other_intersection, circle_circle_other_intersection
from .constructions.incenters import incenter, excenter, incircle, excircle
from .constructions.isogonal_conjugate import isogonal_conjugate
from .constructions.line import line
from .constructions.line_intersection import line_intersection
from .constructions.midpoint import midpoint, median, centroid
from .constructions.new_object import new_point, new_line, new_circle
from .constructions.nine_point_circle import nine_point_circle
from .constructions.object_on_object import point_on_line, line_on_point, point_on_circle
from .constructions.parallels_and_perpendiculars import parallel_line, perpendicular_line, perpendicular_bisector, altitude, orthocenter
from .constructions.projection import project
from .constructions.radical_axis import radical_axis
from .constructions.reflection import reflect_point
from .constructions.rotation import rotate_point
from .constructions.scalars import angle, orientation, distance, direction, power_of_a_point, radius, log
from .constructions.tangent import tangent_point, tangent_line

from .predicates.bisect import bisect
from .predicates.collinear import collinear, between, collinear_and_not_between, not_collinear
from .predicates.concurrent import concurrent
from .predicates.concyclic import concyclic
from .predicates.containment import _in, not_in
from .predicates.convex import convex
from .predicates.equality import equals, equals_mod_360, not_equals, not_equals_mod_360, distinct, identical, not_one_of
from .predicates.exists import exists
from .predicates.line_relations import parallel, perpendicular
from .predicates.quadrilaterals import trapezoid, isosceles_trapezoid, parallelogram, rhombus, rectangle, square
from .predicates.tangent import tangent
from .predicates.triangles import isosceles_triangle, congruent_triangles, anti_congruent_triangles, similar_triangles, anti_similar_triangles

from .types import ConstructionMethod, PredicateMethod, normalize_return_type


CONSTRUCTION_METHOD_DICTIONARY: Dict[str, ConstructionMethod] = {
    name: normalize_return_type(func) for name, func in {
        'altitude': altitude,
        'angle': angle,
        'center': center,
        'centroid': centroid,
        'circle_circle_other_intersection': circle_circle_other_intersection,
        'Circle': circumcircle,
        'circle_from_center_and_point': circle_from_center_and_point,
        'circle_from_center_and_radius': circle_from_center_and_radius,
        'circle_from_two_points_and_angle': circle_from_two_points_and_angle,
        'circumcenter': circumcenter,
        'direction': direction,
        'distance': distance,
        'excenter': excenter,
        'excircle': excircle,
        'external_angle_bisector': external_angle_bisector,
        'incenter': incenter,
        'incircle': incircle,
        'internal_angle_bisector': internal_angle_bisector,
        'isogonal_conjugate': isogonal_conjugate,
        'line_circle_other_intersection': line_circle_other_intersection,
        'line_circle_tangent_point': tangent_point,
        'line_intersection': line_intersection,
        'Line': line,
        'log': log,
        'median': median,
        'midpoint': midpoint,
        'nine_point_circle': nine_point_circle,
        'orientation': orientation,
        'orthocenter': orthocenter,
        'parallel_line': parallel_line,
        'perpendicular_bisector': perpendicular_bisector,
        'perpendicular_line': perpendicular_line,
        'point_circle_tangent_line': tangent_line,
        'power_of_a_point': power_of_a_point,
        'projection': project,
        'radical_axis': radical_axis,
        'radius': radius,
        'rotate_point': rotate_point,
    }.items()
}

PREDICATE_METHOD_DICTIONARY: Dict[str, PredicateMethod] = {
    'anti_congruent_triangles': anti_congruent_triangles,
    'anti_similar_triangles': anti_similar_triangles,
    'between': between,
    'bisect': bisect,
    'collinear_and_not_between': collinear_and_not_between,
    'collinear': collinear,
    'concurrent': concurrent,
    'concyclic': concyclic,
    'congruent_triangles': congruent_triangles,
    'convex': convex,
    'distinct': distinct,
    'equals_mod_360': equals_mod_360,
    'equals': equals,
    'exists': exists,
    'identical': identical,
    'in': _in,
    'isosceles_trapezoid': isosceles_trapezoid,
    'isosceles_triangle': isosceles_triangle,
    'not_collinear': not_collinear,
    'not_equals_mod_360': not_equals_mod_360,
    'not_equals': not_equals,
    'not_in': not_in,
    'not_one_of': not_one_of,
    'parallel': parallel,
    'parallelogram': parallelogram,
    'perpendicular': perpendicular,
    'probably_between': between,
    'rectangle': rectangle,
    'rhombus': rhombus,
    'similar_triangles': similar_triangles,
    'square': square,
    'tangent': tangent,
    'trapezoid': trapezoid,
    'triangle': not_collinear,
}
