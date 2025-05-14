from typing import Mapping

from rules.geometry_objects.geo_object import GeoObject


class Atom(GeoObject):
    def __init__(self, name: str, type_: str) -> None:
        self.name = name
        self.type = type_
        self.id = hash((self.name, self.type))
        self.depth = 1

    def substitute(self, replacements: 'Mapping[GeoObject, GeoObject]', ignore_self=False) -> 'GeoObject':
        """
        Replaces the given object with the given replacement objects.
        If the object is a construction or an equation, replaces subcomponents too.
        """
        return replacements[self]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Atom) and self.name == other.name and self.type == other.type

    def clone(self) -> 'GeoObject':
        return Atom(self.name, self.type)

    def as_literal(self) -> float | None:
        return None

    def as_linear_equation(self) -> 'dict[GeoObject, float] | None':
        return {self: 1}

    def involved_objects(self) -> 'set[GeoObject]':
        """
        Finds all objects referred to in the definition of this object.
        """
        return {self}

    def __hash__(self) -> int:
        return self.id
