from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from .line_intersection import line_intersection


def project(point: EmbeddedPoint, line: EmbeddedLine) -> EmbeddedPoint:
    orthogonal_direction = EmbeddedPoint(line.direction.y, -line.direction.x)
    altitude = EmbeddedLine(point, orthogonal_direction)
    return line_intersection(altitude, line)
