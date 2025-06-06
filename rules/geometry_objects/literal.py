import re
from typing import Mapping

from .geo_type import GeoType
from .geo_object import GeoObject


LITERAL_PATTERN = r'(-?\d+(\.\d+)?)'


class Literal(GeoObject):
    def __init__(self, name: str) -> None:
        self.name = name
        self.type = GeoType.LITERAL
        self.id = hash((self.name, GeoType.LITERAL))
        self.depth = 1

    def substitute(self, replacements: 'Mapping[GeoObject, GeoObject]', ignore_self=False) -> 'GeoObject':
        """
        Replaces the given object with the given replacement objects.
        If the object is a construction or an equation, replaces subcomponents too.
        """
        return self

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Literal) and self.name == other.name

    def clone(self) -> 'GeoObject':
        return Literal(self.name)

    def as_literal(self) -> float | None:
        return float(self.name)

    def as_linear_equation(self) -> 'dict[GeoObject, float] | None':
        return {ONE: self.as_literal()}

    def involved_objects(self) -> 'set[GeoObject]':
        """
        Finds all objects referred to in the definition of this object.
        """
        return set()

    def __hash__(self) -> int:
        return self.id


ONE = Literal('1')
ZERO = Literal('0')


def is_literal(data: str) -> bool:
    """
    Checks if the data represents a literal.
    The current literals are only numbers.
    """
    return re.fullmatch(LITERAL_PATTERN, data) is not None
