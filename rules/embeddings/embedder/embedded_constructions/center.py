from typing import List, Mapping, Tuple, Optional

from ...embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedCircle

from .embedded_construction import EmbeddedConstruction


class Center(EmbeddedConstruction[Tuple[EmbeddedCircle], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        (circle,) = self.get_parameters(embedded_objects)
        return circle.center
