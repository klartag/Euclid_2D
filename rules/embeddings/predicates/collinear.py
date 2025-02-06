from ..embedded_objects import EmbeddedPoint

def collinear(point0: EmbeddedPoint, point1: EmbeddedPoint, point2: EmbeddedPoint) -> bool:
    if point0.is_equal(point1) or point0.is_equal(point2):
        return True
    return (point1 - point0).is_proportional(point2 - point0)
