from dataclasses import dataclass

from .abstract_equation import AbstractEquation

@dataclass
class Equation[S, T](AbstractEquation[S, T]):
    pass
