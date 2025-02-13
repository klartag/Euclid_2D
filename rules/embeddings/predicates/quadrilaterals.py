from ..embedded_objects import EmbeddedPoint, EPSILON

from ..constructions.line import line
from ..constructions.parallels_and_perpendiculars import perpendicular_bisector

from .collinear import collinear
from .line_relations import parallel, perpendicular
from .concyclic import concyclic


def trapezoid(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> bool:
    if collinear(point0, point1, point2):
        return False
    
    base0 = line(point0, point1)
    base1 = line(point2, point3)
    
    if base0 is None or base1 is None:
        return False
    
    return parallel(base0, base1)


def isosceles_trapezoid(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> bool:
    return trapezoid(point0, point1, point2, point3) and concyclic(point0, point1, point2, point3)


def parallelogram(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> bool:
    if collinear(point0, point1, point2):
        return False
    
    line01 = line(point0, point1)
    line12 = line(point1, point2)
    line23 = line(point2, point3)
    line30 = line(point3, point0)
    
    if line01 is None or line12 is None or line23 is None or line30 is None:
        return False
    
    return parallel(line01, line23) and parallel(line12, line30)


def rhombus(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> bool:
    perpendicular_bisector02 = perpendicular_bisector(point0, point2)
    perpendicular_bisector13 = perpendicular_bisector(point1, point3)
    
    diagonal02 = line(point0, point2)
    diagonal13 = line(point1, point3)
    
    if perpendicular_bisector02 is None or perpendicular_bisector13 is None or diagonal02 is None or diagonal13 is None:
        return False
    
    return diagonal02.is_equal(perpendicular_bisector13) and diagonal13.is_equal(perpendicular_bisector02)


def rectangle(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> bool:
    line01 = line(point0, point1)
    line12 = line(point1, point2)
    if line01 is None or line12 is None:
        return False
    
    return parallelogram(point0, point1, point2, point3) and perpendicular(line01, line12)


def square(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint, point3: EmbeddedPoint) -> bool:
    return rectangle(point0, point1, point2, point3) and rhombus(point0, point1, point2, point3)
