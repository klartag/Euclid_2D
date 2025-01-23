import math
from typing import Mapping

from .eq_op import EqOp
from .geo_object import ZERO, GeoObject, ONE
from ..rule_utils import LITERAL, GeometryError


class EquationObject(GeoObject):
    """
    A geometric object representing a combination of variables, such as `distance(A, B) + distance(B, C)`
    """
    left: GeoObject
    right: GeoObject
    op: EqOp

    def __init__(self, left: GeoObject, right: GeoObject, op: EqOp):
        if left.type != LITERAL:
            self.type = left.type
        elif right.type != LITERAL:
            self.type = right.type
        else:
            self.type = LITERAL

        self.left = left
        self.right = right
        self.op = op
        self.id = self._compute_hash()
        self.name = self.to_language_format()

    def _compute_hash(self) -> int:
        """
        Computes the hash of the edge.
        Should be called only once, during initialization.
        """
        if (self_literal := self.as_literal()) is not None:
            return int(round(self_literal * 1000))
        
        if (self_lin := self.as_linear_equation()) is not None:
            return hash(frozenset([(obj, int(round(factor*1000))) for obj, factor in self_lin.items()]))
        
        if (self_log := self.as_log_equation()) is not None:
            return hash(frozenset([(obj, int(round(factor*1000))) for obj, factor in self_log.items()]))
        
        return 0xffffffff

    def __hash__(self) -> int:
        return self.id

    def __eq__(self, other) -> bool:
        """
        Checks if two equations are the same.
        To do this, it evaluates the equations modulo P, with 
        """
        if not isinstance(other, GeoObject):
            return False
        if self.id != other.id:
            return False
        if (self_literal := self.as_literal()) is not None:
            other_literal = other.as_literal()
            if other_literal is None:
                return False
            return abs(self_literal - other_literal) < 1e-6
        if (self_lin := self.as_linear_equation()) is not None:
            other_lin = other.as_linear_equation()
            if other_lin is None:
                return False
            if any(abs(self_lin.get(key, 0) - val) > 1e-6 for key, val in other_lin.items()):
                return False
            if any(abs(other_lin.get(key, 0) - val) > 1e-6 for key, val in self_lin.items()):
                return False
            return True
        if (self_log := self.as_log_equation()) is not None:
            other_log = other.as_log_equation()
            if other_log is None:
                return False
            if any(abs(self_log.get(key, 0) - val) > 1e-6 for key, val in other_log.items()):
                return False
            if any(abs(other_log.get(key, 0) - val) > 1e-6 for key, val in self_log.items()):
                return False
            return True

        raise GeometryError(f'Equation {self} cannot be represented in any known format!')


    def __repr__(self) -> str:
        return self.to_language_format()


    def substitute(self, replacements: Mapping[GeoObject, GeoObject], ignore_self=False) -> GeoObject:
        if self in replacements and not ignore_self:
            return replacements[self]
        
        return EquationObject(self.left.substitute(replacements), self.right.substitute(replacements), self.op)


    def to_language_format(self) -> str:
        left_repr = f'({self.left.to_language_format()})' if isinstance(self.left, EquationObject) and self.left.op.priority() < self.op.priority() else self.left.to_language_format()
        right_repr = f'({self.right.to_language_format()})' if isinstance(self.right, EquationObject) and self.right.op.priority() < self.op.priority() else self.right.to_language_format()
        match self.op:
            case EqOp.ADD:
                if left_repr == '0':
                    return right_repr
                if right_repr == '0':
                    return left_repr
            case EqOp.SUB:
                if right_repr == '0':
                    return left_repr
            case EqOp.MUL:
                if left_repr == '1':
                    return right_repr
                if right_repr == '1':
                    return left_repr
            case EqOp.DIV:
                if right_repr == '1':
                    return left_repr
                
        return f'{left_repr} {self.op.value} {right_repr}'


    def clone(self) -> 'EquationObject':
        return self.substitute({})  # type: ignore


    def as_literal(self) -> float | None:
        """
        Attempts to transform the equation to a scalar.
        """
        if self.type != LITERAL:
            return None
        left_scalar = self.left.as_literal()
        right_scalar = self.right.as_literal()
        if left_scalar is None or right_scalar is None:
            # Not actually sure that this could happen.
            return None
        match self.op:
            case EqOp.ADD:
                return left_scalar + right_scalar
            case EqOp.SUB:
                return left_scalar - right_scalar
            case EqOp.MUL:
                return left_scalar * right_scalar
            case EqOp.DIV:
                return left_scalar / right_scalar


    def as_linear_equation(self) -> dict[GeoObject, float] | None:
        """
        Attempts to tranfsorm the equation to a dictionary mapping geoobjects to their coefficient in the equation.
        If it fails (For example, if there is a A*B factor), it returns None.
        """
        if self.type == LITERAL:
            val = self.as_literal()
            if val is None:
                return None
            if val != 0:
                return {ONE: val}
            else:
                return {}

        left_factors = self.left.as_linear_equation()
        right_factors = self.right.as_linear_equation()
        if left_factors is None or right_factors is None:
            return None
        
        match self.op:
            case EqOp.ADD:
                for obj, coef in right_factors.items():
                    left_factors[obj] = left_factors.get(obj, 0) + coef
                return left_factors
                
            case EqOp.SUB:
                for obj, coef in right_factors.items():
                    left_factors[obj] = left_factors.get(obj, 0) - coef
                return left_factors
                
            case EqOp.MUL:
                if self.left.type == LITERAL:
                    left_val = self.left.as_literal()
                    if left_val is None:
                        return None
                    return {obj: coef * left_val for obj, coef in right_factors.items()}
                if self.right.type == LITERAL:
                    right_val = self.right.as_literal()
                    if right_val is None:
                        return None
                    return {obj: coef * right_val for obj, coef in left_factors.items()}
                return None
            
            case EqOp.DIV:
                right_val = self.right.as_literal()
                if right_val is None:
                    return None
                return {obj: coef / right_val for obj, coef in left_factors.items()}        


    def as_log_equation(self) -> dict[GeoObject, float] | None:
        """
        Attempts to tranfsorm the equation to a dictionary mapping geoobjects to their coefficient in the equation.
        If it fails (For example, if there is a A*B factor), it returns None.
        """
        if self.type == LITERAL:
            val = self.as_literal()
            if (val is None) or (val == 0):
                return None
            return {ONE: math.log(val)}

        left_factors = self.left.as_log_equation()
        right_factors = self.right.as_log_equation()
        if left_factors is None or right_factors is None:
            return None
        
        match self.op:
            case EqOp.MUL:
                for obj, coef in right_factors.items():
                    left_factors[obj] = left_factors.get(obj, 0) + coef
                    return left_factors

            case EqOp.DIV:
                for obj, coef in right_factors.items():
                    left_factors[obj] = left_factors.get(obj, 0) - coef
                    return left_factors

            case EqOp.ADD | EqOp.SUB:
                return None
        
        raise Exception(f"Got unknown oepration {self.op}")


    def involved_objects(self) -> set[GeoObject]:
        return self.left.involved_objects() | self.right.involved_objects()


