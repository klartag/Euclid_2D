from dataclasses import dataclass
from typing import Dict

from ....rule_utils import POINT, LINE, CIRCLE

from ...types import ConstructionMethod, normalize_return_type
from ...constructions.circle_intersection import line_circle_intersection, circle_circle_intersection
from ...constructions.circle import circle_from_center_and_point, circle_from_center_and_radius, circle_from_two_points_and_angle


@dataclass
class ConstructionData:
    type: str
    method: ConstructionMethod
    
    def __post_init__(self):
        self.method = normalize_return_type(self.method)


_EMBEDDED_GEO_OBJECT_POINT_CONSTRUCTIONS: Dict[str, ConstructionMethod] = {
    'line_circle_intersection': line_circle_intersection,
    'circle_circle_intersection': circle_circle_intersection,
}

_EMBEDDED_GEO_OBJECT_LINE_CONSTRUCTIONS: Dict[str, ConstructionMethod] = {
    
}

_EMBEDDED_GEO_OBJECT_CIRCLE_CONSTRUCTIONS: Dict[str, ConstructionMethod] = {
    'circle_from_center_and_point': circle_from_center_and_point,
    'circle_from_center_and_radius': circle_from_center_and_radius,
    'circle_from_two_points_and_angle': circle_from_two_points_and_angle,
}

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY: Dict[str, ConstructionData] = { }

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY.update([
    (name, ConstructionData(POINT, method))
    for (name, method) in _EMBEDDED_GEO_OBJECT_POINT_CONSTRUCTIONS.items()
])

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY.update([
    (name, ConstructionData(LINE, method))
    for (name, method) in _EMBEDDED_GEO_OBJECT_LINE_CONSTRUCTIONS.items()
])

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY.update([
    (name, ConstructionData(CIRCLE, method))
    for (name, method) in _EMBEDDED_GEO_OBJECT_CIRCLE_CONSTRUCTIONS.items()
])
