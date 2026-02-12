from abc import ABC, abstractmethod
from typing import List, Optional

from ....predicates.predicate import Predicate


class PredicatePreprocessingPattern(ABC):
    '''
    An object that recognizes if a predicate matches a certain pattern,
    and if it does, replaces it with a different list of predicates.
    '''
    @abstractmethod
    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]:
        '''
        If `predicate` is a good match, returns the list of predicates it should be replaced with.
        Otherwise, returns `None`.
        '''
        ...
