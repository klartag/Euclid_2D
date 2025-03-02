from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle

from .projection import project
from .parallels_and_perpendiculars import perpendicular_line
from .line import line


def tangent_point(line: EmbeddedLine, circle: EmbeddedCircle) -> EmbeddedPoint:
    projection = project(circle.center, line)
    if not circle.contains_point(projection):
        raise UndefinedEmbeddingError("Cannot calculate tangent point of line not tangent to the circle")
    return projection


def tangent_line(point: EmbeddedPoint, circle: EmbeddedCircle) -> EmbeddedLine:
    if not circle.contains_point(point):
        raise UndefinedEmbeddingError("Cannot calculate tangent line from point not on the circle")
    center_line = line(point, circle.center)
    return perpendicular_line(point, center_line)
