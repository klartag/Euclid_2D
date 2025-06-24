import abc
from dataclasses import dataclass
from typing import Mapping

from ...geometry_objects.geo_object import GeoObject


@dataclass
class Step(abc.ABC):
    """
    TODO: Document
    """

    @abc.abstractmethod
    def to_language_format(self) -> str:
        """
        Converts the given step to a string representing the step.
        """
        ...

    @abc.abstractmethod
    def substitute(self, subs: 'Mapping[GeoObject, GeoObject]') -> 'Step':
        """
        Replaces the object in the given step with other objects.
        """
        ...
