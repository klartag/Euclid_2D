from dataclasses import dataclass

from ..geometry_objects.geo_type import Signature
from ..geometry_objects.geo_object import GeoObject
from ..predicates.predicate import Predicate


@dataclass
class Statement:
    """The statement of a geometry problem."""
    
    signature: Signature
    assumption_objects: dict[str, GeoObject]
    """All objects mentioned in the problem assumptions."""
    assumption_predicates: list[Predicate]
    """The predicates given in the problem assumptions."""
    auxiliary_predicates: list[Predicate]
    """Any auxiliary predicates that should be assumed, other than those in `self.assumption_predicates`."""
    target_objects: dict[str, GeoObject]
    """Names of objects that should be defined in order to solve the problem."""
    target_predicates: list[Predicate]
    """The predicates that must be proved."""

    def get_all_objects(self) -> dict[str, GeoObject]:
        """Returns all objects mentioned in the assumption and target predicates."""
        return self.assumption_objects | self.target_objects

    def starting_predicates(self) -> list[Predicate]:
        """Returns all predicates that should be taken as given at the beginning of a proof."""
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
