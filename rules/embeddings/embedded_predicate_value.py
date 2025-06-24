from enum import Enum


class EmbeddedPredicateValue(Enum):
    """
    The possible return values when checking whether a predicate is correct in an Embedding.
    """

    Correct = 'True'
    """When the predicate is true."""
    Incorrect = 'False'
    """When the predicate is false."""
    Undefined = 'Undefined'
    """When the predicate cannot be evaluated (e.g. due to one of its parameters not existing)."""
