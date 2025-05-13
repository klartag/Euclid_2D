from ..geometry_objects.geo_object import GeoObject
from ..predicates.predicate import Predicate


class Assumptions:
    objects: dict[str, GeoObject]
    predicates: list[Predicate]
