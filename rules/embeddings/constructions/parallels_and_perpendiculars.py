from mpmath import mpf

from ..undefined_embedding_error import UndefinedEmbeddingError
from ..embedded_objects import EmbeddedPoint, EmbeddedLine
from ..predicates.collinear import collinear

from .line_intersection import line_intersection
from .line import line

def parallel_line(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedLine:
    return EmbeddedLine(point, line.direction)

def perpendicular_line(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedLine:
    orthogonal_direction = EmbeddedPoint(line.direction.y, -line.direction.x)
    return EmbeddedLine(point, orthogonal_direction)

def perpendicular_bisector(point0: EmbeddedPoint, point1: EmbeddedPoint) -> EmbeddedLine:
    if point0.is_equal(point1):
        raise UndefinedEmbeddingError("Cannot calculate perpendicular bisector of two identical points.")
    midpoint = (point0 + point1).scale(mpf('0.5'))
    direction = point1 - point0
    orthogonal_direction = EmbeddedPoint(direction.y, -direction.x)
    return EmbeddedLine(midpoint, orthogonal_direction)

def altitude(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedLine:
    if collinear(point0, point1, point2):
        raise UndefinedEmbeddingError("Cannot calculate altitude of triangle with collinear vertices.")
    return perpendicular_line(point0, line(point1, point2))

def orthocenter(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> EmbeddedPoint:
    if collinear(point0, point1, point2):
        raise UndefinedEmbeddingError("Cannot calculate orthocenter of triangle with collinear vertices.")
    altitude0 = altitude(point0, point1, point2)
    altitude1 = altitude(point1, point2, point0)
    return line_intersection(altitude0, altitude1)
