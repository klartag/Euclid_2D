from abc import ABC, abstractmethod
from typing import List, Optional

from ....predicates.predicate import Predicate


class PredicatePreprocessingPattern(ABC):
    @abstractmethod
    def try_match(self, predicate: Predicate) -> Optional[List[Predicate]]: ...
