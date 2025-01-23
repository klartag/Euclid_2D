from typing import List, Mapping, Tuple, Optional

from ....embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from ..embedded_construction import EmbeddedConstruction


def intersect(line0: EmbeddedLine, line1: EmbeddedLine) -> Optional[EmbeddedPoint]:
    if line0.direction.is_proportional(line1.direction):
        return None
    delta = line1.point - line0.point
    determinant = line0.direction.x * line1.direction.y - line0.direction.y * line1.direction.x
    t = (delta.x * line1.direction.y - delta.y * line1.direction.x) / determinant
    return line0.point + line0.direction.scale(t)


class LineIntersection(EmbeddedConstruction[Tuple[EmbeddedLine, EmbeddedLine], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        (line0, line1) = self.get_parameters(embedded_objects)
        return intersect(line0, line1)
