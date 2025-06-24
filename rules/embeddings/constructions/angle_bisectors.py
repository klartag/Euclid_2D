from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine


def internal_angle_bisector(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns the internal bisector of ∠ABC.
    """
    if A.is_equal(B) or B.is_equal(C):
        raise UndefinedEmbeddingError("Cannot evaluate internal angle bisector when two points are equal.")

    direction0 = (A - B).normalize()
    direction1 = (C - B).normalize()

    if direction0.is_equal(-direction1):
        orthogonal_direction = EmbeddedPoint(direction0.y, -direction0.x)
        return EmbeddedLine(B, orthogonal_direction)
    else:
        return EmbeddedLine(B, direction0 + direction1)


def external_angle_bisector(A: EmbeddedPoint, B: EmbeddedPoint, C: EmbeddedPoint) -> EmbeddedLine:
    """
    Returns the external bisector of ∠ABC.
    """
    if A.is_equal(B) or B.is_equal(C):
        raise UndefinedEmbeddingError("Cannot evaluate external angle bisector when two points are equal.")

    direction0 = (A - B).normalize()
    direction1 = (C - B).normalize()

    if direction0.is_equal(direction1):
        orthogonal_direction = EmbeddedPoint(direction0.y, -direction0.x)
        return EmbeddedLine(B, orthogonal_direction)
    else:
        return EmbeddedLine(B, direction0 - direction1)
