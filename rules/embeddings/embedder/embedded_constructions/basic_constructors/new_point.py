from typing import List, Mapping, Tuple, Optional
from decimal import Decimal
from random import normalvariate

from ....embedded_objects import EmbeddedObject, EmbeddedPoint

from ..embedded_construction import EmbeddedConstruction


def random_point() -> EmbeddedPoint:
    return EmbeddedPoint(Decimal(normalvariate()), Decimal(normalvariate()))


class NewPoint(EmbeddedConstruction[Tuple[()], EmbeddedPoint]):
    def construct(
        self, embedded_objects: Mapping[str, EmbeddedObject], distinct_names: Mapping[str, List[str]]
    ) -> Optional[EmbeddedPoint]:
        return random_point()
