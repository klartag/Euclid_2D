from typing import Optional, TypeVar
from abc import ABC, abstractmethod

G = TypeVar("G")
'''The type of object to parse'''


class AbstractGeometryParser[G](ABC):
    @abstractmethod
    def try_parse(self, text: str) -> Optional[G]: ...
