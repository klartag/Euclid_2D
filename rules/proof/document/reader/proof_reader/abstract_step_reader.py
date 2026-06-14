from abc import ABC, abstractmethod
from dataclasses import dataclass
from re import Match
import re
from typing import Optional, TypeVar

from ....steps.step import Step

S = TypeVar('S', bound=Step)


@dataclass
class AbstractStepReader[S](ABC):
    """Can read a specific type of step in a proof."""

    @property
    @abstractmethod
    def pattern(self) -> str:
        """A regex pattern that can recognize whether a line in the proof can be read by this reader."""
        ...

    def try_read(self, line: str) -> Optional[S]:
        """
        Attempts to parse a step in the proof.
        Returns the parsed step if it can, and otherwise returns `None`.
        """
        match = re.search(self.pattern, line)
        if match is None:
            return None
        return self.read(line, match)

    @abstractmethod
    def read(self, line: str, match: Match[str]) -> S:
        """
        Parses a step in the proof.

        line:   The line that is being parsed.
        match:  The regex match returned from applying `self.pattern` on `line`.
        """
        ...
