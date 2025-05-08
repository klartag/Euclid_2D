from abc import ABC, abstractmethod
from re import Match
import re
from typing import Optional, TypeVar

from .....geometry_objects.geo_object import GeoObject

from ....steps.step import Step

S = TypeVar('S', Step)


class AbstractStepParser[S](ABC):
    @property
    @abstractmethod
    def pattern(self) -> str: ...

    def try_parse(self, line: str, obj_map: dict[str, GeoObject]) -> Optional[Step]:
        match = re.search(self.pattern(), line)
        if match is None:
            return None
        return self.parse(line, match, obj_map)

    @abstractmethod
    def parse(self, line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> Step: ...
