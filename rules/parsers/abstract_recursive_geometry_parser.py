from dataclasses import dataclass
from typing import Callable, Optional, Tuple, TypeVar
from abc import abstractmethod

from .abstract_geometry_parser import AbstractGeometryParser

G = TypeVar("G")
"""The type of object to parse"""

D = TypeVar("D")
"""The type of the data defining the object"""

C = TypeVar("C")
"""The type of each component inside the object"""


@dataclass
class AbstractRecursiveGeometryParser[G, D, C](AbstractGeometryParser[G]):
    """
    A class that can parse an object that is built from an array of objects.
    
    C:  The type of object in each item in the array.
        For the rest of the documentation in this file, these will be called the "inner components" of the object.
    D:  A type of object that tells how to put each of the `C`s together.
        For the rest of the documentation in this file, this will be called the "data component" of the object.
    
    An example would be a parser for a ConstructionObject,
    `construction(object_0, object_1, object_2, ...)`
    where each of the `object_i`s are a GeoObject, and `construction` is the name of the construction.
    In this case, the data component would be of the type Construction,
    and the inner components would be GeoObjects.
    """

    component_parsing_func: Callable[[str], Optional[C]]
    """A method to use to parse each of the values of type `C` in the array."""

    def try_parse(self, text: str) -> Optional[G]:
        result = self._try_split_components(text)
        if result is None:
            return None
        data, components_text = result

        components: list[C] = []
        for component_text in components_text:
            component = self.component_parsing_func(component_text)
            if component is None:
                return None
            components.append(component)

        return self._build(data, tuple(components))

    @abstractmethod
    def _try_split_components(self, text: str) -> Optional[Tuple[D, Tuple[str, ...]]]:
        """
        Splits the text into the data component, and a list of strings that can each be parsed into an inner component.
        """
        ...

    @abstractmethod
    def _build(self, data: D, components: Tuple[C, ...]) -> G:
        """Uses the data component and a list of inner components to build the object."""
        ...
