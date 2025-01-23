from typing import List, Mapping, Tuple, Optional

from ...embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from .embedded_construction import EmbeddedConstruction


class ExternalAngleBisector(EmbeddedConstruction[Tuple[EmbeddedPoint, EmbeddedPoint, EmbeddedPoint], EmbeddedLine]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedLine]:
        (point0, point1, point2) = self.get_parameters(embedded_objects)

        if point0.is_equal(point1) or point1.is_equal(point2):
            return None

        direction0 = (point0 - point1).normalize()
        direction1 = (point2 - point1).normalize()

        if direction0.is_equal(direction1):
            orthogonal_direction = EmbeddedPoint(direction0.y, -direction0.x)
            return EmbeddedLine(point1, orthogonal_direction)
        else:
            return EmbeddedLine(point1, direction0 - direction1)
