from _collections_abc import dict_items
from fractions import Fraction
from typing import Dict
from functools import reduce

from ...geometry_objects.eq_op import EqOp
from ...geometry_objects.literal import Literal
from ...geometry_objects.equation_object import EquationObject
from ...geometry_objects.geo_object import GeoObject


class LinearExpression:
    inner: Dict[GeoObject, Fraction]

    def __init__(self, inner: Dict[GeoObject, Fraction]):
        self.inner = inner

    def items(self):
        return self.inner.items()

    def to_equation_object(self) -> EquationObject | Literal:
        if len(self.inner) == 0:
            return Literal('0')

        monomials = [
            EquationObject(self._rational_to_equation_object(constant), geo_object, EqOp.MUL)
            for (geo_object, constant) in self.inner.items()
        ]
        return reduce(lambda x, y: EquationObject(x, y, EqOp.ADD), monomials)

    def _rational_to_equation_object(self, constant: Fraction) -> EquationObject | Literal:
        if isinstance(constant, int):
            return Literal(str(constant))
        else:
            return EquationObject(Literal(str(constant.numerator)), Literal(str(constant.denominator)), EqOp.DIV)

    def __repr__(self) -> str:
        return f'LinearExpression({self.inner})'
