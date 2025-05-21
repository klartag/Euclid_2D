import re
from typing import Optional

from ...errors import IllegalObjectError
from ...geometry_objects.geo_type import Signature
from ...geometry_objects.equation_object import EqOp, EquationObject

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser


class EquationObjectParser(AbstractGeometryObjectParser[EquationObject]):
    def try_parse(self, data: str, signature: Signature) -> Optional[EquationObject]:
        pass


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


def parse_equation_object(data: str, obj_map: dict[str, GeoObject]) -> EquationObject:
    """
    Parses a general equation equation with +-*/().
    """
    data = data.strip()

    # Finding all additions and subtractions.
    paren_depth = 0
    ops: list[EqOp] = []
    indices: list[int] = []
    for idx, c in enumerate(data):
        if c == '(':
            paren_depth += 1
        elif c == ')':
            paren_depth -= 1

        if paren_depth != 0:
            continue

        if c in '+-':
            ops.append(EqOp(c))
            indices.append(idx)

    if len(ops) > 0:
        indices.append(len(data))
        if indices[0] == 0:
            curr = ZERO
        else:
            curr = parse_geo_object(data[: indices[0]], obj_map)
        for i in range(len(ops)):
            nxt = parse_geo_object(data[indices[i] + 1 : indices[i + 1]], obj_map)
            curr = EquationObject(curr, nxt, ops[i])

        assert isinstance(curr, EquationObject)
        return curr

    # Finding all multiplications and divisions.
    paren_depth = 0
    ops = []
    indices = []
    for idx, c in enumerate(data):
        if c == '(':
            paren_depth += 1
        elif c == ')':
            paren_depth -= 1

        if paren_depth != 0:
            continue

        if c in '*/':
            ops.append(EqOp(c))
            indices.append(idx)

    assert len(ops) > 0
    indices.append(len(data))
    curr = parse_geo_object(data[: indices[0]], obj_map)
    for i in range(len(ops)):
        nxt = parse_geo_object(data[indices[i] + 1 : indices[i + 1]], obj_map)
        curr = EquationObject(curr, nxt, ops[i])

    assert isinstance(curr, EquationObject)
    return curr
