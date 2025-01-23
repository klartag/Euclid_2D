if __name__ == '__main__':
    # Dealing with path issues.
    from os.path import dirname, abspath
    import sys
    sys.path.append(dirname(dirname(abspath(__file__))))


import functools
import torch
from torch import Tensor, tensor
from typing import Generic, TypeVar, Union

from rules.rule_utils import split_args
from .imprecise import ImpreciseTensor

PI = torch.tensor(torch.pi)

T = TypeVar('T', Tensor, ImpreciseTensor)

def torch_hinge_loss(x, eps=0.1):
    return torch.relu(eps-x)

def stable_sqrt(x):
    return torch.sqrt(x + 1e-12)


def det(p1: 'Point[T]', p2: 'Point[T]', p3: 'Point[T]') -> T:
    """
    Computes the determinant of (p2-p1) and (p3 - p1).
    """
    d1 = p2 - p1
    d2 = p3 - p1
    return d1.x * d2.y - d1.y * d2.x

class Point(Generic[T]):
    x: T
    y: T

    def __init__(self, x: T, y: T, device=None):
        self.x = x
        self.y = y

        if isinstance(self.x, Union[float, int]):
            self.x = torch.FloatTensor(self.x)
        if isinstance(self.y, Union[float, int]):
            self.y = torch.FloatTensor(self.y)
        

        if device is not None:
            self.x = self.x.to(device)
            self.y = self.y.to(device)
            self.device = device
        else:
            self.device = self.x.device

    def distance_sqr(self, other: 'Point[T]') -> T:
        px, py = other.x, other.y
        return ((self.x - px)**2 + (self.y - py)**2)
    

    def distance(self, other: 'Point[T]') -> T:
        return self.distance_sqr(other).sqrt()
    
    def norm(self) -> T:
        return (self.x**2 + self.y**2).sqrt()

    def dot(self, other: 'Point[T]') -> T:
        return self.x * other.x + self.y * other.y

    def __add__(self, other: 'Point[T]') -> 'Point[T]':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point[T]') -> 'Point[T]':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, l: Union[float,T]) -> 'Point[T]':
        if isinstance(l, Tensor):
            assert l.numel() == 1, str(l.numel())
        return Point(self.x*l, self.y*l)
    
    def __rmul__(self, l: Union[float,T]) -> 'Point[T]':
        if isinstance(l, Tensor):
            assert l.numel() == 1, str(l.numel())
        return Point(self.x*l, self.y*l)
    
    def __truediv__(self, l: Union[float,T]):
        if isinstance(l, Tensor):
            assert l.numel() == 1, str(l.numel()) + str(l)
        return Point(self.x/l, self.y/l)
    
    def line_distance_sqr(self, other: 'Line[T]') -> T:
        return self.distance_sqr(other.projection(self))
    
    def line_distance(self, other: 'Line[T]') -> T:
        return self.distance(other.projection(self))

    def angle(self) -> T:
        return self.y.atan2(self.x)

    def rotate(self, rad_angle: T) -> 'Point[T]':
        """
        Rotates the point by the given angle in radians.
        """
        return Point(self.x * rad_angle.cos() - self.y * rad_angle.sin(), self.x * rad_angle.sin() + self.y * rad_angle.cos())

    def rotate90(self) -> 'Point[T]':
        neg_y = -self.y
        assert isinstance(neg_y, type(self.y))
        return Point(neg_y, self.x)

    def reflect(self, center: 'Point[T] | Line[T]') -> 'Point[T]':
        """
        Computes the reflection of `self` around `center`.
        """
        if isinstance(center, Point):
            return center * 2 - self
        else:
            proj = center.projection(self)
            return proj * 2 - self

    @staticmethod
    def angle_between(p1: 'Point[T]', p2: 'Point[T]', p3: 'Point[T]') -> T:
        return (p3 - p2).angle() - (p1 - p2).angle()
    
    @staticmethod
    def internal_bisector(p1: 'Point[T]', p2: 'Point[T]', p3: 'Point[T]') -> 'Line[T]':
        angle = Point.angle_between(p1, p2, p3)
        return Line(p2, (p1 - p2).rotate(angle / 2) + p2)
    
    @staticmethod
    def external_bisector(p1: 'Point[T]', p2: 'Point[T]', p3: 'Point[T]') -> 'Line[T]':
        angle = Point.angle_between(p1, p2, p3) + PI
        return Line(p2, (p1 - p2).rotate(angle / 2) + p2)
    @staticmethod
    def perpendicular_bisector(p1: 'Point[T]', p2: 'Point[T]') -> 'Line[T]':
        mid = (p1 + p2) / 2
        return Line(mid, mid + (p2 - p1).rotate90())
    
    @staticmethod
    def parse_imprecise(s: str) -> 'Point[ImpreciseTensor]':
        """
        Parses a point, in either the format `(x, y)` or `x, y`
        """
        s = s.strip()
        if s[0] == '(':
            if s[-1] != ')':
                raise ValueError(f'Failed to parse point: {s}')
            s = s[1:-1]
        x, y = split_args(s)
        return Point(ImpreciseTensor(float(x)), ImpreciseTensor(float(y)))
    
    def to_language_format(self) -> str:
        return f'({self.x}, {self.y})'
    def __repr__(self) -> str:
        return self.to_language_format()
    


