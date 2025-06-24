from abc import ABC, abstractmethod
from typing import List, Optional

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate

from ..embedded_constructions.embedded_construction import EmbeddedConstruction


class ConstructionPattern(ABC):
    """
    TODO: Document
    """

    @abstractmethod
    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        """
        TODO: Document
        """
        ...
