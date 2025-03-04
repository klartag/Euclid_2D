from dataclasses import dataclass
from typing import Callable, List, Mapping, Tuple, Optional, Unpack

from ....embeddings.embedded_objects.embedded_object import EmbeddedObject
from ....geometry_objects.geo_object import GeoObject

from ... import Embedding
from ...embedded_objects import EmbeddedPoint
from ...types import ConstructionMethod

from .embedded_construction import EmbeddedConstruction


@dataclass
class OtherIntersectionEmbeddedConstruction(EmbeddedConstruction):
    construction_method: ConstructionMethod
    
    def __init__(self, input_objects: Tuple[GeoObject, ...], output_name: str, construction_method: ConstructionMethod):
        self.input_objects = input_objects
        self.output_name = output_name
        self.construction_method = construction_method

    def construct(
        self, partial_embedding: Embedding, distinct_names: Mapping[str, List[str]]
    ) -> Tuple[EmbeddedObject, ...]:
        parameter_options = self.get_parameters(partial_embedding)
        results = []
        for parameter_option in parameter_options:
            for obj in partial_embedding.values():
                if isinstance(obj, EmbeddedPoint) and \
                    all(parameter.contains_point(obj) for parameter in parameter_option):
                    results.extend(self.construction_method(obj, *parameter_option))
        return tuple(results)
