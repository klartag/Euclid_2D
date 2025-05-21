from dataclasses import dataclass
from typing import Dict


from ....rule_utils import GeoType
from ....predicates.global_predicates import get_constructions

from ...types import ConstructionMethod, normalize_return_type
from ...constructions.circle_intersection import line_circle_intersection, circle_circle_intersection
from ...constructions.circle import (
    circle_from_center_and_point,
    circle_from_center_and_radius,
    circle_from_two_points_and_angle,
)
from ...constructions.polarity import polar, pole, line_from_origin
from ...constructions.rotation import rotate_point
from ...constructions.tangent import tangent_line


@dataclass
class ConstructionData:
    type: str
    method: ConstructionMethod

    def __post_init__(self):
        self.method = normalize_return_type(self.method)


_EMBEDDED_GEO_OBJECT_POINT_CONSTRUCTIONS: Dict[str, ConstructionMethod] = {
    'line_circle_intersection': line_circle_intersection,
    'circle_circle_intersection': circle_circle_intersection,
    'rotate_point': rotate_point,
    'pole': pole,
}

_EMBEDDED_GEO_OBJECT_LINE_CONSTRUCTIONS: Dict[str, ConstructionMethod] = {
    'tangent_line': tangent_line,
    'polar': polar,
    'line_from_origin': line_from_origin,
}

_EMBEDDED_GEO_OBJECT_CIRCLE_CONSTRUCTIONS: Dict[str, ConstructionMethod] = {
    'circle_from_center_and_point': circle_from_center_and_point,
    'circle_from_center_and_radius': circle_from_center_and_radius,
    'circle_from_two_points_and_angle': circle_from_two_points_and_angle,
}

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY: Dict[str, ConstructionData] = {}

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY.update(
    [
        (name, ConstructionData(GeoType.POINT, method))
        for (name, method) in _EMBEDDED_GEO_OBJECT_POINT_CONSTRUCTIONS.items()
    ]
)

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY.update(
    [
        (name, ConstructionData(GeoType.LINE, method))
        for (name, method) in _EMBEDDED_GEO_OBJECT_LINE_CONSTRUCTIONS.items()
    ]
)

EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY.update(
    [
        (name, ConstructionData(GeoType.CIRCLE, method))
        for (name, method) in _EMBEDDED_GEO_OBJECT_CIRCLE_CONSTRUCTIONS.items()
    ]
)

for name in EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY:
    if name in get_constructions():
        raise ValueError(
            f"Construction '{name}' is a real construction \
                and thus is not allowed to be in the EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY."
        )
