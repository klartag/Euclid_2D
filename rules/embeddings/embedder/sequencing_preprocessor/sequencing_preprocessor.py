from typing import List

from ....predicates.predicate import Predicate

from .pattern import PredicatePreprocessingPattern


class SequencingPreprocessor:
    '''
    An object that applies `PredicatePreprocessingPattern`s over an entire list of predicates.
    '''
    def __init__(self, patterns: List[PredicatePreprocessingPattern]):
        self.patterns = patterns
    
    def preprocess_assumptions(self, predicates: List[Predicate]) -> List[Predicate]:
        '''
        Takes a list of predicates as input.
        For each predicate, if it matches a pattern from `self.patterns`, applies it.
        Otherwise, keeps the predicate as it was.
        
        Returns the processed list of predicates.
        '''
        processed_predicates = []
        for predicate in predicates:
            for preprocess_pattern in self.patterns:
                pattern_match_attempt = preprocess_pattern.try_match(predicate)
                if pattern_match_attempt is not None:
                    processed_predicates.extend(pattern_match_attempt)
                    break
            else:
                processed_predicates.append(predicate)
        return processed_predicates