class Line(Generic[T]):
    p1: Point[T]
    p2: Point[T]

    def __init__(self, p1: Point[T], p2: Point[T]):
        self.p1 = p1
        self.p2 = p2

    @property
    def points(self):
        return self.p1, self.p2
    
    def slope_sign(self) -> Tensor:
        return torch.sign((self.p1.x - self.p2.x)*(self.p1.y - self.p2.y))

    def equation_coefficients(self) -> tuple[T, T, T]:
        return self.p1.y - self.p2.y, self.p2.x - self.p1.x, self.p1.x*self.p2.y - self.p1.y*self.p2.x
    
    def eval_equation(self, other: Point[T]) -> T:
        px, py = other.x, other.y
        a, b, c = self.equation_coefficients()
        return a*px + b*py + c

    def direction(self) -> Point[T]:
        return self.p2 - self.p1
    
    def unit_direction(self) -> Point[T]:
        v = self.p2 - self.p1
        return v / v.norm()

    def unit_orthogonal_direction(self) -> Point[T]:
        return self.unit_direction().rotate90()

    def distance(self, other: Point[T]) -> T:
        px, py = other.x, other.y
        a, b, c = self.equation_coefficients()

        return (a*px + b*py + c).abs() / (a**2 + b**2).sqrt()

    def projection(self, other: Point[T]) -> Point[T]:
        px, py = other.x, other.y
        a, b, c = self.equation_coefficients()
        x = (b*(b*px - a*py) - a*c) / (a**2 + b**2)
        y = (a*(-b*px + a*py) - b*c) / (a**2 + b**2)
        return Point(x, y)


    def intersect_line(self, other: 'Line[T]') -> Point[T]:
        x1, y1, x2, y2 = self.p1.x, self.p1.y, self.p2.x, self.p2.y, 
        x3, y3, x4, y4 = other.p1.x, other.p1.y, other.p2.x, other.p2.y

        x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
        y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))

        return Point(x, y)

    def perpendicular_line_at(self, other: Point[T]) -> 'Line[T]':
        return Line(other, self.unit_orthogonal_direction() + other)

    def parallel_line_at(self, other: Point[T]) -> 'Line[T]':
        return Line(other, other + self.unit_direction())

    def angle_between(self, other: 'Line[T]') -> T:
        v1, v2 = self.unit_direction(), other.unit_direction()
        return v1.dot(v2).acos()
    
    def smallest_angle_between(self, other: 'Line[T]') -> T:
        v1, v2 = self.unit_direction(), other.unit_direction()
        return v1.dot(v2).abs().acos()

    def line_angle(self) -> Tensor:
        v = self.unit_direction()
        return torch.acos(v.x)

    def line_reflection(self, point: Point) -> Point:
        mid_point = self.projection(point)
        return mid_point*2 - point

    @staticmethod
    def parse_imprecise(s: str) -> 'Line[ImpreciseTensor]':
        """
        Parses a line, in either the format `(p1, p2)` or `p1, p2`
        """
        s = s.strip()
        if s[0] == '(':
            if s[-1] != ')':
                raise ValueError(f'Failed to parse line: {s}')
            s = s[1:-1]
        p1, p2 = split_args(s)
        return Line(Point.parse_imprecise(p1), Point.parse_imprecise(p2))

    def to_language_format(self) -> str:
        return f'({self.p1}, {self.p2})'
    def __repr__(self) -> str:
        return self.to_language_format()

    def intersect_circle(self, c: 'Circle[T]') -> tuple[Point[T], Point[T]]:
        """
        This method generally requires IFs.
        I currently just return NaNs for the illegal points.
        """
        p = self.projection(c.center)
        dir = self.unit_direction()

        rem_norm = (c.radius**2 - p.distance(c.center)**2).sqrt()

        dir = dir * rem_norm

        return (p + dir, p - dir)
        

