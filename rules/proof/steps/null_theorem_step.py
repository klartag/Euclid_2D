from dataclasses import dataclass
from typing import Mapping

from ...geometry_objects.geo_object import GeoObject
from ...predicates.predicate import Predicate

from .step import Step


@dataclass
class NullTheoremStep(Step):
    result_objects: list[GeoObject]
    result_predicates: list[Predicate]

    def to_language_format(self) -> str:
        result_str = ', '.join(
            [f'{obj.name}: {obj.type}' for obj in self.result_objects]
            + [pred.to_language_format() for pred in self.result_predicates]
        )
        return f'We have {result_str}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return NullTheoremStep(
            [g.substitute(subs) for g in self.result_objects],
            [pred.substitute(subs) for pred in self.result_predicates],
        )
