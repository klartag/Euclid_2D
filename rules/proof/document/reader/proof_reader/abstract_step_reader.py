from abc import ABC, abstractmethod
from dataclasses import dataclass
from re import Match
import re
from typing import Optional, TypeVar

from ....steps.step import Step

S = TypeVar('S', bound=Step)


@dataclass
class AbstractStepReader[S](ABC):
    @property
    @abstractmethod
    def pattern(self) -> str: ...

    def try_read(self, line: str) -> Optional[S]:
        match = re.search(self.pattern, line)
        if match is None:
            return None
        return self.read(line, match)

    @abstractmethod
    def read(self, line: str, match: Match[str]) -> S: ...
