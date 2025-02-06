from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Mapping, TypeVar, Tuple, Optional, TypeVarTuple, Unpack

from ... import Embedding

from ...embedded_objects.embedded_object import EmbeddedObject

InputArgs = TypeVarTuple("InputArgs")
Output = TypeVar('Output', bound=EmbeddedObject)


@dataclass
class EmbeddedConstruction[InputArgs, Output](ABC):
    input_names: Tuple[str, ...]
    output_name: str

    def get_parameters(self, partial_embedding: Embedding) -> Tuple[Unpack[InputArgs]]:
        return tuple([partial_embedding[name] for name in self.input_names])

    @abstractmethod
    def construct(
        self, partial_embedding: Embedding, distinct_names: Mapping[str, List[str]]
    ) -> Optional[Output]: ...
