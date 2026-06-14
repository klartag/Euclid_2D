from typing import Optional, TypeVar
from abc import ABC, abstractmethod

G = TypeVar("G")
"""The type of object to parse"""


class AbstractGeometryParser[G](ABC):
    """A class that can parse text that depicts some sort of object related to geometry or the proof system."""

    @abstractmethod
    def try_parse(self, text: str) -> Optional[G]:
        ...
