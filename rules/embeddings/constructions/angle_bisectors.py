from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine

def internal_angle_bisector(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedLine:
    if point0.is_equal(point1) or point1.is_equal(point2):
        raise UndefinedEmbeddingError("Cannot evaluate internal angle bisector when two points are equal.")

    direction0 = (point0 - point1).normalize()
    direction1 = (point2 - point1).normalize()

    if direction0.is_equal(-direction1):
        orthogonal_direction = EmbeddedPoint(direction0.y, -direction0.x)
        return EmbeddedLine(point1, orthogonal_direction)
    else:
        return EmbeddedLine(point1, direction0 + direction1)


def external_angle_bisector(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedLine:
    if point0.is_equal(point1) or point1.is_equal(point2):
        raise UndefinedEmbeddingError("Cannot evaluate external angle bisector when two points are equal.")

    direction0 = (point0 - point1).normalize()
    direction1 = (point2 - point1).normalize()

    if direction0.is_equal(direction1):
        orthogonal_direction = EmbeddedPoint(direction0.y, -direction0.x)
        return EmbeddedLine(point1, orthogonal_direction)
    else:
        return EmbeddedLine(point1, direction0 - direction1)
