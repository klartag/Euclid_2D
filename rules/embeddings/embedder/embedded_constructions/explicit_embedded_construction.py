from dataclasses import dataclass
from typing import Callable, List, Mapping, Tuple, Optional, Unpack

from ...embedded_objects.embedded_object import EmbeddedObject

from .embedded_construction import EmbeddedConstruction


@dataclass
class ExplicitEmbeddedConstruction[InputArgs, Output](EmbeddedConstruction[InputArgs, Output]):
    construction_method: Callable[[Unpack[InputArgs]], Output]
    
    def __init__(self, input_names: Tuple[str, ...], output_name: str, construction_method: Callable):
        self.input_names = input_names
        self.output_name = output_name
        self.construction_method = construction_method

    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[Output]:
        parameters = self.get_parameters(embedded_objects)
        return self.construction_method(*parameters)
