from dataclasses import dataclass
import itertools
from typing import Tuple

from ... import Embedding

from ...embedded_objects.embedded_object import EmbeddedObject
from ...types import ConstructionMethod
from ...embedder.embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

from .embedded_construction import EmbeddedConstruction


@dataclass
class ExplicitEmbeddedConstruction(EmbeddedConstruction):
    construction_method: ConstructionMethod
    
    def __init__(self, input_objects: Tuple[ExtendedGeoObject, ...], output_name: str, construction_method: ConstructionMethod):
        self.input_objects = input_objects
        self.output_name = output_name
        self.construction_method = construction_method

    def construct(self, partial_embedding: Embedding) -> Tuple[EmbeddedObject, ...]:
        parameter_options = self.get_parameters(partial_embedding)
        return tuple(itertools.chain(*[self.construction_method(*parameters) for parameters in parameter_options]))

    def __repr__(self) -> str:
        type_name = type(self).__name__
        super_repr = super().__repr__()
        base_parameters = super_repr[super_repr.index('(') + 1: super_repr.rindex(')')]
        method_parameter = f'construction_method={repr(self.construction_method.__name__)}'
        return f'{type_name}({method_parameter}, {base_parameters})'
