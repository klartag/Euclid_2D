from abc import ABC, abstractmethod
from typing import Optional

from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate

from ...embedded_geo_objects.embedded_geo_object import ExtendedGeoObject


class LocusPattern(ABC):
    @abstractmethod
    def match(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]: ...
