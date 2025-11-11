from dataclasses import dataclass
from typing import Self, Sequence


@dataclass(frozen=True)
class BasicFunctionTerm[T]:
    function: str
    parameters: tuple[T, ...]

    def __eq__(self, other: Self) -> bool:
        return isinstance(other, BasicFunctionTerm) and \
            self.function == other.function and \
            len(self.parameters) == len(other.parameters) and \
            all([p == q for (p, q) in zip(self.parameters, other.parameters)])
            
    def __hash__(self) -> int:
        return hash((self.function, tuple(self.parameters)))

    def __str__(self) -> str:
        return f'{self.function}{self.parameters}'
