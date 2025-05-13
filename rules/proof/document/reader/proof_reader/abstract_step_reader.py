from abc import ABC, abstractmethod
from re import Match
import re
from typing import Optional, TypeVar

from .....geometry_objects.geo_object import GeoObject

from ....steps.step import Step

S = TypeVar('S', Step)


class AbstractStepReader[S](ABC):
    @property
    @abstractmethod
    def pattern(self) -> str: ...

    def try_read(self, line: str, obj_map: dict[str, GeoObject]) -> Optional[Step]:
        match = re.search(self.pattern(), line)
        if match is None:
            return None
        return self.read(line, match, obj_map)

    @abstractmethod
    def read(self, line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> Step: ...
