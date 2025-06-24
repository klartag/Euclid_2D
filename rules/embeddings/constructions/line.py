from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine


def line(A: EmbeddedPoint, B: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns the line AB.
    """
    if A.is_equal(B):
        raise UndefinedEmbeddingError("Cannot calculate line through two identical points.")
    return EmbeddedLine(A, B - A)
