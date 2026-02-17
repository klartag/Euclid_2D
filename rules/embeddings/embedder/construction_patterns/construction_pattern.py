from abc import ABC, abstractmethod
from typing import List, Optional

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate

from ..embedded_constructions.embedded_construction import EmbeddedConstruction


class ConstructionPattern(ABC):
    '''
    Represents a pattern that a list of predicates may follow,
    that can help understand how to construct a GeoObject
    given the predicates it satisfies.
    '''

    @abstractmethod
    def match(self, object_: GeoObject, predicates: List[Predicate]) -> Optional[EmbeddedConstruction]:
        '''
        Checks whether this ConstructionPattern knows how to construct the embedding of `object_` given the list of predicates in `predicates`.
        If so, returns an `EmbeddedConstruction` describing how the embedding of `object_` can be calculated.
        
        object_:        The GeoObject whose embedding we want to know how to calculate.
        predicates:     The list of *all* predicates containing `object_`,
                        that the `Embedder` did not take into account so far.
                        
        Returns:        Instructions on how to calculate the embedding of `object_` in a way that
                        is equivalent to all of the `predicates`.
        '''
        ...
