from dataclasses import dataclass
import itertools
from typing import List, Mapping, Tuple

from ....geometry_objects.geo_object import GeoObject

from ... import Embedding

from ...embedded_objects.embedded_object import EmbeddedObject
from ...types import ConstructionMethod
from ...embedder.embedded_geo_objects.embedded_geo_object import EmbeddedGeoObject

from .embedded_construction import EmbeddedConstruction


@dataclass
class ExplicitEmbeddedConstruction(EmbeddedConstruction):
    construction_method: ConstructionMethod
    
    def __init__(self, input_objects: Tuple[GeoObject | EmbeddedGeoObject, ...], output_name: str, construction_method: ConstructionMethod):
        self.input_objects = input_objects
        self.output_name = output_name
        self.construction_method = construction_method

    def construct(
        self, partial_embedding: Embedding, distinct_names: Mapping[str, List[str]]
    ) -> Tuple[EmbeddedObject, ...]:
        parameter_options = self.get_parameters(partial_embedding)
        return tuple(itertools.chain(*[self.construction_method(*parameters) for parameters in parameter_options]))
