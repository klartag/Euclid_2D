from typing import Optional, Tuple, TypeVar
from abc import ABC, abstractmethod

from ..geometry_objects.geo_object import GeoObject

D = TypeVar("D")
G = TypeVar("G", bound=GeoObject)


class DelayedGeometryObjectParser[D, G](ABC):
    @abstractmethod
    def try_split_components(self, text: str) -> Optional[Tuple[D, Tuple[str, ...]]]: ...

    @abstractmethod
    def build(self, data: D, components: Tuple[GeoObject, ...]) -> G: ...
