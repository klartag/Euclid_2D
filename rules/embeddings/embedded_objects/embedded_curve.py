from abc import abstractmethod

from .embedded_object import EmbeddedObject
from .point import EmbeddedPoint


class EmbeddedCurve(EmbeddedObject):
    @abstractmethod
    def contains_point(self, point: EmbeddedPoint) -> bool:
        """
        Returns whether a given point is on this curve.
        """
        ...
