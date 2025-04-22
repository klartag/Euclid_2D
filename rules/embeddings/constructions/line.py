from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine


def line(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedLine:
    if point0.is_equal(point1):
        raise UndefinedEmbeddingError("Cannot calculate line through two identical points.")
    return EmbeddedLine(point0, point1 - point0)
