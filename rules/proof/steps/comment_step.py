from dataclasses import dataclass
from typing import Mapping

from ...geometry_objects.geo_object import GeoObject

from .step import Step


@dataclass
class CommentStep(Step):
    comment: str

    def to_language_format(self):
        return f'Comment: {self.comment}'

    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        return CommentStep(self.comment)
