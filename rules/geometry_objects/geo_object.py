import re
from typing import Mapping, TypeVar

from ..rule_utils import LITERAL, NULL


LITERAL_PATTERN = r'(-?\d+(\.\d+)?)'
EQN_SPLIT_PATTERN = r'([+-])'

ID = 0


class GeoObject:
    __slots__ = 'name', 'type', 'id'
    name: str
    type: str
    id: int

    def __init__(self, name, type, id: int | None = None) -> None:
        self.name = name
        self.type = type
        self.id = id or hash((self.name, self.type))

    def substitute(self, replacements: 'Mapping[GeoObject, GeoObject]', ignore_self=False) -> 'GeoObject':
        """
        Replaces the given object with the given replacement objects.
        If the object is a construction or an equation, replaces subcomponents too.
        """
        return replacements.get(self, self)

    def __repr__(self) -> str:
        return self.name

    def to_language_format(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, GeoObject) and self.name == other.name and self.type == other.type

    def __hash__(self) -> int:
        return self.id

    def clone(self) -> 'GeoObject':
        return GeoObject(self.name, self.type, self.id)

    def __lt__(self, other: 'GeoObject') -> bool:
        return (len(self.name), self.name) < (len(other.name), other.name)

    def __le__(self, other: 'GeoObject') -> bool:
        return (len(self.name), self.name) <= (len(other.name), other.name)

    def __gt__(self, other: 'GeoObject') -> bool:
        return (len(self.name), self.name) > (len(other.name), other.name)

    def __ge__(self, other: 'GeoObject') -> bool:
        return (len(self.name), self.name) >= (len(other.name), other.name)

    def as_literal(self) -> float | None:
        if self.type == LITERAL:
            return float(self.name)
        return None

    def as_linear_equation(self) -> 'dict[GeoObject, float] | None':
        if self.type == LITERAL:
            val = self.as_literal()
            if val is None:
                return None
            if val != 0:
                return {ONE: val}
            return {}
        return {self: 1}

    def involved_objects(self) -> 'set[GeoObject]':
        """
        Finds all objects referred to in the definition of this object.
        """
        return {self}


ONE = GeoObject('1', LITERAL)
ZERO = GeoObject('0', LITERAL)
LOG_0 = GeoObject('LOG_0', NULL)


def is_literal(data: str) -> bool:
    """
    Checks if the data represents a literal.
    The current literals are only numbers.
    """
    return re.fullmatch(LITERAL_PATTERN, data) is not None


T = TypeVar('T')


def remove_empty(d: dict[T, float]) -> dict[T, float]:
    """
    Removes all items whose value is 0 from the dictionary.
    """
    return {k: v for k, v in d.items() if v != 0}
