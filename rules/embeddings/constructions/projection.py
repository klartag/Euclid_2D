from ..embedded_objects import EmbeddedPoint, EmbeddedLine

from .line_intersection import line_intersection


def project(A: EmbeddedPoint, l: EmbeddedLine) -> EmbeddedPoint:
    """
    Returns the projection of A onto l.
    """
    orthogonal_direction = EmbeddedPoint(l.direction.y, -l.direction.x)
    altitude = EmbeddedLine(A, orthogonal_direction)
    return line_intersection(altitude, l)
