from dataclasses import dataclass
from typing import Dict

from ....rule_utils import POINT, LINE, CIRCLE

from ...types import ConstructionMethod, ExtendedConstructionMethod, normalize_return_type
from ...constructions.circle_intersection import line_circle_intersection, circle_circle_intersection

@dataclass
class ConstructionData:
    type: str
    method: ConstructionMethod


EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY: Dict[str, ConstructionData] = {
    'line_circle_intersection': (POINT, line_circle_intersection),
    'circle_circle_intersection': (POINT, circle_circle_intersection),
}
