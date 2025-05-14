from ..rule_utils import split_args

from .geo_object import GeoObject
from .literal import Literal
from .literal import ZERO, is_literal
from .construction_object import ConstructionObject
from .equation_object import EquationObject, is_equation_object
from .eq_op import EqOp


def parse_geo_object(data: str, obj_map: dict[str, GeoObject]) -> GeoObject:
    """
    Parses the given data string.
    @data: A string describing a geometric object.
    @obj_map: A dictionary from names of objects to geometric objects.
    @return: The parsed geometric object.
    """
    data = data.strip()

    # Removing parentheses.
    while data[0] == '(':
        assert data[-1] == ')'
        data = data[1:-1]

    # Checking if the data is just a number, such as 50.
    if is_literal(data):
        return Literal(data)
    # Checking if the data is an equation.
    if is_equation_object(data):
        return parse_equation_object(data, obj_map)

    # If there are no parentheses, this is a simple object name.
    if '(' not in data:
        return obj_map[data]

    # This is a construction term, like distance(a, b).
    # Currently, construction objects will just have the name of their construction.
    const_name, arg_str = data[:-1].split('(', 1)
    args = tuple(parse_geo_object(arg, obj_map) for arg in split_args(arg_str))
    return ConstructionObject.from_args(const_name, args)


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
