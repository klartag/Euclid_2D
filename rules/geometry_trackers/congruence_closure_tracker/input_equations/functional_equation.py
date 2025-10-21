from dataclasses import dataclass

from .abstract_input_equation import AbstractInputEquation


@dataclass
class FunctionalEquation[T](AbstractInputEquation[T]):
    left0: T
    left1: T
    right: T
