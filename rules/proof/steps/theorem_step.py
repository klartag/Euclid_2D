from dataclasses import dataclass, field
from typing import Mapping

from ...geometry_objects.geo_object import GeoObject
from ...predicates.predicate import Predicate

from .step import Step


@dataclass
class TheoremStep(Step):
    """
    TODO: Document
    """

    theorem_name: str
    inputs: list[GeoObject]
    result_predicates: list[Predicate]
    comment: str = field(compare=False, default='')

    def to_language_format(self) -> str:
        input_str = ', '.join(obj.name for obj in self.inputs)
        result_str = ', '.join([pred.to_language_format() for pred in self.result_predicates])

        comment = f'  # {self.comment}' if self.comment else ''

        return f'By {self.theorem_name} on {input_str} we get {result_str}{comment}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return TheoremStep(
            self.theorem_name,
            [g.substitute(subs) for g in self.inputs],
            [pred.substitute(subs) for pred in self.result_predicates],
            self.comment,
        )

    def __hash__(self) -> int:
        return hash(self.theorem_name) ^ hash(tuple(self.inputs))
