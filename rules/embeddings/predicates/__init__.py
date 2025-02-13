from typing import Callable, Dict, Tuple, Unpack

from ..embedded_objects import EmbeddedObject

from .collinear import collinear, between, collinear_and_not_between
from .concurrent import concurrent
from .concyclic import concyclic
from .equality import equals, equals_mod_360
from .bisect import bisect
from .line_relations import parallel, perpendicular
from .triangles import isosceles_triangle, congruent_triangles, anti_congruent_triangles, similar_triangles, anti_similar_triangles


PREDICATE_METHOD_DICTIONARY: Dict[str, Callable[[Unpack[Tuple[EmbeddedObject, ...]]], bool]] = {
    'collinear': collinear,
    'concurrent': concurrent,
    'concyclic': concyclic,
    'equals': equals,
    'equals_mod_360': equals_mod_360,
    
    'between': between,
    'collinear_and_not_between': collinear_and_not_between,
    'bisect': bisect,
    'parallel': parallel,
    'perpendicular': perpendicular,

    'isosceles_triangle': isosceles_triangle,
    'congruent_triangles': congruent_triangles,
    'anti_congruent_triangles': anti_congruent_triangles,
    'similar_triangles': similar_triangles,
    'anti_similar_triangles': anti_similar_triangles,
}

'''
Predicates remaining:

* some very atomic predicates

* trapezoid
* isosceles_trapezoid
* parallelogram
* rhombus
* rectangle
* square
'''
