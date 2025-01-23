from typing import List, Mapping, Tuple, Optional

from ...embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine

from .embedded_construction import EmbeddedConstruction

from .intersections.line_intersection import intersect


def project(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedPoint:
    orthogonal_direction = EmbeddedPoint(line.direction.y, -line.direction.x)
    altitude = EmbeddedLine(point, orthogonal_direction)
    return intersect(altitude, line)


class Projection(EmbeddedConstruction[Tuple[EmbeddedPoint, EmbeddedLine], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        (point, line) = self.get_parameters(embedded_objects)
        return project(point, line)
