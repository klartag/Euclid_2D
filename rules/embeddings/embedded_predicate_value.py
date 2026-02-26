from enum import Enum

class EmbeddedPredicateValue(Enum):
    """
    Represents a possible result when evaluating a predicate in an embedding.
    The `Undefined` value happens when a predicate can not be evaluated.
    """
    Correct = 'True'
    Incorrect = 'False'
    Undefined = 'Undefined'
