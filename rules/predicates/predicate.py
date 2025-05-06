from typing import TYPE_CHECKING, Mapping, Optional

from rules.geometry_configuration.torch_geo.geometry_entities import torch_hinge_loss


if TYPE_CHECKING:
    from ..geometry_objects.geo_object import GeoObject
    from ..geometry_configuration.torch_geo.geometry_entities import Point, Line, Circle, Triangle
    from ..geometry_objects.construction_object import Construction
    from .implementations.macro_predicate import MacroData

from ..symmetry import Symmetry
from ..rule_utils import POINT, LINE, SCALAR, ANGLE, ORIENTATION, LITERAL, CIRCLE, union, unpack_dict


# CONSTRUCTIONS: Optional[dict[str, Construction]] = {}
# MACROS: Optional[dict[str, MacroData]] = {}


INPUT_LABEL = 'inputs'
PREPROCESS_LABEL = 'preprocess'
RESULT_PREDICATE_LABEL = 'conclude'
POSS_CONCLUSIONS_LABEL = 'possible_conclusions'

PREDICATE_SIGNATURES = {
    'between': [[POINT, POINT, POINT]],
    'equals': [
        [POINT, POINT],
        [SCALAR, SCALAR],
        [SCALAR, LITERAL],
        [LITERAL, SCALAR],
        [ANGLE, ANGLE],
        [ANGLE, LITERAL],
        [LITERAL, ANGLE],
        [CIRCLE, CIRCLE],
        [LINE, LINE],
        [ORIENTATION, ORIENTATION],
        [ORIENTATION, LITERAL],
        [LITERAL, ORIENTATION],
    ],
    'equals_mod_360': [[ANGLE, ANGLE], [ANGLE, LITERAL], [LITERAL, ANGLE]],
    'not_equals': [
        [POINT, POINT],
        [SCALAR, SCALAR],
        [SCALAR, LITERAL],
        [LITERAL, SCALAR],
        [ANGLE, ANGLE],
        [ANGLE, LITERAL],
        [LITERAL, ANGLE],
        [CIRCLE, CIRCLE],
        [LINE, LINE],
        [ORIENTATION, ORIENTATION],
        [ORIENTATION, LITERAL],
        [LITERAL, ORIENTATION],
        [LITERAL, LITERAL],
    ],
    'not_equals_mod_360': [[ANGLE, ANGLE], [ANGLE, LITERAL], [LITERAL, ANGLE], [LITERAL, LITERAL]],
    'in': [[POINT, LINE], [POINT, CIRCLE]],
    'tangent': [[LINE, CIRCLE], [CIRCLE, CIRCLE]],
    'not_in': [[POINT, LINE], [POINT, CIRCLE]],
    'convex': [[POINT] * 3, [POINT] * 4, [POINT] * 5],
    'not_collinear': [[POINT] * 3],
    'false': [[]],
    'exists': [[POINT], [LINE], [CIRCLE], [SCALAR], [ORIENTATION]],
}


