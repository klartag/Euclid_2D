from decimal import Decimal
from typing import List, Mapping, Tuple, Optional

from ....embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedLine, EmbeddedCircle

from ..embedded_construction import EmbeddedConstruction

from .line_circle_other_intersection import reflect


class CircleCircleOtherIntersection(EmbeddedConstruction[Tuple[EmbeddedCircle, EmbeddedCircle], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        (circle0, circle1) = self.get_parameters(embedded_objects)

        distinct_points = [embedded_objects.get(name, None) for name in distinct_names.get(self.output_name, [])]
        distinct_points = [p for p in distinct_points if isinstance(p, EmbeddedPoint)]

        distinct_points_in_intersection = [
            p for p in distinct_points if circle0.contains_point(p) and circle1.contains_point(p)
        ]

        if len(distinct_points_in_intersection) != 1:
            return None

        if circle0.center.is_equal(circle1.center):
            return None

        symmetry_line = EmbeddedLine(circle0.center, circle1.center - circle0.center)

        other_intersection = reflect(distinct_points_in_intersection[0], symmetry_line)

        if other_intersection.is_equal(distinct_points_in_intersection[0]):
            return None

        return other_intersection
