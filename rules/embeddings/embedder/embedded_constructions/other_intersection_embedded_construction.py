from dataclasses import dataclass
from typing import Callable, List, Mapping, Tuple, Optional, Unpack

from ....geometry_objects.geo_object import GeoObject

from ... import Embedding

from ...embedded_objects import EmbeddedPoint

from .embedded_construction import EmbeddedConstruction


@dataclass
class OtherIntersectionEmbeddedConstruction[InputArgs, Output](EmbeddedConstruction[InputArgs, Output]):
    construction_method: Callable[[Unpack[InputArgs]], Output]
    
    def __init__(self, input_objects: Tuple[GeoObject, ...], output_name: str, construction_method: Callable):
        self.input_objects = input_objects
        self.output_name = output_name
        self.construction_method = construction_method

    def construct(
        self, partial_embedding: Embedding, distinct_names: Mapping[str, List[str]]
    ) -> Optional[Output]:
        parameters = self.get_parameters(partial_embedding)
        for object in partial_embedding.values():
            if isinstance(object, EmbeddedPoint) and \
                all(parameter.contains_point(object) for parameter in parameters):
                return self.construction_method(object, *parameters)
