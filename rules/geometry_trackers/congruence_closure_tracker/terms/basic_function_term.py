from dataclasses import dataclass
from typing import Sequence


@dataclass
class BasicFunctionTerm[T]:
    function: str
    parameters: Sequence[T]
