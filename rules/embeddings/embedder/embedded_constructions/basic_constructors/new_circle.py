from decimal import Decimal
from typing import List, Mapping, Tuple, Optional

from random import normalvariate

from ....embedded_objects import EmbeddedObject, EmbeddedCircle

from ..embedded_construction import EmbeddedConstruction

from .new_point import random_point


class NewCircle(EmbeddedConstruction[Tuple[()], EmbeddedCircle]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedCircle]:
        return EmbeddedCircle(random_point(), Decimal(normalvariate() ** 2))
