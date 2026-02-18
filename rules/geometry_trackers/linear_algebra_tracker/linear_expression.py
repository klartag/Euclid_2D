from _collections_abc import dict_items
from fractions import Fraction
from typing import Dict
from functools import reduce

from ...geometry_objects.eq_op import EqOp
from ...geometry_objects.literal import Literal
from ...geometry_objects.equation_object import EquationObject
from ...geometry_objects.geo_object import GeoObject


class LinearExpression:
    '''Represents a linear expression of scalars.'''

    inner: Dict[GeoObject, Fraction]
    '''
    A mapping from each GeoObject
    (which must be a scalar for this expression to make sense)
    to a Fraction depicting how many times it appears in the linear expression.
    '''

    def __init__(self, inner: Dict[GeoObject, Fraction]):
        self.inner = inner

    def items(self):
        return self.inner.items()

    def keys(self):
        return self.inner.keys()

    def values(self):
        return self.inner.values()

    def __iter__(self):
        return iter(self.inner)

    def __contains__(self, k: GeoObject) -> bool:
        return k in self.inner
    
    def __len__(self) -> int:
        return len(self.inner)

    def to_equation_object(self) -> EquationObject | Literal:
        '''
        Returns an EquationObject that represents this linear expression.
        '''
        if len(self.inner) == 0:
            return Literal('0')

        monomials = [
            EquationObject(self._rational_to_equation_object(constant), geo_object, EqOp.MUL)
            for (geo_object, constant) in self.inner.items()
        ]
        return reduce(lambda x, y: EquationObject(x, y, EqOp.ADD), monomials)

    def _rational_to_equation_object(self, constant: Fraction) -> EquationObject | Literal:
        '''Converts a Fraction into a GeoObject representing its value.'''
        if isinstance(constant, int):
            return Literal(str(constant))
        else:
            return EquationObject(Literal(str(constant.numerator)), Literal(str(constant.denominator)), EqOp.DIV)

    def __repr__(self) -> str:
        return f'LinearExpression({self.inner})'
