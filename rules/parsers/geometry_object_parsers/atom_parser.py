import re
from typing import Literal, Optional

from ...errors import IllegalObjectError
from ...geometry_objects.geo_type import Signature
from ...geometry_objects.atom import Atom

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser

ATOM_PATTERN = r'[A-Za-z_][A-Za-z_0-9\']*'


class AtomParser(AbstractGeometryObjectParser[Atom]):
    def try_parse(self, data: str, signature: Signature) -> Optional[Atom]:
        if re.fullmatch(ATOM_PATTERN, data) is None:
            return None
        if data not in signature:
            raise IllegalObjectError(f"The type of the Atom with the name `{data}` is not known.")
        return Atom(data, signature[data])


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
