from typing import Callable, Dict, Optional, Tuple, Unpack

from ..embedded_objects import EmbeddedObject

from .angle_bisectors import internal_angle_bisector, external_angle_bisector
from .center import center
from .circle_intersection import line_circle_other_intersection, circle_circle_other_intersection
from .circumcircle import circumcircle
from .line_intersection import line_intersection
from .line import line
from .midpoint import midpoint
from .new_object import new_point, new_line, new_circle
from .object_on_object import point_on_line, line_on_point, point_on_circle
from .parallels_and_perpendiculars import parallel_line, perpendicular_bisector
from .projection import project
from .reflection import reflect
from .scalars import angle, orientation, distance, direction, power_of_a_point, radius


CONSTRUCTION_METHOD_DICTIONARY: Dict[str, Callable[[Unpack[Tuple[EmbeddedObject, ...]]], Optional[EmbeddedObject]]] = {
    'Line': line,
    'Circle': circumcircle,
    'line_intersection': line_intersection,
    'line_circle_other_intersection': line_circle_other_intersection,
    'circle_circle_other_intersection': circle_circle_other_intersection,
    'internal_angle_bisector': internal_angle_bisector,
    'external_angle_bisector': external_angle_bisector,
    'perpendicular_bisector': perpendicular_bisector,
    'center': center,
    'parallel_line': parallel_line,
    'projection': project,
    'midpoint': midpoint,
    
    'orientation': orientation,
    'angle': angle,
    'distance': distance,
    'direction': direction,
    'power_of_a_point': power_of_a_point,
    'radius': radius
}
