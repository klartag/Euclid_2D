from ..embedded_objects import EmbeddedPoint

from ..constructions.parallels_and_perpendiculars import perpendicular_bisector

from .concurrent import concurrent


def concyclic(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> bool:
    if point1.is_equal(point2) or point1.is_equal(point3) or point2.is_equal(point3):
        return True
    
    perpendicular_bisector_0 = perpendicular_bisector(point0, point1)
    perpendicular_bisector_1 = perpendicular_bisector(point0, point2)
    perpendicular_bisector_2 = perpendicular_bisector(point0, point3)
    
    if perpendicular_bisector_0 is None or perpendicular_bisector_1 is None or perpendicular_bisector_2 is None:
        return False
    
    return concurrent(perpendicular_bisector_0, perpendicular_bisector_1, perpendicular_bisector_2)
