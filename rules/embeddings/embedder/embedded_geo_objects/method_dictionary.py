from dataclasses import dataclass
from typing import Dict

from ....rule_utils import POINT, LINE, CIRCLE

from ...types import ConstructionMethod, ExtendedConstructionMethod, normalize_return_type


@dataclass
class ConstructionData:
    type: str
    method: ConstructionMethod


EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY: Dict[str, ConstructionData] = [
    
]
