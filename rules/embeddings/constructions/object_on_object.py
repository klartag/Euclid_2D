from typing import Sequence, Tuple
from mpmath import mp
from random import uniform

from ..embedded_objects import EmbeddedPoint, EmbeddedLine, EmbeddedCircle, EmbeddedObject
from ..predicates.tangent import tangent

from .new_object import new_point
from .projection import project

def line_on_point(objects: Sequence[EmbeddedObject], point: EmbeddedPoint) -> Tuple[EmbeddedLine]:
    # TODO: Return multiple lines dep. on which lines already exist through the point.
    return (EmbeddedLine(point, new_point()),)

def point_on_circle(objects: Sequence[EmbeddedObject], circle: EmbeddedCircle) -> Tuple[EmbeddedPoint]:
    points = [point for point in objects if isinstance(point, EmbeddedPoint)]
    points_on_circle = [point for point in points if circle.contains_point(point)]

    result_angles = []
    
    if len(points_on_circle) > 0:
        angles = [mp.atan2(point.y - circle.center.y, point.x - circle.center.x) for point in points_on_circle]
        angles.sort()
        angles.append(angles[0] + 2 * mp.pi)
        
        for i in range(len(angles) - 1):
            start, end = angles[i:i+2]
            near_start = start * 0.9 + end * 0.1
            near_end = start * 0.1 + end * 0.9
            result_angles.extend([
                uniform(start, near_start),
                uniform(near_start, near_end),
                uniform(near_end, end)
            ])
    else:
        result_angles.append(uniform(0, 2 * mp.pi))
    
    return tuple([circle.center + EmbeddedPoint(mp.cos(angle), mp.sin(angle)).scale(circle.radius_squared ** 0.5) for angle in result_angles])

def point_on_line(objects: Sequence[EmbeddedObject], line: EmbeddedLine) -> Tuple[EmbeddedPoint]:
    points = [point for point in objects if isinstance(point, EmbeddedPoint)] \
        + [project(circle.center, line) for circle in objects if isinstance(circle, EmbeddedCircle) and tangent(line, circle)]
    
    points_on_line = [point for point in points if line.contains_point(point)]

    all_positions = [line.direction.scalar_product(point - line.point) / line.direction.length_squared() for point in points]
    positions_on_line = [line.direction.scalar_product(point - line.point) / line.direction.length_squared() for point in points_on_line]
    positions_on_line.extend([0, 1])
    if len(all_positions) > 0:
        max_position = max(all_positions)
        min_position = min(all_positions)
        positions_on_line.extend([2 * max_position - min_position, 2 * min_position - max_position])
    positions_on_line = list(set(positions_on_line))
    positions_on_line.sort()
    
    result_positions = []
    for i in range(len(positions_on_line) - 1):
        start, end = positions_on_line[i:i+2]
        result_positions.append(uniform(start * 0.1 + end * 0.9, start * 0.9 + end * 0.1))
    for i in range(1, len(positions_on_line) - 1):
        end_0, start, end_1 = positions_on_line[i-1:i+2]
        result_positions.append(uniform(start, start * 0.9 + end_0 * 0.1))
        result_positions.append(uniform(start, start * 0.9 + end_1 * 0.1))
    
    return tuple([line.point + line.direction.scale(position) for position in result_positions])
