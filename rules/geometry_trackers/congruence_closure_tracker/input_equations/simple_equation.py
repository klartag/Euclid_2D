from dataclasses import dataclass

from .abstract_input_equation import AbstractInputEquation


@dataclass
class SimpleEquation[T](AbstractInputEquation[T]):
    left: T
    right: T
