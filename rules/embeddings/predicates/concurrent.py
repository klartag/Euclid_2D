from ..embedded_objects import EmbeddedLine

from ..constructions.line_intersection import line_intersection


def concurrent(line0: EmbeddedLine, line1: EmbeddedLine, line2: EmbeddedLine) -> bool:
    """
    TODO: Document
    """
    if line0.is_equal(line1) or line0.is_equal(line2) or line1.is_equal(line2):
        return True

    intersection = line_intersection(line0, line1)

    if intersection is None:
        return False

    return line2.contains_point(intersection)
