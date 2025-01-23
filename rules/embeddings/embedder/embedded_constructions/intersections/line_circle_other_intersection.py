from decimal import Decimal
from typing import List, Mapping, Tuple, Optional

from ....embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine, EmbeddedCircle

from ..embedded_construction import EmbeddedConstruction
from ..projection import project


def reflect(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedPoint:
    projection = project(point, line)
    return point + (projection - point).scale(Decimal(2))


class LineCircleOtherIntersection(EmbeddedConstruction[Tuple[EmbeddedLine, EmbeddedCircle], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        (line, circle) = self.get_parameters(embedded_objects)

        distinct_points = [embedded_objects.get(name, None) for name in distinct_names.get(self.output_name, [])]
        distinct_points = [p for p in distinct_points if isinstance(p, EmbeddedPoint)]

        distinct_points_in_intersection = [
            p for p in distinct_points if line.contains_point(p) and circle.contains_point(p)
        ]

        if len(distinct_points_in_intersection) != 1:
            return None

        orthogonal_direction = EmbeddedPoint(line.direction.y, -line.direction.x)
        symmetry_line = EmbeddedLine(circle.center, orthogonal_direction)

        other_intersection = reflect(distinct_points_in_intersection[0], symmetry_line)

        if other_intersection.is_equal(distinct_points_in_intersection[0]):
            return None

        return other_intersection
