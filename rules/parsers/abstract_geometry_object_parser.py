from typing import Optional, TypeVar
from abc import ABC, abstractmethod

from ..geometry_objects.geo_type import Signature

T = TypeVar("T")


class AbstractGeometryObjectParser[T](ABC):
    @abstractmethod
    def try_parse(self, data: str, signature: Signature) -> Optional[T]: ...
