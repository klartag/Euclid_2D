from abc import ABC, abstractmethod
from dataclasses import dataclass
import itertools
from typing import Tuple

from ... import Embedding

from ...embedded_objects.embedded_object import EmbeddedObject
from ...embedder.embedded_geo_objects.embedded_geo_object import ExtendedGeoObject


@dataclass
class EmbeddedConstruction(ABC):
    """
    TODO: Document
    """

    input_objects: Tuple[ExtendedGeoObject, ...]
    output_name: str

    def get_parameters(self, partial_embedding: Embedding) -> Tuple[Tuple[EmbeddedObject, ...]]:
        """
        TODO: Document
        """
        return tuple(itertools.product(*[partial_embedding.evaluate_object(obj_) for obj_ in self.input_objects]))

    @abstractmethod
    def construct(self, partial_embedding: Embedding) -> Tuple[EmbeddedObject, ...]:
        """
        TODO: Document
        """
        ...

    def __repr__(self):
        type_name = type(self).__name__
        return f'{type_name}(output_name={self.output_name}, input_objects={self.input_objects})'
