from typing import List, Mapping, Tuple, Optional

from ....embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from ..embedded_construction import EmbeddedConstruction


class Line(EmbeddedConstruction[Tuple[EmbeddedPoint, EmbeddedPoint], EmbeddedLine]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedLine]:
        (point0, point1) = self.get_parameters(embedded_objects)
        if point0.is_equal(point1):
            return None
        return EmbeddedLine(point0, point1 - point0)
