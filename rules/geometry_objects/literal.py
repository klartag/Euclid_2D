import re
from typing import Mapping

from rules.geometry_objects.geo_object import GeoObject

from ..rule_utils import LITERAL


LITERAL_PATTERN = r'(-?\d+(\.\d+)?)'


class Literal(GeoObject):
    def __init__(self, name: str) -> None:
        self.name = name
        self.type = LITERAL
        self.id = hash((self.name, LITERAL))
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


ONE = Literal('1')
ZERO = Literal('0')


def is_literal(data: str) -> bool:
    """
    Checks if the data represents a literal.
    The current literals are only numbers.
    """
    return re.fullmatch(LITERAL_PATTERN, data) is not None
