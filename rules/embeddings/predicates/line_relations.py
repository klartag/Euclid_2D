from ..embedded_objects import EmbeddedPoint, EmbeddedLine


def parallel(line0: EmbeddedLine, line1: EmbeddedLine) -> bool:
    """
    TODO: Document
    """
    return line0.direction.is_proportional(line1.direction)


def perpendicular(line0: EmbeddedLine, line1: EmbeddedLine) -> bool:
    """
    TODO: Document
    """
    perpendicular_direction = EmbeddedPoint(line0.direction.y, -line0.direction.x)
    return perpendicular_direction.is_proportional(line1.direction)