def is_equation_object(data: str) -> bool:
    """
    Checks if the given data represents an equation.
    The data represents an equation if it has any mathematical operator (+, -, *, /) out of parentheses.
    """
    paren_stack = 0
    for c in data:
        match c:
            case '+' | '-' | '*' | '/':
                if paren_stack == 0:
                    return True
            case '(':
                paren_stack += 1
            case ')':
                paren_stack -= 1
    return False


def __neg__(self) -> EquationObject:
    return EquationObject(ZERO, self, EqOp.SUB)


def __add__(self, other: GeoObject | int | float) -> EquationObject:
    if isinstance(other, int) or isinstance(other, float):
        other = GeoObject(str(other), LITERAL)
    
    return EquationObject(self, other, EqOp.ADD)


def __sub__(self, other: GeoObject | int | float) -> EquationObject:
    if isinstance(other, int) or isinstance(other, float):
        other = GeoObject(str(other), LITERAL)
    return EquationObject(self, other, EqOp.SUB)


def __mul__(self, other: GeoObject | int | float) -> EquationObject:
    if isinstance(other, int) or isinstance(other, float):
        other = GeoObject(str(other), LITERAL)

    return EquationObject(self, other, EqOp.MUL)


def __truediv__(self, other: GeoObject | int | float) -> 'EquationObject':
    """
    Attempts to divide the two equations.
    """
    if isinstance(other, int) or isinstance(other, float):
        other = GeoObject(str(other), LITERAL)
    return EquationObject(self, other, EqOp.DIV)


GeoObject.__neg__ = __neg__
GeoObject.__add__ = __add__
GeoObject.__sub__ = __sub__
GeoObject.__mul__ = __mul__
GeoObject.__truediv__ = __truediv__
