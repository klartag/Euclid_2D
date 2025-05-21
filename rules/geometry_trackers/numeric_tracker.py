import itertools
import torch
import warnings
from torch import Tensor

from ..predicates.predicate_factory import predicate_from_args
from ..geometry_objects.construction_object import ConstructionObject
from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.equation_object import EquationObject
from ..predicates.predicate import Predicate
from ..rule_utils import GeoType

from torch_geo.geometry_entities import Circle, Embed, Line, Point, Triangle, det
from torch_geo.imprecise import ImpreciseTensor

ZERO = ImpreciseTensor(torch.tensor(0), torch.tensor(0))
T180 = ImpreciseTensor(torch.tensor(180), torch.tensor(0))
PI = ImpreciseTensor(torch.pi)
T360 = ImpreciseTensor(torch.tensor(180), torch.tensor(0))


def rad_to_degree(rad: ImpreciseTensor) -> ImpreciseTensor:
    """
    Converts radians to degrees.
    """
    return rad * T180 / PI


def small_rem(x: ImpreciseTensor, modulus: ImpreciseTensor) -> ImpreciseTensor:
    res = x % modulus
    return ImpreciseTensor(torch.where(res.mean > modulus.mean / 2, res.mean - modulus.mean, res.mean), res.variance)


class NumericTracker:
    """
    A class to track numeric embeddings of objects.
    It is used to find open predicates, such as "triangle" and "not_in".
    """

    err_prob: Tensor
    embeds: dict[GeoObject, Embed]

    def __init__(self, err_prob: float):
        self.err_prob = torch.tensor(err_prob)
        self.embeds = {}

    def approx_equals(self, a: ImpreciseTensor, b: ImpreciseTensor) -> bool:
        """
        checks if the two floats are approximately equal, up to the numeric precision.
        """
        return torch.all(a.approx_eq(b, self.err_prob)).item()  # type: ignore

    def approx_different(self, a: ImpreciseTensor, b: ImpreciseTensor) -> bool:
        return torch.any(a.approx_ne(b, self.err_prob)).item()  # type: ignore

    def approx_nonzero(self, a: ImpreciseTensor) -> bool:
        return self.approx_different(a, ZERO)

    def _get_predicates_asym(self, obj_1: GeoObject, obj_2: GeoObject) -> list[Predicate]:
        """
        Gets the predicates involving the two objects.
        This function is not guaranteed to find all predicates,
        but should find all of them if called with both (obj_1, obj_2) and (obj_2, obj_1).
        """
        # print(f'Get predicates asym {obj_1} {obj_2}')
        if obj_1 not in self.embeds:
            return []
        if obj_2 not in self.embeds:
            return []
        emb_1 = self.embeds[obj_1]
        emb_2 = self.embeds[obj_2]

        res = []

        match obj_1.type, obj_2.type:
            case GeoType.POINT, GeoType.POINT:
                assert isinstance(emb_1, Point) and isinstance(
                    emb_2, Point
                ), f'_get_predicates_asym received embed {obj_1} => {emb_1} and {obj_2} => {emb_2}'
                if self.approx_nonzero(emb_1.distance_sqr(emb_2)):
                    res.append(predicate_from_args('not_equals', (obj_1, obj_2)))
            case GeoType.POINT, GeoType.LINE:
                assert isinstance(emb_1, Point) and isinstance(
                    emb_2, Line
                ), f'_get_predicates_asym received embed {obj_1} => {emb_1} and {obj_2} => {emb_2}'
                dist = emb_1.line_distance_sqr(emb_2)
                if self.approx_nonzero(emb_1.line_distance_sqr(emb_2)):
                    res.append(predicate_from_args('not_in', (obj_1, obj_2)))
            case GeoType.POINT, GeoType.CIRCLE:
                assert isinstance(emb_1, Point) and isinstance(
                    emb_2, Circle
                ), f'_get_predicates_asym received embed {obj_1} => {emb_1} and {obj_2} => {emb_2}'
                if self.approx_nonzero(emb_2.eval_equation(emb_1)):
                    res.append(predicate_from_args('not_in', (obj_1, obj_2)))
            case GeoType.LINE, GeoType.LINE:
                assert isinstance(emb_1, Line) and isinstance(
                    emb_2, Line
                ), f'_get_predicates_asym received embed {obj_1} => {emb_1} and {obj_2} => {emb_2}'
                if self.approx_nonzero(small_rem(emb_1.angle() - emb_2.angle(), PI)) or self.approx_nonzero(
                    emb_2.p1.line_distance_sqr(emb_1)
                ):
                    # angle_diff = small_rem(emb_1.angle() - emb_2.angle(), PI)
                    # dist = emb_2.p1.line_distance_sqr(emb_1)
                    # print(f'For {obj_1} and {obj_2}: angle_diff=({angle_diff.mean, angle_diff.variance}) dist={dist.mean, dist.variance}')
                    res.append(predicate_from_args('not_equals', (obj_1, obj_2)))
            case GeoType.CIRCLE, GeoType.CIRCLE:
                assert isinstance(emb_1, Circle) and isinstance(
                    emb_2, Circle
                ), f'_get_predicates_asym received embed {obj_1} => {emb_1} and {obj_2} => {emb_2}'
                if self.approx_nonzero(emb_1.center.distance_sqr(emb_2.center)) or self.approx_different(
                    emb_2.radius, emb_1.radius
                ):
                    res.append(predicate_from_args('not_equals', (obj_1, obj_2)))
            case GeoType.SCALAR, GeoType.SCALAR:
                assert isinstance(emb_1, ImpreciseTensor) and isinstance(
                    emb_2, ImpreciseTensor
                ), f'_get_predicates_asym received embed {obj_1} => {emb_1} and {obj_2} => {emb_2}'
                if self.approx_different(emb_1, emb_2):
                    res.append(predicate_from_args('not_equals', (obj_1, obj_2)))
            case GeoType.ANGLE, GeoType.ANGLE:
                assert isinstance(emb_1, ImpreciseTensor) and isinstance(
                    emb_2, ImpreciseTensor
                ), f'_get_predicates_asym received embed {obj_1} => {emb_1} and {obj_2} => {emb_2}'
                # We don't bother with inequalities of angles, since they bloat the system and add nothing of value.
                if isinstance(obj_1, ConstructionObject) and obj_1.constructor.name == 'angle':
                    return []
                if isinstance(obj_2, ConstructionObject) and obj_2.constructor.name == 'angle':
                    return []
                diff = emb_1 - emb_2
                if self.approx_nonzero(small_rem(diff, T360)):
                    res.append(predicate_from_args('not_equals_mod_360', (obj_1, obj_2)))
        # if res:
        #     print(f'Numeric predicates: {res}')
        return res

    def get_pair_predicates(self, obj_1: GeoObject, obj_2: GeoObject):
        """
        Gets all predicates involving the two objects.
        """
        res = self._get_predicates_asym(obj_1, obj_2)
        if obj_1.type != obj_2.type:
            res += self._get_predicates_asym(obj_2, obj_1)
        return res

    def add_object(self, obj: GeoObject, embed: Embed) -> list[Predicate]:
        """
        Adds the embedding of the object.
        """
        match obj.type:
            case GeoType.POINT:
                assert isinstance(embed, Point)
            case GeoType.LINE:
                assert isinstance(embed, Line)
            case GeoType.CIRCLE:
                assert isinstance(embed, Circle)
            case GeoType.SCALAR | GeoType.ANGLE:
                assert isinstance(embed, Tensor)

        self.embeds[obj] = embed

        return self.get_predicates(obj)

    def make_embedding(self, obj: ConstructionObject) -> Embed | None:
        """
        Finds an embedding in R^2 for the given object, assuming that all its components have been embedded,
        and that it is well defined.
        Otherwise, returns None.
        """
        if obj in self.embeds:
            return self.embeds[obj]
        # print(f'Making embedding for {obj}')

        for comp in obj.components:
            if isinstance(comp, ConstructionObject):
                self.make_embedding(comp)

        if any(comp not in self.embeds for comp in obj.components):
            # print('Null components!')
            return None

        arg_embeds = [self.embeds[comp] for comp in obj.components]

        embed: Embed
        match obj.constructor.name:
            case 'midpoint' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Point):
                embed = (arg_embeds[0] + arg_embeds[1]) / 2
            case 'distance' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Point):
                embed = arg_embeds[0].distance(arg_embeds[1])
            case 'Line' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Point):
                embed = Line(arg_embeds[0], arg_embeds[1])
            case 'Circle' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Triangle(arg_embeds[0], arg_embeds[1], arg_embeds[2]).circumcircle()
            case 'circumcenter' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Triangle(arg_embeds[0], arg_embeds[1], arg_embeds[2]).circumcenter()
            case 'center' if isinstance(arg_embeds[0], Circle):
                embed = arg_embeds[0].center
            case 'radius' if isinstance(arg_embeds[0], Circle):
                embed = arg_embeds[0].radius
            case 'angle' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = rad_to_degree(Point.angle_between(arg_embeds[0], arg_embeds[1], arg_embeds[2]))
            case 'exp' if isinstance(arg_embeds[0], ImpreciseTensor):
                embed = arg_embeds[0].exp()
            # case 'log' if isinstance(arg_embeds[0], ImpreciseTensor):
            #     embed = arg_embeds[0].log()
            case 'abs' if isinstance(arg_embeds[0], ImpreciseTensor):
                embed = arg_embeds[0].abs()
            case 'abs_angle' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = rad_to_degree(Point.angle_between(arg_embeds[0], arg_embeds[1], arg_embeds[2]))
                embed = small_rem(embed, T360)
            case 'line_intersection' if isinstance(arg_embeds[0], Line) and isinstance(arg_embeds[1], Line):
                raw_intersection = arg_embeds[0].intersect_line(arg_embeds[1])
                if raw_intersection is None:
                    return
                embed = raw_intersection
            case 'Circle_from_radius' if isinstance(arg_embeds[0], Point) and isinstance(
                arg_embeds[1], ImpreciseTensor
            ):
                embed = Circle(arg_embeds[0], arg_embeds[1])
            case 'parallel_line' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Line):
                embed = Line(arg_embeds[0], arg_embeds[1].p2 - arg_embeds[1].p1 + arg_embeds[0])
            case 'median' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Line(arg_embeds[0], (arg_embeds[1] + arg_embeds[2]) / 2)
            case 'midline' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Line((arg_embeds[0] + arg_embeds[1]) / 2, (arg_embeds[0] + arg_embeds[2]) / 2)
            case 'point_reflection' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Point):
                embed = arg_embeds[1] * 2 - arg_embeds[0]
            case 'line_reflection' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Line):
                proj = arg_embeds[1].projection(arg_embeds[0])
                embed = proj * 2 - arg_embeds[0]
            case 'centroid' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = (arg_embeds[0] + arg_embeds[1] + arg_embeds[2]) / 3
            case 'parallelogram_point' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = arg_embeds[2] + arg_embeds[0] - arg_embeds[1]
            case 'radical_axis' if isinstance(arg_embeds[0], Circle) and isinstance(arg_embeds[1], Circle):
                embed = arg_embeds[0].radical_axis(arg_embeds[1])
            case 'internal_angle_bisector' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Point.internal_bisector(arg_embeds[0], arg_embeds[1], arg_embeds[2])
            case 'external_angle_bisector' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Point.external_bisector(arg_embeds[0], arg_embeds[1], arg_embeds[2])
            case 'incircle' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                a = arg_embeds[0]
                b = arg_embeds[1]
                c = arg_embeds[2]
                embed = Triangle(a, b, c).incircle()
            case 'excircle' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                a = arg_embeds[0]
                b = arg_embeds[1]
                c = arg_embeds[2]
                center = Point.external_bisector(a, b, c).intersect_line(Point.external_bisector(b, c, a))
                if center is None:
                    return

                radius = center.line_distance(Line(a, b))
                embed = Circle(center, radius)
            case 'orientation':
                return None
            case 'projection' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Line):
                embed = arg_embeds[1].projection(arg_embeds[0])
            # case 'line_circle_other_intersection' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Line) and isinstance(arg_embeds[2], Circle):
            #     inters = arg_embeds[1].intersect_circle(arg_embeds[2])
            #     embed = max(inters, key=lambda p: p.distance(arg_embeds[0]))  # type: ignore
            # case 'circle_circle_other_intersection' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Circle) and isinstance(arg_embeds[2], Circle):
            #     inters = arg_embeds[1].intersect_circle(arg_embeds[2])
            #     embed = max(inters, key=lambda p: p.distance(arg_embeds[0]))  # type: ignore
            case 'perpendicular_line' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Line):
                embed = Line(arg_embeds[0], arg_embeds[0] + arg_embeds[1].unit_orthogonal_direction())
            case 'altitude' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Line(arg_embeds[0], arg_embeds[0] + (arg_embeds[2] - arg_embeds[1]).rotate90())
            case 'distance_from_line' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Line):
                embed = arg_embeds[0].line_distance(arg_embeds[1])
            case 'intersection_of_tangents_circles' if isinstance(arg_embeds[0], Circle) and isinstance(
                arg_embeds[1], Circle
            ):
                diff = arg_embeds[1].center - arg_embeds[0].center
                diff *= arg_embeds[0].radius / diff.norm()
                embed = arg_embeds[0].center + diff
            case 'intersection_of_tangent_line_and_circle' if isinstance(arg_embeds[0], Line) and isinstance(
                arg_embeds[1], Circle
            ):
                embed = arg_embeds[0].projection(arg_embeds[1].center)
            case 'nine_points_circle' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                embed = Triangle(
                    (arg_embeds[0] + arg_embeds[1]) / 2,
                    (arg_embeds[1] + arg_embeds[2]) / 2,
                    (arg_embeds[2] + arg_embeds[0]) / 2,
                ).circumcircle()
            case 'perpendicular_bisector' if isinstance(arg_embeds[0], Point) and isinstance(arg_embeds[1], Point):
                embed = Point.perpendicular_bisector(arg_embeds[0], arg_embeds[1])
            case 'orthocenter' if (
                isinstance(arg_embeds[0], Point)
                and isinstance(arg_embeds[1], Point)
                and isinstance(arg_embeds[2], Point)
            ):
                raw_ortho = Triangle(arg_embeds[0], arg_embeds[1], arg_embeds[2]).orthocenter()
                if raw_ortho is None:
                    return None
                embed = raw_ortho
            case 'log':
                # We don't build logs. No need to warn about it.
                return None
            case 'isogonal_conjugate' | 'line_circle_other_intersection' | 'circle_circle_other_intersection':
                warnings.warn(f'Construction "{obj.constructor.name}" not implemented in the numeric checker!')
                return None

            case _:
                warnings.warn(
                    f'Unknown construction "{obj.constructor.name}" with args {[comp.type for comp in obj.components]}!'
                )
                return None
        # print(f'Embedding of {obj}: {embed}')
        self.embeds[obj] = embed
        return embed

    def add_construction(self, obj: GeoObject) -> list[Predicate]:
        """
        Tracks the given objects.
        Returns all nondegeneracy conditions involving the object.
        """
        # print(f'Adding construction {obj}')
        if not isinstance(obj, ConstructionObject):
            return []

        if self.make_embedding(obj) is None:
            # print('Embedding is None!')
            return []

        res = self.get_predicates(obj)
        # print(f'Found predicates: {res}')
        return res

    def points(self) -> list[tuple[GeoObject, Point]]:
        """
        Return all point embeddings.
        """
        return [(obj, embed) for obj, embed in self.embeds.items() if isinstance(embed, Point)]

    def get_predicates(self, obj: GeoObject) -> list[Predicate]:
        """
        Gets all predicates known numerically on the object.
        """
        if obj not in self.embeds:
            return []
        # print(self.embeds)
        res = []
        for other_obj in self.embeds:
            res += self.get_pair_predicates(obj, other_obj)
        # print(f'Numeric predicates found: {res}')
        if obj.type == GeoType.POINT:
            eo = self.embeds[obj]
            assert isinstance(eo, Point)
            for (p1, e1), (p2, e2) in itertools.combinations(self.points(), 2):
                if self.approx_nonzero(det(eo, e1, e2)):
                    res.append(predicate_from_args('not_collinear', (obj, p1, p2)))

        return res

    def is_nonzero(self, eq: EquationObject):
        """
        Checks if the given equation is known to be nonzero.
        """
        ...

    def clone(self) -> 'NumericTracker':
        """
        Returns a deep copy of the numeric tracker.
        """
        res = NumericTracker(self.err_prob.item())
        res.embeds = dict(self.embeds)
        return res
