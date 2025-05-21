from typing import Optional, TypeVar
from abc import ABC, abstractmethod

from ..geometry_objects.geo_type import Signature
from ..geometry_objects.geo_object import GeoObject

G = TypeVar("G", bound=GeoObject)


class ImmediateGeometryObjectParser[G](ABC):
    @abstractmethod
    def try_parse(self, text: str, signature: Signature) -> Optional[G]: ...
