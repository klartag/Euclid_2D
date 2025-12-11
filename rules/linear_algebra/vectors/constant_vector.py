from fractions import Fraction
from typing import Literal, Self

from .abstract_vector import AbstractVector


class ConstantVector(AbstractVector):
    type_name: Literal['Constant'] = 'Constant'

    inner: Fraction

    def __init__(self, value: Fraction):
        self.inner = value

    def __mul__(self, x: Fraction) -> 'ConstantVector':
        return ConstantVector(self.inner * x)

    def __truediv__(self, x: Fraction) -> 'ConstantVector':
        return ConstantVector(self.inner / x)

    def __add__(self, other: Self) -> 'ConstantVector':
        return ConstantVector(self.inner + other.inner)

    def __sub__(self, other: Self) -> 'ConstantVector':
        return ConstantVector(self.inner - other.inner)
    
    def __eq__(self, other: Self) -> bool:
        return self.inner == other.inner
    
    def __bool__(self) -> bool:
        return self.inner != 0

    def inner_repr(self) -> str:
        return str(self.inner)

    def clone(self) -> 'ConstantVector':
        return ConstantVector(self.inner)
