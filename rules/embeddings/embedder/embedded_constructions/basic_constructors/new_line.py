from typing import List, Mapping, Tuple, Optional

from ....embedded_objects import EmbeddedObject, EmbeddedLine

from ..embedded_construction import EmbeddedConstruction

from .new_point import random_point


class NewLine(EmbeddedConstruction[Tuple[()], EmbeddedLine]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedLine]:
        return EmbeddedLine(random_point(), random_point())
