from dataclasses import dataclass
from typing import Mapping

from ...geometry_objects.geo_object import GeoObject
from ...predicates.predicate import Predicate

from .step import Step


@dataclass
class IfStep(Step):
    """
    A step of the form:
    If predicate:
        stuff
    Else if predicate:
        stuff
    """

    data: dict[Predicate, list[Step]]
    """A dictionary, containing a map from tested predicate to the proof segment under it."""

    def to_language_format(self) -> str:
        reprs = [
            (pred.to_language_format(), '\n'.join(step.to_language_format() for step in steps))
            for pred, steps in self.data.items()
        ]
        reprs = sorted(reprs, key=lambda t: len(t[1]))
        res = []
        for pred, body in reprs:
            if len(res) == 0:
                res.append(f'If {pred}:')
            else:
                res.append(f'Else if {pred}:')
            body = body.split('\n')
            body = ['\t' + row for row in body]
            body = '\n'.join(body)
            res.append(body)
        return '\n'.join(res)

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return IfStep(
            {
                pred.substitute(subs): [sub_step.substitute(subs) for sub_step in sub_steps]
                for pred, sub_steps in self.data.items()
            }
        )
