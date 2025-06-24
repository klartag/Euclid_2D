from typing import Tuple
from mpmath import mpf

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, EPSILON

from .reflection import reflect_point
from .radical_axis import radical_axis


def line_circle_other_intersection(
    first_intersection: EmbeddedPoint, line: EmbeddedLine, circle: EmbeddedCircle
) -> EmbeddedPoint:
    """
    TODO: Document
    """
    orthogonal_direction = EmbeddedPoint(line.direction.y, -line.direction.x)
    symmetry_line = EmbeddedLine(circle.center, orthogonal_direction)
    other_intersection = reflect_point(first_intersection, symmetry_line)
    if other_intersection.is_equal(first_intersection):
        raise UndefinedEmbeddingError("The line and circle are tangent and do not have another intersection.")
    return other_intersection


def circle_circle_other_intersection(
    first_intersection: EmbeddedPoint, circle0: EmbeddedCircle, circle1: EmbeddedCircle
) -> EmbeddedPoint:
    """
    TODO: Document
    """
    if circle0.center.is_equal(circle1.center):
        raise UndefinedEmbeddingError("The circles are concentric and do not have valid intersections.")
    symmetry_line = EmbeddedLine(circle0.center, circle1.center - circle0.center)
    other_intersection = reflect_point(first_intersection, symmetry_line)
    if other_intersection.is_equal(first_intersection):
        raise UndefinedEmbeddingError("The circles are tangent and do not have another intersection.")
    return other_intersection


def quadratic_equation_solutions(a: mpf, b: mpf, c: mpf) -> Tuple[mpf, ...]:
    """
    TODO: Document
    """
    determinant = b**2 - 4 * a * c
    if abs(determinant) < EPSILON**2:
        return (-b / (2 * a),)
    elif determinant < 0:
        raise UndefinedEmbeddingError("No solution was found for the quadratic equation.")
    else:
        return ((-b + determinant**0.5) / (2 * a), (-b - determinant**0.5) / (2 * a))


def line_circle_intersection(line: EmbeddedLine, circle: EmbeddedCircle) -> Tuple[EmbeddedPoint, ...]:
    """
    TODO: Document
    """
    a = line.direction.length_squared()
    b = 2 * line.direction.scalar_product(line.point - circle.center)
    c = (line.point - circle.center).length_squared() - circle.radius_squared

    time_options = quadratic_equation_solutions(a, b, c)
    return tuple([line.point + line.direction.scale(t) for t in time_options])


def circle_circle_intersection(circle0: EmbeddedCircle, circle1: EmbeddedCircle) -> Tuple[EmbeddedPoint, ...]:
    """
    TODO: Document
    """
    axis = radical_axis(circle0, circle1)
    return line_circle_intersection(axis, circle0)
