from abc import ABC, abstractmethod
from typing import Optional

from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate

from ...embedded_geo_objects.embedded_geo_object import ExtendedGeoObject


class LocusPattern(ABC):
    """
    Represents a way in which some predicates can be parsed into a defining locus for an object.
    """
    @abstractmethod
    def match(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]:
        """
        object_:    The object whose locus we are trying to define.
        predicate:  The predicate that defines the object.
        
        Returns:    An object that defines all possible locations `object_` can be in, that satisfy `predicate`.
                    (Returns `None` if the current LocusPattern does not know how to turn this predicate into a locus.)
        """
        ...
