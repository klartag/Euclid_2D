from dataclasses import dataclass
from typing import Callable, Optional, Tuple, TypeVar
from abc import abstractmethod

from .abstract_geometry_parser import AbstractGeometryParser

G = TypeVar("G")
'''The type of object to parse'''

D = TypeVar("D")
'''The type of the data defining the object'''

C = TypeVar("C")
'''The type of each component inside the object'''


@dataclass
class AbstractRecursiveGeometryParser[G, D, C](AbstractGeometryParser[G]):
    component_parsing_func: Callable[[str], Optional[C]]

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
    def _try_split_components(self, text: str) -> Optional[Tuple[D, Tuple[str, ...]]]: ...

    @abstractmethod
    def _build(self, data: D, components: Tuple[C, ...]) -> G: ...
