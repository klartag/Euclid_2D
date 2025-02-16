from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Mapping, TypeVar, Tuple, Optional, TypeVarTuple, Unpack

from ....geometry_objects.geo_object import GeoObject

from ... import Embedding

from ...embedded_objects.embedded_object import EmbeddedObject

InputArgs = TypeVarTuple("InputArgs")
Output = TypeVar('Output', bound=EmbeddedObject)


@dataclass
class EmbeddedConstruction[InputArgs, Output](ABC):
    input_objects: Tuple[GeoObject, ...]
    output_name: str

    def get_parameters(self, partial_embedding: Embedding) -> Tuple[Unpack[InputArgs]]:
        return tuple([partial_embedding.evaluate_object(obj_) for obj_ in self.input_objects])

    @abstractmethod
    def construct(
        self, partial_embedding: Embedding, distinct_names: Mapping[str, List[str]]
    ) -> Optional[Output]: ...
