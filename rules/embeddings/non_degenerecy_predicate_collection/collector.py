from decimal import Decimal
from typing import List
from itertools import combinations

from ...geometry_objects.geo_object import GeoObject
from ...rule_utils import LITERAL

from ..embedded_objects import Embedding, EmbeddedPoint

from ...predicates.predicate import Predicate
from ...predicates.predicate_factory import predicate_from_args
from ...geometry_objects.construction_object import ConstructionObject


class NonDegeneracyPrediateCollector:
    def __init__(self):
        pass

    def collect(self, assumption_objects: dict[str, GeoObject], embedding: Embedding) -> List[Predicate]:
        triangle_non_degenerecy_predicates = self.collect_triangle_non_degenerecy_predicates(assumption_objects, embedding)
        return triangle_non_degenerecy_predicates

    def collect_triangle_non_degenerecy_predicates(self, assumption_objects: dict[str, GeoObject], embedding: Embedding) -> List[Predicate]:
        predicates = []

        points = {name: point for (name, point) in embedding.items() if isinstance(point, EmbeddedPoint)}
        for name0, name1, name2 in combinations(points, 3):
            point0, point1, point2 = points[name0], points[name1], points[name2]
            if point0.is_equal(point1) or point0.is_equal(point2) or point1.is_equal(point2):
                continue
            if (point1 - point0).is_proportional(point2 - point0):
                continue

            object0 = assumption_objects[name0]
            object1 = assumption_objects[name1]
            object2 = assumption_objects[name2]

            not_collinear_predicate = predicate_from_args('not_collinear', (object0, object1, object2))

            diff1 = point1 - point0
            orthogonal_to_diff1 = EmbeddedPoint(diff1.y, -diff1.x)
            diff2 = point2 - point0
            orientation = GeoObject(str(int(Decimal(90).copy_sign(diff2.scalar_product(orthogonal_to_diff1)))), LITERAL)

            orientation_object = ConstructionObject.from_args('orientation', (object0, object1, object2))
            orientation_predicate = predicate_from_args('equals_mod_360', (orientation_object, orientation))

            predicates.extend([not_collinear_predicate, orientation_predicate])

        return predicates
