from ..embedded_objects import EmbeddedLine, EmbeddedCircle, EPSILON

from ..embedded_objects.embedded_curve import EmbeddedCurve

from ..constructions.projection import project


def tangent(curve0: EmbeddedCurve, curve1: EmbeddedCurve) -> bool:
    if isinstance(curve0, EmbeddedCircle) and isinstance(curve1, EmbeddedCircle):
        return circle_tangency(curve0, curve1)
    elif isinstance(curve0, EmbeddedLine) and isinstance(curve1, EmbeddedCircle):
        return line_tangency(curve0, curve1)
    elif isinstance(curve0, EmbeddedCircle) and isinstance(curve1, EmbeddedLine):
        return line_tangency(curve1, curve0)
    else:
        raise Exception(f"Tangency undefined for {curve0._type()} and {curve1._type()}")


def circle_tangency(circle0: EmbeddedCircle, circle1: EmbeddedCircle) -> bool:
    center_distance = (circle0.center - circle1.center).length()
    radius0 = circle0.radius_squared ** 0.5
    radius1 = circle1.radius_squared ** 0.5    
    return abs(radius0 + radius1 - center_distance) < EPSILON or abs(abs(radius0 - radius1) - center_distance) < EPSILON


def line_tangency(line: EmbeddedLine, circle: EmbeddedCircle) -> bool:
    return abs((project(circle.center, line) - circle.center).length_squared() - circle.radius_squared) < EPSILON**2
