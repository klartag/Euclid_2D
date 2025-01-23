from typing import List, Mapping, Tuple, Optional

from ....embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from ..embedded_construction import EmbeddedConstruction

from .new_point import random_point


class LineOnPoint(EmbeddedConstruction[Tuple[EmbeddedPoint], EmbeddedLine]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedLine]:
        (point,) = self.get_parameters(embedded_objects)
        return EmbeddedLine(point, random_point())
