from _collections_abc import dict_items
from typing import Dict
from functools import reduce

from ...geometry_objects.eq_op import EqOp
from ...geometry_objects.literal import Literal
from ...geometry_objects.equation_object import EquationObject
from ...geometry_objects.geo_object import GeoObject

from ...linear_algebra.vectors.abstract_vector import Rational


class LinearExpression:
    inner: Dict[GeoObject, Rational]

    def __init__(self, inner: Dict[GeoObject, Rational]):
        self.inner = inner

    def items(self) -> dict_items[GeoObject, Rational]:
        return self.inner.items()

    def to_equation_object(self) -> EquationObject | Literal:
        if len(self.inner) == 0:
            return Literal('0')
        monomials = [
            EquationObject(self._constant_to_equation_object(constant), geo_object, EqOp.MUL)
            for (geo_object, constant) in self.inner.items()
        ]
        return reduce(lambda x, y: EquationObject(x, y, EqOp.ADD), monomials)

    def _constant_to_equation_object(self, constant: Rational) -> EquationObject | Literal:
        if isinstance(constant, int):
            return Literal(str(constant))
        else:
            return EquationObject(Literal(str(constant.numerator)), Literal(str(constant.denominator)), EqOp.DIV)
