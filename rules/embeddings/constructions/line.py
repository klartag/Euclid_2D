from typing import Optional

from ..embedded_objects import EmbeddedPoint, EmbeddedLine


def line(point0: EmbeddedPoint, point1: EmbeddedPoint) -> Optional[EmbeddedLine]:
    if point0.is_equal(point1):
        return None
    return EmbeddedLine(point0, point1 - point0)
