from dataclasses import dataclass
from typing import Sequence

from .abstract_term import AbstractTerm
from .constant_term import ConstantTerm


@dataclass
class BasicFunctionTerm[T](AbstractTerm[T]):
    function: str
    parameters: Sequence[ConstantTerm[T]]
