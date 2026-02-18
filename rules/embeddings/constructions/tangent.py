from typing import Tuple

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, EPSILON
from .circle_intersection import line_circle_intersection

from .projection import project
from .parallels_and_perpendiculars import perpendicular_line
from .line import line


def line_circle_tangent_point(line: EmbeddedLine, circle: EmbeddedCircle) -> EmbeddedPoint:
    '''
    Returns the point of tangency between a line and a circle.
    (If the given line and circle are not tangent to each other, raises an error.)
    '''
    projection = project(circle.center, line)
    if not circle.contains_point(projection):
        raise UndefinedEmbeddingError("Cannot calculate tangent point of line not tangent to the circle")
    return projection


def circle_circle_tangent_point(circle0: EmbeddedCircle, circle1: EmbeddedCircle) -> EmbeddedPoint:
    '''
    Returns the point of tangency between two circles.
    (If the given circles are not tangent to each other, raises an error.)
    '''
    center_line = line(circle0.center, circle1.center)
    potential_tangency_candidates = line_circle_intersection(center_line, circle0)
    for candidate in potential_tangency_candidates:
        if circle1.contains_point(candidate):
            return candidate
    else:
        raise UndefinedEmbeddingError("Attempted to calculate tangent point between two circles that are not tangent.")


def point_circle_tangent_line(point: EmbeddedPoint, circle: EmbeddedCircle) -> EmbeddedLine:
    '''
    Returns the line tangent to a circle at a given point.
    (If the given point does not lie on the circle, raises an error.)
    '''
    if not circle.contains_point(point):
        raise UndefinedEmbeddingError("Cannot calculate tangent line from point not on the circle")
    center_line = line(point, circle.center)
    return perpendicular_line(point, center_line)


def tangent_line(point: EmbeddedPoint, circle: EmbeddedCircle) -> Tuple[EmbeddedLine]:
    '''
    Returns all tangent lines to a circle that pass through a given point.
    (The point need not necessarily lie on the circle.)
    '''
    power_of_a_point = (circle.center - point).length_squared() - circle.radius_squared
    if abs(power_of_a_point) < EPSILON**2:
        return (point_circle_tangent_line(point, circle),)
    elif power_of_a_point < 0:
        return ()
    else:
        inversion_ratio = circle.radius_squared / (circle.center - point).length_squared()
        inverted_point = circle.center + (point - circle.center).scale(inversion_ratio)
        polar_line = perpendicular_line(inverted_point, line(inverted_point, circle.center))
        polar_line_intersections = line_circle_intersection(polar_line, circle)
        return tuple([line(point, intersection) for intersection in polar_line_intersections])
