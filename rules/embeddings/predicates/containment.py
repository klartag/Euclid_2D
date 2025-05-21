from typing import Tuple

from ...rule_utils import GeoType

from ..embedded_objects import EmbeddedObject


def _in(*objects: Tuple[EmbeddedObject, ...]) -> bool:
    points = [point for point in objects if point._type() == GeoType.POINT]
    curves = [curve for curve in objects if curve not in points]
    return all([curve.contains_point(point) for curve in curves for point in points])


def not_in(*objects: Tuple[EmbeddedObject, ...]) -> bool:
    return not _in(*objects)
