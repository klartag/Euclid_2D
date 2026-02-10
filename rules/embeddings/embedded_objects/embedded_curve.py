from abc import abstractmethod

from .embedded_object import EmbeddedObject
from .point import EmbeddedPoint


class EmbeddedCurve(EmbeddedObject):
    '''Represents a curve embedded in coordinate space.'''

    @abstractmethod
    def contains_point(self, point: EmbeddedPoint) -> bool:
        '''Returns whether this curve contains a point.'''
        ...