class Triangle(Generic[T]):
    p1: Point[T]
    p2: Point[T]
    p3: Point[T]

    def __init__(self, p1: Point[T], p2: Point[T], p3: Point[T]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self._circumcenter = None

    def area(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        return (x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2) / 2

    @functools.cache
    def circumcenter(self) -> Point[T]:
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        x = ((x1 + x2)*(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2)/2 + (y1 - y2)*(x1*x2 - x1*x3 - x2*x3 + x3**2 + y1*y2 - y1*y3 - y2*y3 + y3**2)/2)/(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2)
        y = (-(x1 - x2)*(x1*x2 - x1*x3 - x2*x3 + x3**2 + y1*y2 - y1*y3 - y2*y3 + y3**2)/2 + (y1 + y2)*(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2)/2)/(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2)
        return Point(x, y)

    def circumcircle(self) -> 'Circle[T]':
        center = self.circumcenter()
        radius = self.p1.distance(center)

        return Circle(center, radius)

    def altitudes(self) -> list[Line]:
        altitudes = [Line(self.p2, self.p3).perpendicular_line_at(self.p1), 
                     Line(self.p3, self.p1).perpendicular_line_at(self.p2),
                     Line(self.p1, self.p2).perpendicular_line_at(self.p3)]
        return altitudes

    def orthocenter(self) -> Point[T] | None:
        alts = self.altitudes()
        res = alts[0].intersect_line(alts[1])
        return res
    


    def incenter(self) -> Point[T]:
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y

        px = (x1*((x2 - x3)**2 + (y2 - y3)**2).sqrt() + x2*((x1 - x3)**2 + (y1 - y3)**2).sqrt() + x3*((x1 - x2)**2 + (y1 - y2)**2).sqrt())/(((x1 - x2)**2 + (y1 - y2)**2).sqrt() + ((x1 - x3)**2 + (y1 - y3)**2).sqrt() + ((x2 - x3)**2 + (y2 - y3)**2).sqrt())
        py = (y1*((x2 - x3)**2 + (y2 - y3)**2).sqrt() + y2*((x1 - x3)**2 + (y1 - y3)**2).sqrt() + y3*((x1 - x2)**2 + (y1 - y2)**2).sqrt())/(((x1 - x2)**2 + (y1 - y2)**2).sqrt() + ((x1 - x3)**2 + (y1 - y3)**2).sqrt() + ((x2 - x3)**2 + (y2 - y3)**2).sqrt())
        return Point(px, py)

    def excenter(self) -> Point[T]:
        A, B, C = self.p1, self.p2, self.p3
        a, b, c = B.distance(C), A.distance(C), A.distance(B)
        excenter = (b*B + c*C - a*A) / (b + c - a)

        return excenter
    
    def centroid(self) -> Point[T]:
        return (self.p1 + self.p2 + self.p3)/3


    def incircle(self) -> 'Circle[T]':
        center = self.incenter()
        radius = center.distance(Line(self.p1, self.p2).projection(center))

        return Circle(center, radius)

    def excircle(self) -> 'Circle[T]':
        excenter = self.excenter()
        radius = Line(self.p1, self.p2).distance(excenter)
        return Circle(excenter, radius)
    
    def incircle_tangent_points(self) -> list[Point]:
        center = self.incenter()
        tangent_points = [Line(self.p1, self.p2).projection(center),
                          Line(self.p2, self.p3).projection(center),
                          Line(self.p3, self.p1).projection(center)]
        return tangent_points
    
    def isogonal_conjugate(self, point: Point[T]) -> Point[T]:
        """
        Computes the isogonal conjugate of the given point with respect to `self`.
        """
        b2 = Point.internal_bisector(self.p1, self.p2, self.p3)
        b3 = Point.internal_bisector(self.p1, self.p3, self.p2)

        r2 = point.reflect(b2)
        r3 = point.reflect(b3)

        res = Line(self.p2, r2).intersect_line(Line(self.p3, r3))
        assert res is not None
        return res



class Circle(Generic[T]):
    center: Point[T]
    radius: T

    def __init__(self, center: Point[T], radius: T):
        self.center = center
        self.radius = radius

    def eval_equation(self, other: Point[T]):
        return other.distance_sqr(self.center) - self.radius**2

    def circumference(self) -> T:
        return self.radius * (2 * torch.pi)
    
    def radical_axis(self, other: 'Circle[T]') -> Line[T]:
        """
        The line where the power of points with respect to the two circles are equal.
        """
        a = (other.center.x - self.center.x) * 2
        b = (other.center.y - self.center.y) * 2
        c = self.center.x**2 + self.center.y**2 - self.radius**2 - other.center.x**2 - other.center.y**2 +other.radius**2
        # When the line is not x == k
        zero = self.center.x * 0
        one = zero + 1
        
        p1 = Point(zero, -c/b)
        p2 = Point(one, -(c + a)/b)

        return Line(p1, p2)

    @staticmethod
    def parse(s: str) -> 'Circle[ImpreciseTensor]':
        """
        Parses a circle, in either the format `(p1, r)` or `p1, r`
        """
        s = s.strip()
        if s[0] == '(':
            if s[-1] != ')':
                raise ValueError(f'Failed to parse circle: {s}')
            s = s[1:-1]
        p, r = split_args(s)
        return Circle(Point.parse_imprecise(p), ImpreciseTensor(float(r)))

    def to_language_format(self) -> str:
        return f'({self.center}, {self.radius})'
    
    def __repr__(self) -> str:
        return self.to_language_format()

    def intersect_line(self, l: Line[T]) -> tuple[Point[T], Point[T]]:
        return l.intersect_circle(self)
    
    def intersect_circle(self, c: 'Circle[T]') -> tuple[Point[T], Point[T]]:
        diff = c.center - self.center
        d = diff.norm()

        a_minus_b = (self.radius**2 - c.radius**2) / d
        a = (a_minus_b + d) / 2
        h = (self.radius**2 - a**2).sqrt()
        diff /= diff.norm()

        return (
            self.center + diff * a + diff.rotate90() * h,
            self.center + diff * a - diff.rotate90() * h,
        )
    
Embed = Point[ImpreciseTensor] | Line[ImpreciseTensor] | Circle[ImpreciseTensor] | ImpreciseTensor


def main():
    """
    Manually testing the geometric constructions.
    """
    p1 = Point(ImpreciseTensor(-0.7051842212677002), ImpreciseTensor(0.942358672618866))
    p2 = Point(ImpreciseTensor(0.3496091067790985), ImpreciseTensor( -1.1898506879806519))
    p3 = Point(ImpreciseTensor(-0.35358646512031555), ImpreciseTensor(0.23162223398685455))

    l = Line(p2, p1)
    d = p3.line_distance(l)
    print(d.mean, d.variance)


if __name__ == '__main__':
    main()