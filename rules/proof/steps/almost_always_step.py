from dataclasses import dataclass
from typing import Mapping

from ...predicates.predicate import Predicate
from ...geometry_objects.geo_object import GeoObject

from .step import Step


@dataclass
class AlmostAlwaysStep(Step):
    """
    A step that states that some predicate is satisfied on an open set,
    and asserts that in the current problem it is almost always true.
    This assertion is not checked, and incorrect use of this step can lead to contradictions.
    """

    predicates: list[Predicate]

    def to_language_format(self) -> str:
        return f'It is almost always true that ' + ', '.join(pred.to_language_format() for pred in self.predicates)

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return AlmostAlwaysStep([pred.substitute(subs) for pred in self.predicates])
