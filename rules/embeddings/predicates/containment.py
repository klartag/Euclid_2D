from typing import Tuple

from ...geometry_objects.geo_type import GeoType

from ..embedded_objects import EmbeddedObject


def _in(*objects: Tuple[EmbeddedObject, ...]) -> bool:
    """
    Given a list of points, and then a list of curves,
    checks whether all of the points lie on the intersection of all of the curves.
    """
    points = [point for point in objects if point._type() == GeoType.POINT]
    curves = [curve for curve in objects if curve not in points]
    return all([curve.contains_point(point) for curve in curves for point in points])


def not_in(*objects: Tuple[EmbeddedObject, ...]) -> bool:
    """
    Given a list of points, and then a list of curves,
    checks whether there exists a point that does *not* lie on the intersection of all of the curves.
    """
    return not _in(*objects)
