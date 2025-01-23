from decimal import Decimal
from typing import List, Mapping, Tuple, Optional

from ...embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from .embedded_construction import EmbeddedConstruction


class Midpoint(EmbeddedConstruction[Tuple[EmbeddedPoint, EmbeddedPoint], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        (point0, point1) = self.get_parameters(embedded_objects)
        return (point0 + point1).scale(Decimal('0.5'))
