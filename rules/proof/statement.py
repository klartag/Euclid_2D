from dataclasses import dataclass

from rules.geometry_objects.geo_type import Signature

from ..geometry_objects.geo_object import GeoObject
from ..predicates.predicate import Predicate


@dataclass
class Statement:
    signature: Signature
    assumption_objects: dict[str, GeoObject]
    assumption_predicates: list[Predicate]
    auxiliary_predicates: list[Predicate]
    target_objects: dict[str, GeoObject]
    target_predicates: list[Predicate]

    def get_all_objects(self) -> dict[str, GeoObject]:
        return self.assumption_objects | self.target_objects

    def starting_predicates(self) -> list[Predicate]:
        return self.assumption_predicates + self.auxiliary_predicates

    def shallow_copy(self) -> 'Statement':
        return Statement(
            dict(self.signature),
            dict(self.assumption_objects),
            list(self.assumption_predicates),
            list(self.auxiliary_predicates),
            dict(self.target_objects),
            list(self.target_predicates),
        )
