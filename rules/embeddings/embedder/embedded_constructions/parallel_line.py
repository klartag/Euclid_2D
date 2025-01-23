from typing import List, Mapping, Tuple, Optional

from ...embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from .embedded_construction import EmbeddedConstruction


class ParallelLine(EmbeddedConstruction[Tuple[EmbeddedPoint, EmbeddedLine], EmbeddedLine]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedLine]:
        (point, line) = self.get_parameters(embedded_objects)
        return EmbeddedLine(point, line.direction)
