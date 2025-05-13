from dataclasses import dataclass

from ..geometry_objects.geo_object import GeoObject
from ..predicates.predicate import Predicate


@dataclass
class Statement:
    objects: dict[str, GeoObject]
    assumption_predicates: list[Predicate]
    auxiliary_predicates: list[Predicate]
    target_predicates: list[Predicate]

    def starting_predicates(self) -> list[Predicate]:
        return self.assumption_predicates + self.auxiliary_predicates

    def shallow_copy(self) -> 'Statement':
        return Statement(
            dict(self.objects),
            list(self.assumption_predicates),
            list(self.auxiliary_predicates),
            list(self.target_predicates),
        )
