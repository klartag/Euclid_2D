from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle

from .reflection import reflect_point


def line_circle_other_intersection(
    first_intersection: EmbeddedPoint, line: EmbeddedLine, circle: EmbeddedCircle
) -> EmbeddedPoint:
    orthogonal_direction = EmbeddedPoint(line.direction.y, -line.direction.x)
    symmetry_line = EmbeddedLine(circle.center, orthogonal_direction)
    other_intersection = reflect_point(first_intersection, symmetry_line)
    if other_intersection.is_equal(first_intersection):
        raise UndefinedEmbeddingError("The line and circle are tangent and do not have another intersection.")
    return other_intersection


def circle_circle_other_intersection(
    first_intersection: EmbeddedPoint, circle0: EmbeddedCircle, circle1: EmbeddedCircle
) -> EmbeddedPoint:
    if circle0.center.is_equal(circle1.center):
        raise UndefinedEmbeddingError("The circles are concentric and do not have valid intersections.")
    symmetry_line = EmbeddedLine(circle0.center, circle1.center - circle0.center)
    other_intersection = reflect_point(first_intersection, symmetry_line)
    if other_intersection.is_equal(first_intersection):
        raise UndefinedEmbeddingError("The circles are tangent and do not have another intersection.")
    return other_intersection
