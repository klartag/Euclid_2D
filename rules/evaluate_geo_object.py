from .geometry_objects.construction_object import ConstructionObject
from .geometry_objects.equation_object import EquationObject
from .geo_config import get_sympy_objects
from .geometry_objects.parse import parse_geo_object
from .geometry_objects.geo_object import *
import sympy


def evaluate(object, obj_map):
    if object.name in obj_map:
        return obj_map[object.name]
    elif object.type == "Literal":
        return float(object.name)
    elif isinstance(object, ConstructionObject):
        return evaluate_construction(object, obj_map)
    elif isinstance(object, EquationObject):
        return evaluate_equation(object, obj_map)
    else:
        print(object, object.name, obj_map)
        raise NotImplementedError()


def evaluate_equation(object, obj_map):
    return sum(val * evaluate(component, obj_map) for component, val in object.components)


def evaluate_construction(object, obj_map):
    args = [(component.name, evaluate(component, obj_map)) for component in object.components]
    match object.constructor.name:
        case "distance":
            assert len(args) == 2 and all(isinstance(arg[1], sympy.Point2D) for arg in args), str(args)
            obj_map[f"Line({args[0][0]},{args[1][0]})"] = sympy.Line(args[0][1], args[1][1])
            distance = sympy.Point.distance(args[0][1], args[1][1])
            return distance
        case "center":
            assert len(args) == 1 and all(isinstance(arg[1], sympy.Circle) for arg in args), str(args)
            center = args[0][1].center
            return center
        case "radius":
            assert len(args) == 1 and all(isinstance(arg[1], sympy.Circle) for arg in args), str(args)
            radius = args[0][1].radius
            return radius
        case "angle":
            assert len(args) == 3 and all(isinstance(arg[1], sympy.Point2D) for arg in args), str(args)
            line1, line2 = sympy.Line(args[1][1], args[0][1]), sympy.Line(args[1][1], args[2][1])
            name1, name2 = f"Line({args[1][0]}, {args[0][0]})", f"Line({args[1][0]}, {args[2][0]})"
            obj_map[name1] = line1
            obj_map[name2] = line2
            area = sympy.Triangle(args[0][1], args[1][1], args[2][1]).area
            signed_angle = sympy.sign(area) * sympy.Line.angle_between(line1, line2) / sympy.pi * 180
            return signed_angle
        case "Line":
            assert len(args) == 2 and all(isinstance(arg[1], sympy.Point2D) for arg in args), str(args)
            line = sympy.Line(args[0][1], args[1][1])
            obj_map[object.name] = line
            return line
        case "radical_axis":
            assert len(args) == 2 and all(isinstance(arg[1], sympy.Circle) for arg in args), str(args)
            c1, c2 = args[0][1], args[1][1]
            o1, o2 = c1.center, c2.center
            r1, r2 = c1.radius, c2.radius
            d = o1.distance(o2)
            P = ((d**2 + r1**2 - r2**2) / 2 / d**2) * o1 + ((d**2 + r2**2 - r1**2) / 2 / d**2) * o2
            line = sympy.Line(o1, o2)
            obj_map[f"Line({args[0][0]}, {args[1][0]})"] = line
            radical_axis = line.perpendicular_line(P)
            obj_map[object.name] = radical_axis
            return radical_axis
        case "orientation":
            assert len(args) == 3 and all(isinstance(arg[1], sympy.Point2D) for arg in args), str(args)
            triangle = sympy.Triangle(args[0][1], args[1][1], args[2][1])
            return sympy.sign(triangle.area)
        case "exp":
            assert len(args) == 1, str(args)
            return sympy.exp(args[0][1])
        case "log":
            assert len(args) == 1, str(args)
            return sympy.log(args[0][1])
        case "abs":
            assert len(args) == 1, str(args)
            return sympy.Abs(args[0][1])
        case _:
            print(object)
            raise NotImplementedError()


def test_evaluation():
    from .predicates.predicate import Predicate

    obj_map = {
        'A': GeoObject('A', 'Point'),
        'B': GeoObject('B', 'Point'),
        'C': GeoObject('C', 'Point'),
        'D': GeoObject('D', 'Point'),
        'r': GeoObject('r', 'Scalar'),
    }
    geo_object = parse_geo_object('angle(A, B, C) - angle(B, C, D)', obj_map)
    sympy_obj_map, sympy_symbols = get_sympy_objects(obj_map)
    print(geo_object)
    print(sympy_obj_map, sympy_symbols)
    print(evaluate(geo_object, sympy_obj_map))


if __name__ == "__main__":
    test_evaluation()
