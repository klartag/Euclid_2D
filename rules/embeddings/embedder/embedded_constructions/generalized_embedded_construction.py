from dataclasses import dataclass
import itertools
from typing import Callable, Tuple, Unpack

from ... import Embedding

from ...embedded_objects.embedded_object import EmbeddedObject
from ...embedder.embedded_geo_objects.embedded_geo_object import ExtendedGeoObject

from .embedded_construction import EmbeddedConstruction

GeneralizedConstructionMethod = Callable[
    [Tuple[EmbeddedObject], Unpack[Tuple[EmbeddedObject, ...]]], Tuple[EmbeddedObject, ...]
]


@dataclass
class GeneralizedEmbeddedConstruction(EmbeddedConstruction):
    """
    TODO: Document
    """

    construction_method: GeneralizedConstructionMethod

    def __init__(
        self,
        input_objects: Tuple[ExtendedGeoObject, ...],
        output_name: str,
        construction_method: GeneralizedConstructionMethod,
    ):
        self.input_objects = input_objects
        self.output_name = output_name
        self.construction_method = construction_method

    def construct(self, partial_embedding: Embedding) -> Tuple[EmbeddedObject, ...]:
        parameter_options = self.get_parameters(partial_embedding)
        return tuple(
            itertools.chain(
                *[self.construction_method(partial_embedding.values(), *parameters) for parameters in parameter_options]
            )
        )

    def __repr__(self) -> str:
        type_name = type(self).__name__
        super_repr = super().__repr__()
        base_parameters = super_repr[super_repr.index('(') + 1 : super_repr.rindex(')')]
        method_parameter = f'construction_method={repr(self.construction_method.__name__)}'
        return f'{type_name}({method_parameter}, {base_parameters})'
