from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine


def line_intersection(line0: EmbeddedLine, line1: EmbeddedLine) -> EmbeddedPoint:
    if line0.direction.is_proportional(line1.direction):
        raise UndefinedEmbeddingError("Cannot calculate line intersection of parallel lines.")
    delta = line1.point - line0.point
    determinant = line0.direction.x * line1.direction.y - line0.direction.y * line1.direction.x
    t = (delta.x * line1.direction.y - delta.y * line1.direction.x) / determinant
    return line0.point + line0.direction.scale(t)
