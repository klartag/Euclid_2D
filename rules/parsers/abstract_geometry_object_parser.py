from typing import Optional, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class AbstractGeometryObjectParser[T](ABC):
    @abstractmethod
    def try_parse(self, data: str) -> Optional[T]: ...
