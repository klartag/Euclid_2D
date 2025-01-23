from decimal import Decimal
from typing import List, Mapping, Tuple, Optional
from random import normalvariate

from ....embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from ..embedded_construction import EmbeddedConstruction


class PointOnLine(EmbeddedConstruction[Tuple[EmbeddedLine], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        (line,) = self.get_parameters(embedded_objects)

        return line.point + line.direction.scale(Decimal(normalvariate(0, 10)))
