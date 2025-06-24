from abc import ABC, abstractmethod
from typing import Mapping

from .geo_type import GeoType


class GeoObject(ABC):
    """
    TODO: Document
    """

    __slots__ = 'name', 'type', 'id', 'depth'
    name: str
    type: GeoType
    id: int
    depth: int

    @abstractmethod
    def substitute(self, replacements: 'Mapping[GeoObject, GeoObject]', ignore_self=False) -> 'GeoObject':
        """
        Replaces the given object with the given replacement objects.
        If the object is a construction or an equation, replaces subcomponents too.
        """
        ...

    @abstractmethod
    def involved_objects(self) -> 'set[GeoObject]':
        """
        Finds all objects referred to in the definition of this object.
        """
        ...

    @abstractmethod
    def as_linear_equation(self) -> 'dict[GeoObject, float] | None':
        """
        TODO: Document
        """
        ...

    @abstractmethod
    def as_literal(self) -> float | None:
        """
        TODO: Document
        """
        ...

    @abstractmethod
    def clone(self) -> 'GeoObject':
        """
        TODO: Document
        """
        ...

    @abstractmethod
    def __eq__(self, other: object) -> bool: ...

    def __lt__(self, other: 'GeoObject') -> bool:
        return (self.depth, len(self.name), self.name) < (other.depth, len(other.name), other.name)

    def __le__(self, other: 'GeoObject') -> bool:
        return (self.depth, len(self.name), self.name) <= (other.depth, len(other.name), other.name)

    def __gt__(self, other: 'GeoObject') -> bool:
        return (self.depth, len(self.name), self.name) > (other.depth, len(other.name), other.name)

    def __ge__(self, other: 'GeoObject') -> bool:
        return (self.depth, len(self.name), self.name) >= (other.depth, len(other.name), other.name)

    def __hash__(self) -> int:
        return self.id

    def __repr__(self) -> str:
        return self.name

    def to_language_format(self) -> str:
        """
        TODO: Document
        """
        return self.name
