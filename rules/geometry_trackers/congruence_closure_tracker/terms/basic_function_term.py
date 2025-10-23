from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class BasicFunctionTerm[T]:
    function: str
    parameters: Sequence[T]