class Predicate:
    """
    A statement on a property of some objects.
    """

    name: str
    """The name of the predicate."""
    components: 'tuple[GeoObject, ...]'
    """The objects to which the predicate applies."""
    symmetry: Symmetry
    """The permutation group acting on the predicate objects that preserves the predicate."""
    signatures: list[list[str]]
    """The possible types of the objects of the predicate."""

    def __init__(self, name: str, objects: 'tuple[GeoObject, ...]', sym=Symmetry.NONE):
        self.name = name
        self.symmetry = sym
        self.components = self.symmetry.canonical_order(objects)

    def is_valid(self) -> bool:
        """
        Checks that the predicate matches a legal signature.
        """
        if self.name not in PREDICATE_SIGNATURES:
            return False
        self_types = [obj.type for obj in self.components]
        return any(sig == self_types for sig in PREDICATE_SIGNATURES[self.name])

    def substitute(self, replacements: 'Mapping[GeoObject, GeoObject]') -> 'Predicate':
        """
        Replaces some of the objects the predicate is applied to with new objects.
        Used when declaring that two objects are equal.

        Parameters:
        * `old_obj`: The object possibly in the predicate.
        * `new_obj`: The object to replace it with.

        Return:

        A predicate with the old object replaced with the new one.
        """
        return Predicate(self.name, tuple(obj.substitute(replacements) for obj in self.components), self.symmetry)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Predicate):
            return False
        return self.name == other.name and self.components == other.components

    def __hash__(self) -> int:
        return hash((self.name, self.components))

    def __repr__(self) -> str:
        return f'{self.name}({", ".join(obj.name for obj in self.components)})'

    def unpack(self) -> 'list[Predicate]':
        """
        Some predicates are not "raw" predicates, but serve as packs of other predicates.
        For example, the predicate between(A, B, C, D) is actually [between(A, B, C), between(B, C, D)].
        @return: A list of all sub-predicates of this predicate.
        """
        return [self]

    def is_open(self) -> bool:
        """
        Checks if a predicate is an "open" predicate, which is almost always satisfied.
        """
        return 'not' in self.name or self.name in ['triangle', 'distinct', 'exists', 'convex', 'acute_triangle']

    def potential(self, torch_obj_map: 'dict[str, Point|Line|Circle|Triangle]', eps: float = 1e-1):
        """
        Returns a differentiable value which is positive for all inputs not satisfying the predicate,
        and zero for those that are.
        @param inputs: A list of the inputs for the predicate.
        """
        import torch
        from ..geometry_configuration.torch_geo.geometry_entities import Point, Line, Circle, Triangle, Tensor
        from ..geometry_configuration.evaluate_geo_object import evaluate

        expr = None
        args = [evaluate(object, torch_obj_map) for object in self.components]
        match self.name:
            case 'equals':
                assert len(args) == 2
                if isinstance(args[0], Tensor) or isinstance(args[1], Tensor):
                    if self.components[0].type == ANGLE or self.components[1].type == ANGLE:
                        loss = torch.abs((args[0] - args[1]) / 180) ** 2  # type: ignore
                    else:
                        loss = torch.abs(args[0] - args[1]) ** 2  # type: ignore
                elif isinstance(args[0], Point):
                    loss = args[0].distance(args[1]) ** 2  # type: ignore
                elif isinstance(args[0], Line):
                    p1, p2 = args[0].points  # type: ignore
                    line = args[1]
                    loss = line.distance(p1) ** 2 + line.distance(p2) ** 2  # type: ignore
                elif isinstance(args[0], Circle):
                    expr = args[0].center.distance(args[1].center)  # type: ignore
                    loss = torch.abs(args[0].radius - args[1].radius) ** 2  # type: ignore
                elif self.components[0].type == ORIENTATION or self.components[1].type == ORIENTATION:
                    expr = args[0] * args[1]  # type: ignore
                    loss = torch_hinge_loss(expr, eps) ** 2  # type: ignore
                else:
                    print(self.name, self.components)
                    raise NotImplementedError()
            case 'not_equals':
                assert len(args) == 2
                if isinstance(args[0], Tensor):
                    expr = torch.abs(args[0] - args[1])
                elif isinstance(args[0], Point):
                    expr = args[0].distance(args[1])  # type: ignore
                elif isinstance(args[0], Line):
                    p1, p2 = args[0].p1, args[0].p2
                    line = args[1]
                    expr = (line.distance(p1) + line.distance(p2)) / 2  # type: ignore
                elif isinstance(args[0], Circle):
                    expr = (args[0].center.distance(args[1].center) + torch.abs(args[0].radius - args[1].radius)) / 2  # type: ignore
                elif self.components[0].type == ORIENTATION:
                    expr = -args[0] * args[1]  # type: ignore
                else:
                    raise NotImplementedError()
                loss = torch_hinge_loss(expr, eps) ** 2  # type: ignore
            case 'equals_mod_360':
                assert len(args) == 2
                device = args[0].device  # type: ignore
                diff = torch.remainder((args[0] - args[1]) / 360, torch.tensor(1, device=device))
                loss = torch.min(diff.abs(), 1 - diff.abs()) ** 2
            case 'not_equals_mod_360':
                assert len(args) == 2
                device = args[0].device  # type: ignore
                diff = torch.remainder((args[0] - args[1]) / 360, torch.tensor(1, device=device))
                expr = torch.min(diff.abs(), 1 - diff.abs()) ** 2
                loss = torch_hinge_loss(expr, eps)  # type: ignore
            case 'collinear':
                assert len(args) == 3 and all(isinstance(arg, Point) for arg in args)
                dist1 = args[0].distance(args[1])
                dist2 = args[1].distance(args[2])
                dist3 = args[0].distance(args[2])
                loss = torch.min(torch.abs(dist1 + dist2 - dist3) ** 2, torch.abs(dist1 + dist3 - dist2) ** 2)
                loss = torch.min(loss, torch.abs(dist2 + dist3 - dist1) ** 2)

                # line = Line(args[0], args[1])  # type: ignore
                # loss = line.distance(args[2]) ** 2  # type: ignore
            case "collinear_and_not_between":
                assert len(args) == 3 and all(isinstance(arg, Point) for arg in args)
                line = Line(args[0], args[1])  # type: ignore
                colinear_loss = line.distance(args[2]) ** 2  # type: ignore

                d1 = args[0].distance(args[1])
                d2 = args[1].distance(args[2])
                d3 = args[0].distance(args[2])
                not_between_loss = torch_hinge_loss(torch.abs(d1 + d2 - d3), eps) ** 2

                loss = colinear_loss + not_between_loss

            case 'concyclic':
                assert len(args) == 4 and all(isinstance(arg, Point) for arg in args)
                triangle = Triangle(args[0], args[1], args[2])  # type: ignore
                circle = triangle.circumcircle()
                center, radius = circle.center, circle.radius
                distance = args[3].distance(center)  # type: ignore
                loss = torch.abs(distance - radius) ** 2
            case 'concurrent':
                assert len(args) == 3 and all(isinstance(arg, Line) for arg in args)
                point = args[0].intersect_line(args[1])  # type: ignore
                distance = args[2].distance(point)  # type: ignore
                loss = distance**2
            case 'between':
                assert len(args) == 3
                assert isinstance(args[0], Point)
                assert isinstance(args[1], Point)
                assert isinstance(args[2], Point)
                d1 = args[0].distance(args[1])
                d2 = args[1].distance(args[2])
                d3 = args[0].distance(args[2])
                loss = torch.abs(d1 + d2 - d3) ** 2
                # v1 = Line(args[0], args[1]).unit_direction()
                # v2 = Line(args[1], args[2]).unit_direction()
                # loss = (1-v1.dot(v2))**2
            case 'midpoint':
                assert len(args) == 3 and all(isinstance(arg, Point) for arg in args)
                mid_point = (args[1] + args[2]) / 2  # type: ignore
                distance = mid_point.distance(args[0])
                loss = distance**2
            case 'triangle' | 'not_collinear':
                assert len(args) == 3
                assert isinstance(args[0], Point)
                assert isinstance(args[1], Point)
                assert isinstance(args[2], Point)
                line1, line2, line3 = Line(args[0], args[1]), Line(args[1], args[2]), Line(args[0], args[2])  # type: ignore
                distance1, distance2, distanc3 = line1.distance(args[2]), line2.distance(args[0]), line3.distance(args[1])  # type: ignore
                loss = torch.square((torch_hinge_loss(distance1, eps) + torch_hinge_loss(distance1, eps) + torch_hinge_loss(distance1, eps)))  # type: ignore
            case "in":
                assert len(args) == 2 and isinstance(args[0], Point)
                if isinstance(args[1], Line):
                    distance = args[1].distance(args[0])
                    loss = distance**2
                elif isinstance(args[1], Circle):
                    distance = args[1].center.distance(args[0])
                    radius = args[1].radius
                    loss = torch.abs(distance - radius) ** 2
            case "not_in":
                assert len(args) == 2 and isinstance(args[0], Point)
                if isinstance(args[1], Line):
                    distance = args[1].distance(args[0])
                    loss = torch_hinge_loss(distance, eps) ** 2  # type: ignore
                elif isinstance(args[1], Circle):
                    distance = args[1].center.distance(args[0])
                    radius = args[1].radius
                    loss = torch_hinge_loss(torch.abs(radius - distance), eps) ** 2  # type: ignore
            case "perpendicular":
                assert len(args) == 2
                assert isinstance(args[0], Line)
                assert isinstance(args[1], Line)
                v1, v2 = args[0].unit_direction(), args[1].unit_direction()
                loss = torch.abs(v1.dot(v2)) ** 2
            case "tangent":
                assert len(args) == 2
                if isinstance(args[0], Line) and isinstance(args[1], Circle):
                    center, radius = args[1].center, args[1].radius
                    distance = args[0].distance(center)
                    loss = torch.abs(distance - radius) ** 2
                elif isinstance(args[0], Circle) and isinstance(args[1], Circle):
                    center1, radius1 = args[0].center, args[0].radius
                    center2, radius2 = args[1].center, args[1].radius
                    distance = center1.distance(center2)
                    possible_losses = [
                        torch.abs(distance - radius1 - radius2),
                        torch.abs(radius1 - distance - radius2),
                        torch.abs(radius2 - distance - radius1),
                    ]
                    loss = torch.min(torch.stack(possible_losses)) ** 2
                else:
                    print(self.name, args)
                    raise NotImplementedError()
            case "parallel":
                assert len(args) == 2 and isinstance(args[0], Line) and isinstance(args[1], Line)
                line1, line2 = args[0], args[1]
                v1, v2 = line1.unit_direction(), line2.unit_direction()
                loss = 100 * torch.min((v1 - v2).norm() ** 2, (v1 + v2).norm() ** 2)
                # angle1, angle2 = line1.line_angle(), line2.line_angle()
                # device = angle1.device  # type: ignore
                # diff = (torch.remainder((angle1 - angle2) / torch.pi, torch.tensor(1, device=device)))
                # loss = torch.min(diff.abs(), 1-diff.abs()) ** 2
            case _:
                raise NotImplementedError(self.name)
        return loss

    def to_language_format(self) -> str:
        """
        Represents the predicate in the language format.
        """
        match self.name:
            case 'equals':
                return f'{self.components[0].to_language_format()} == {self.components[1].to_language_format()}'
            case 'equals_mod_360':
                return f'{self.components[0].to_language_format()} == {self.components[1].to_language_format()} mod 360'
            case 'not_equals':
                return f'{self.components[0].to_language_format()} != {self.components[1].to_language_format()}'
            case 'not_equals_mod_360':
                return f'{self.components[0].to_language_format()} != {self.components[1].to_language_format()} mod 360'
            case 'in':
                if len(self.components) == 2:
                    return f'{self.components[0].to_language_format()} in {self.components[1].to_language_format()}'
                else:
                    idx = 0
                    while self.components[idx].type == POINT:
                        idx += 1
                    return f'{", ".join(comp.to_language_format() for comp in self.components[:idx])} in {", ".join(comp.to_language_format() for comp in self.components[idx:])}'
            case 'not_in':
                return f'{self.components[0].to_language_format()} not in {self.components[1].to_language_format()}'
            case _:
                return f'{self.name}({", ".join(obj.name for obj in self.components)})'

    def involved_objects(self) -> 'set[GeoObject]':
        return union(comp.involved_objects() for comp in self.components)
