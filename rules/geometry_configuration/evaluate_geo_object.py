if __name__ == '__main__':
    # Dealing with path issues.
    from os.path import dirname, abspath
    import sys
    sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

from rules.geometry_objects import construction_object, equation_object
from rules.geometry_objects.eq_op import EqOp
from .torch_geo.geometry_entities import *

from typing import Iterable, Dict, TYPE_CHECKING
import torch


def evaluate(object, obj_map):
    if object.name in obj_map:
        return obj_map[object.name]
    if object.type == "Literal":
        return torch.tensor(float(object.name))
    if isinstance(object, construction_object.ConstructionObject):
        return evaluate_construction(object, obj_map)
    elif isinstance(object, construction_object.EquationObject):
        return evaluate_equation(object, obj_map)
    else:
        print(object, object.name, object.type, type(object))
        raise NotImplementedError()


def evaluate_equation(object, obj_map):
    left = evaluate(object.left, obj_map)
    right = evaluate(object.right, obj_map)
    match object.op:
        case EqOp.ADD:
            return left + right
        case EqOp.SUB:
            return left - right
        case EqOp.MUL:
            return left * right
        case EqOp.DIV:
            return left / right
        case _:
            raise NotImplementedError(object.op)



def evaluate_construction(object, obj_map):
    args = [(component.__repr__(), evaluate(component, obj_map)) for component in object.components]
    match object.constructor.name:
        case "distance":
            assert len(args) == 2 and all(isinstance(arg[1], Point) for arg in args), str(args)
            obj_map[f"Line({args[0][0]},{args[1][0]})"] = Line(args[0][1], args[1][1])
            distance = args[0][1].distance(args[1][1])
            return  distance
        case "distance_from_line":
            assert len(args) == 2 and isinstance(args[0][1], Point) and  isinstance(args[1][1], Line), str(args)
            distance = args[1][1].distance(args[0][1])
            return  distance
        case "midpoint":
            assert len(args) == 2 and all(isinstance(arg[1], Point) for arg in args), str(args)
            point = (args[0][1] + args[1][1]) / 2
            obj_map[f"Midp({args[0][0]}, {args[1][0]})"] = point
            return point
        case "midline":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            point_0 = (args[0][1] + args[1][1]) / 2
            point_1 = (args[1][1] + args[2][1]) / 2
            obj_map[f"Midp({args[0][0]}, {args[1][0]})"] = point_0
            obj_map[f"Midp({args[1][0]}, {args[2][0]})"] = point_1
            line = Line(point_0, point_1)
            return line
        case "center":
            assert len(args) == 1 and all(isinstance(arg[1], Circle) for arg in args), str(args)
            center = args[0][1].center
            return center
        case "radius":
            assert len(args) == 1 and all(isinstance(arg[1], Circle) for arg in args), str(args)
            radius = args[0][1].radius
            return  radius
        case "angle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line1, line2 = Line(args[1][1], args[0][1]), Line(args[1][1], args[2][1])
            name1, name2 = f"Line({args[1][0]}, {args[0][0]})", f"Line({args[1][0]}, {args[2][0]})"
            area = Triangle(args[0][1], args[1][1], args[2][1]).area()
            angle = -1*torch.sign(area)*line1.angle_between(line2) / torch.pi * 180
            return  angle
        case "coangle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line1, line2 = Line(args[1][1], args[0][1]), Line(args[1][1], args[2][1])
            name1, name2 = f"Line({args[1][0]}, {args[0][0]})", f"Line({args[1][0]}, {args[2][0]})"
            area = Triangle(args[0][1], args[1][1], args[2][1]).area()
            angle = -1*torch.sign(area)*line1.angle_between(line2) / torch.pi * 180
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            orientation = torch.sign(-triangle.area())*90
            coangle = angle - orientation
            return  coangle
        case "halfangle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line1, line2 = Line(args[1][1], args[0][1]), Line(args[1][1], args[2][1])
            name1, name2 = f"Line({args[1][0]}, {args[0][0]})", f"Line({args[1][0]}, {args[2][0]})"
            area = Triangle(args[0][1], args[1][1], args[2][1]).area()
            angle = -1*torch.sign(area)*line1.angle_between(line2) / torch.pi * 180
            halfangle = angle / 2
            return  halfangle
        case "abs_angle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line1, line2 = Line(args[1][1], args[0][1]), Line(args[1][1], args[2][1])
            name1, name2 = f"Line({args[1][0]}, {args[0][0]})", f"Line({args[1][0]}, {args[2][0]})"
            angle = torch.abs(line1.angle_between(line2)) / torch.pi * 180
            return  angle
        case "angle_between":
            assert len(args) == 2 and isinstance(args[0][1], Line)
            angle = args[0][1].angle_between(args[1][1]) / torch.pi*180
            #signed_angle = line.slope_sign() * angle
            return angle
        case "direction":
            assert len(args) == 2 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line = Line(args[0][1], args[1][1])
            device = args[0][1].device
            angle = line.line_angle() / torch.pi*180
            signed_angle = line.slope_sign() * angle
            return signed_angle
        case "line_angle":
            assert len(args) == 1 and isinstance(args[0][1], Line)
            line = args[0][1]
            device = line.p1.device
            angle = line.line_angle() / torch.pi*180
            signed_angle = line.slope_sign() * angle
            return signed_angle
        case "Line":
            assert len(args) == 2 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line = Line(args[0][1], args[1][1])
            obj_map[object.name] = line
            return  line

        case "incircle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            obj_map[f"tri({args[0][0]}, {args[1][0]}, {args[2][0]})"] = triangle
            circle = triangle.incircle()
            obj_map[f"incircle({args[0][0]}, {args[1][0]}, {args[2][0]})"] = circle
            return circle
        case "incenter":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            obj_map[f"tri({args[0][0]}, {args[1][0]}, {args[2][0]})"] = triangle
            incenter = triangle.incenter()
            return incenter
        case "excenter":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            obj_map[f"tri({args[0][0]}, {args[1][0]}, {args[2][0]})"] = triangle
            excenter = triangle.excenter()
            return excenter
        case "excircle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            obj_map[f"tri({args[0][0]}, {args[1][0]}, {args[2][0]})"] = triangle
            circle = triangle.excircle()
            return circle
        case "orthocenter":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            obj_map[f"tri({args[0][0]}, {args[1][0]}, {args[2][0]})"] = triangle
            center = triangle.orthocenter()
            obj_map[f"orthocenter({args[0][0]}, {args[1][0]}, {args[2][0]})"] = center
            return center
        
        case "centroid":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            obj_map[f"tri({args[0][0]}, {args[1][0]}, {args[2][0]})"] = triangle
            centroid = triangle.centroid()
            obj_map[f"centroid({args[0][0]}, {args[1][0]}, {args[2][0]})"] = centroid
            return centroid
        
        case "isogonal_conjugate":
            assert len(args) == 4 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[1][1], args[2][1], args[3][1])
            point = args[0][1]
            isogonal_conjugate = triangle.isogonal_conjugate(point)
            return isogonal_conjugate
        
        case "circumcenter":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            circle = triangle.circumcircle()
            obj_map[f"c_{args[0][0]}{args[1][0]}{args[2][0]}"] = circle
            return circle.center

        case "line_intersection":
            assert len(args) == 2 and all(isinstance(arg[1], Line) for arg in args), str(args)
            point = args[0][1].intersect_line(args[1][1])
            obj_map[f"intersec({args[0][0]}, {args[1][0]})"] = point
            return point
        case "intersection_of_tangent_line_and_circle" | "line_circle_tangent_point": 
            assert len(args) == 2 and isinstance(args[0][1], Line) and isinstance(args[1][1], Circle), str(args)
            line, circle = args[0][1], args[1][1]
            intersection_point = line.projection(circle.center)
            obj_map[f"tangent({args[1][0]}, {args[0][0]})"] = intersection_point
            return intersection_point

        case "intersection_of_tangents_circles":
            assert len(args) == 2 and all(isinstance(arg[1], Circle) for arg in args), str(args)
            c1, c2 = args[0][1], args[1][1]
            o1, o2 = c1.center, c2.center
            r1, r2 = c1.radius, c2.radius
            radical_axis = c1.radical_axis(c2)
            intersection_point = radical_axis.projection(o1)
            return intersection_point
        case "power_of_a_point":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], Circle), str(args)
            point, circle = args[0][1], args[1][1]
            center = circle.center
            power_of_a_point = center.distance(point) ** 2 - circle.radius ** 2
            return power_of_a_point

        case "projection":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], Line), str(args)
            point = args[1][1].projection(args[0][1])
            obj_map[f"project({args[1][0]}, {args[0][0]})"] = point
            return point

        case "altitude":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line = Line(args[1][1], args[2][1])
            obj_map[f"Line({args[1][0]}, {args[2][0]})"] = line
            projection = line.projection(args[0][1])
            obj_map[f"project({args[0][0]}, Line({args[1][0]}, {args[2][0]})"] = projection
            altitude = Line(args[0][1], projection)
            obj_map[f"altitude({args[0][0]}, {args[1][0]}, {args[2][0]})"] = altitude
            return altitude
        case "median":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            line = Line(args[1][1], args[2][1])
            obj_map[f"Line({args[1][0]}, {args[2][0]})"] = line
            midpoint = (args[1][1] + args[2][1]) / 2
            obj_map[f"midpoint({args[1][0]}, {args[2][0]})"] = midpoint
            median = Line(args[0][1], midpoint)
            obj_map[f"median({args[0][0]}, {args[1][0]}, {args[2][0]})"] = median
            return median
        
        case "internal_angle_bisector":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            incenter = triangle.incenter()
            line = Line(args[1][1], incenter)
            obj_map[f"bisect({args[0][0]}, {args[1][0]}, {args[2][0]})"] = line
            return line
        case "external_angle_bisector":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            excenter = triangle.excenter()
            line = Line(args[1][1], excenter)
            obj_map[f"ex_bisect({args[0][0]}, {args[1][0]}, {args[2][0]})"] = line
            return line

        case "circle_circle_other_intersection":
            assert len(args) == 3 and isinstance(args[0][1], Point) and isinstance(args[1][1], Circle) and isinstance(args[2][1], Circle), str(args)
            point, c1, c2 = args[0][1], args[1][1], args[2][1]
            center1, center2 = c1.center, c2.center
            other_point = Line(center1, center2).line_reflection(point)
            return other_point

        case "line_circle_other_intersection":
            assert len(args) == 3 and isinstance(args[0][1], Point) and isinstance(args[1][1], Line) and isinstance(args[2][1], Circle), str(args)
            point, line, circle = args[0][1], args[1][1], args[2][1]
            center = circle.center
            projection = line.projection(center)
            other_point = 2*projection - point
            return other_point

        case "line_reflection":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], Line), str(args)
            point = args[1][1].line_reflection(args[0][1])
            obj_map[f"line_reflect({args[0][0]}, {args[1][0]})"] = point
            return point
        case "point_reflection":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], Point), str(args)
            point = args[0][1].point_reflection(args[1][1])
            obj_map[f"point_reflect({args[0][0]}, {args[1][0]})"] = point
            return point
        case "perpendicular_line":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], Line), str(args)
            point = args[1][1].perpendicular_line_at(args[0][1])
            obj_map[f"perpendicular_line({args[0][0]}, {args[1][0]})"] = point
            return point
        case "perpendicular_bisector":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], Point), str(args)
            line = Line(args[0][1], args[1][1]).perpendicular_line_at((args[0][1] + args[1][1])*0.5)
            obj_map[f"line_bisect({args[0][0]}, {args[1][0]})"] = line
            return line
        case "parallel_line":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], Line), str(args)
            line = args[1][1].parallel_line_at(args[0][1])
            obj_map[f"parallel_line({args[0][0]}, {args[1][0]})"] = line 
            return line
        case "radical_axis":
            assert len(args) == 2 and all(isinstance(arg[1], Circle) for arg in args), str(args)
            c1, c2 = args[0][1], args[1][1]
            radical_axis = c1.radical_axis(c2)
            obj_map[object.name] = radical_axis
            return radical_axis
        case "orientation":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            return torch.sign(-triangle.area())*90
        case "Circle_from_radius":
            assert len(args) == 2 and isinstance(args[0][1], Point) and isinstance(args[1][1], torch.Tensor), str(args)
            circle = Circle(args[0][1], args[1][1])
            obj_map[f"Circle({args[0][0]}, {args[1][0]})"] = circle
            return circle
        case "Circle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            circle = triangle.circumcircle()
            obj_map[f"c_{args[0][0]}{args[1][0]}{args[2][0]}"] = circle
            return circle
        case "nine_points_circle":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            A, B, C = args[0][1], args[1][1], args[2][1]
            circle = Triangle((A+B)/2, (B+C)/2, (C+A)/2).circumcircle()
            return circle
        case "euler_line":
            assert len(args) == 3 and all(isinstance(arg[1], Point) for arg in args), str(args)
            triangle = Triangle(args[0][1], args[1][1], args[2][1])
            center1 = triangle.circumcenter()
            center2 = triangle.orthocenter()
            return Line(center1, center2)
        case "exp":
            assert len(args) == 1, str(args)
            return torch.exp(args[0][1])
        case "log":
            assert len(args) == 1, str(args)
            return torch.log(args[0][1])
        case "abs":
            assert len(args) == 1, str(args)
            return torch.abs(args[0][1])
        case _:
            raise NotImplementedError(object.constructor.name)
        

def test_evaluation():
    from rules.predicate import Predicate
    from rules.geo_config import GeoConfig
    from rules import geo_object
    
    obj_map = {
        'A': geo_object.GeoObject('A', 'Point'),
        'B': geo_object.GeoObject('B', 'Point'),
        'C': geo_object.GeoObject('C', 'Point'),
        'D': geo_object.GeoObject('D', 'Point'),
        'r': geo_object.GeoObject('r', 'Scalar'),
    }

    geo_object = geo_object.GeoObject.parse('angle(A, B, C) - angle(B, C, D)', obj_map)
    config = GeoConfig(obj_map, [])
    params = torch.randn(config.num_params, device='cpu')
    torch_obj_map = config.get_torch_objects(params)
    print(geo_object)
    print(torch_obj_map, params)
    print(evaluate(geo_object, torch_obj_map))

if __name__ == "__main__":
    test_evaluation()