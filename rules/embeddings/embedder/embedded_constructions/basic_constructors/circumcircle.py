from typing import List, Mapping, Tuple, Optional

from ....embedded_objects import EmbeddedObject, EmbeddedPoint, EmbeddedCircle

from ..embedded_construction import EmbeddedConstruction

from ..perpendicular_bisector import perpendicular_bisector
from ..intersections.line_intersection import intersect


class Circumcircle(EmbeddedConstruction[Tuple[EmbeddedPoint, EmbeddedPoint, EmbeddedPoint], EmbeddedCircle]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedCircle]:
        (point0, point1, point2) = self.get_parameters(embedded_objects)

        if point0.is_equal(point1) or point0.is_equal(point2) or point1.is_equal(point2):
            return None

        if (point1 - point0).is_proportional(point2 - point0):
            return None

        perpendicular_bisector0 = perpendicular_bisector(point0, point1)
        perpendicular_bisector1 = perpendicular_bisector(point0, point2)

        if perpendicular_bisector0 is None or perpendicular_bisector1 is None:
            return None

        center = intersect(perpendicular_bisector0, perpendicular_bisector1)

        if center is None:
            return None

        return EmbeddedCircle(center, (point0 - center).length_squared())
