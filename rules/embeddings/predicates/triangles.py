from ..embedded_objects import EmbeddedPoint, EPSILON
from ..constructions.scalars import orientation

from .collinear import collinear

def isosceles_triangle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> bool:
    if collinear(point0, point1, point2):
        return False
    return abs((point0 - point1).length_squared() - (point0 - point2).length_squared()) < EPSILON**2


def congruent_without_orientation(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint, point4: EmbeddedPoint, point5: EmbeddedPoint) -> bool:
    if collinear(point0, point1, point2) or collinear(point3, point4, point5):
        return False
    if abs((point0 - point1).length_squared() - (point3 - point4).length_squared()) > EPSILON**2:
        return False
    if abs((point1 - point2).length_squared() - (point4 - point5).length_squared()) > EPSILON**2:
        return False
    if abs((point2 - point0).length_squared() - (point5 - point3).length_squared()) > EPSILON**2:
        return False
    return True


def congruent_triangles(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint, point4: EmbeddedPoint, point5: EmbeddedPoint) -> bool:
    if not congruent_without_orientation(point0, point1, point2, point3, point4, point5):
        return False
    return orientation(point0, point1, point2).is_equal(orientation(point3, point4, point5))


def anti_congruent_triangles(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint, point4: EmbeddedPoint, point5: EmbeddedPoint) -> bool:
    if not congruent_without_orientation(point0, point1, point2, point3, point4, point5):
        return False
    return not orientation(point0, point1, point2).is_equal(orientation(point3, point4, point5))


def similar_without_orientation(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint, point4: EmbeddedPoint, point5: EmbeddedPoint) -> bool:
    if collinear(point0, point1, point2) or collinear(point3, point4, point5):
        return False
    ratio0 = (point0 - point1).length_squared() / (point3 - point4).length_squared()
    ratio1 = (point1 - point2).length_squared() / (point4 - point5).length_squared()
    ratio2 = (point2 - point0).length_squared() / (point5 - point3).length_squared()
    return abs(ratio0 - ratio1) < EPSILON and abs(ratio1 - ratio2) < EPSILON


def similar_triangles(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint, point4: EmbeddedPoint, point5: EmbeddedPoint) -> bool:
    if not similar_without_orientation(point0, point1, point2, point3, point4, point5):
        return False
    return orientation(point0, point1, point2).is_equal(orientation(point3, point4, point5))


def anti_similar_triangles(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint, point4: EmbeddedPoint, point5: EmbeddedPoint) -> bool:
    if not similar_without_orientation(point0, point1, point2, point3, point4, point5):
        return False
    return not orientation(point0, point1, point2).is_equal(orientation(point3, point4, point5))
