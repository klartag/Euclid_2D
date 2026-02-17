from abc import ABC, abstractmethod
from dataclasses import dataclass
import itertools
from typing import Tuple

from ... import Embedding

from ...embedded_objects.embedded_object import EmbeddedObject
from ...embedder.embedded_geo_objects.embedded_geo_object import ExtendedGeoObject


@dataclass
class EmbeddedConstruction(ABC):
    '''
    Represents a way in which the embedding of a GeoObject can be constructed,
    given the embeddings of some other GeoObjects.
    '''

    input_objects: Tuple[ExtendedGeoObject, ...]
    '''The objects that should be input into the construction.'''
    output_name: str
    '''The name that the resulting object should get.'''

    def get_parameters(self, partial_embedding: Embedding) -> Tuple[Tuple[EmbeddedObject, ...]]:
        '''
        Gets the embeddings of the input objects.
        Since some EmbeddedObjects might have multiple possible values,
        returns a list of all possible tuples of values that the embedded objects may have.
        '''
        return tuple(itertools.product(*[partial_embedding.evaluate_object(obj_) for obj_ in self.input_objects]))

    @abstractmethod
    def construct(self, partial_embedding: Embedding) -> Tuple[EmbeddedObject, ...]:
        '''
        Constructs the eReturns all possible values this construction may have.
        '''
        ...

    def __repr__(self):
        type_name = type(self).__name__
        return f'{type_name}(output_name={self.output_name}, input_objects={self.input_objects})'
