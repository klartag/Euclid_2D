from dataclasses import dataclass
from typing import Callable, List, Mapping, Tuple, Optional, Unpack

from ....geometry_objects.geo_object import GeoObject

from ... import Embedding

from .embedded_construction import EmbeddedConstruction


@dataclass
class ExplicitEmbeddedConstruction[InputArgs, Output](EmbeddedConstruction[InputArgs, Output]):
    construction_method: Callable[[Unpack[InputArgs]], Output]
    
    def __init__(self, input_objects: Tuple[GeoObject, ...], output_name: str, construction_method: Callable):
        self.input_objects = input_objects
        self.output_name = output_name
        self.construction_method = construction_method

    def construct(
        self, partial_embedding: Embedding, distinct_names: Mapping[str, List[str]]
    ) -> Optional[Output]:
        parameters = self.get_parameters(partial_embedding)
        if any(parameter is None for parameter in parameters):
            return None
        return self.construction_method(*parameters)
