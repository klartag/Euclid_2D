if __name__ == '__main__':
    # Dealing with path issues.
    from os.path import dirname, abspath
    import sys

    sys.path.append(dirname(dirname(abspath(__file__))))


from torch_geo.geometry_entities import Circle, Line, Point, det
import torch
from torch import tensor, Tensor

prec = tensor(1e-4)


def approx_equals(t1: Tensor, t2: Tensor | float) -> bool:
    return bool(torch.all(torch.abs(t1 - t2) < prec).item())


def random_point():
    return Point(torch.rand(()), torch.rand(()))


def rad_angle_distance(a1: Tensor, a2: Tensor):
    diff = (a2 - a1) % (2 * torch.pi)
    return torch.where(diff > torch.pi, diff - 2 * torch.pi, diff)


def test_distance_example():
    a = Point(tensor(0), tensor(0))
    b = Point(tensor(3), tensor(4))
    assert approx_equals(a.distance(b), 5)


def test_project():
    for _ in range(100):
        a = random_point()
        b = random_point()
        c = random_point()
        l = Line(b, c)
        p = l.projection(a)

        assert approx_equals(p.line_distance(l), 0)
        assert approx_equals((a - p).dot(b - p), 0)


def test_bisector():
    for _ in range(100):
        a = random_point()
        b = random_point()
        c = random_point()
        l = Point.internal_bisector(a, b, c)
        assert approx_equals(b.line_distance(l), 0), f'B is not on the angle bisector: {b.line_distance(l)}'

        p = l.projection(c)
        ctag = p * 2 - c
        assert approx_equals(det(ctag, b, a), 0), f"{a}, {b} {ctag} are not collinear: {det(ctag, b, a)}"

    for _ in range(100):
        a = random_point()
        b = random_point()
        c = random_point()
        l = Point.external_bisector(a, b, c)
        assert approx_equals(b.line_distance(l), 0), f'B is not on the angle bisector: {b.line_distance(l)}'

        p = l.projection(c)
        ctag = p * 2 - c
        assert approx_equals(det(ctag, b, a), 0), f"{a}, {b} {ctag} are not collinear: {det(ctag, b, a)}"


def test_distance():
    for _ in range(1000):
        a = random_point()
        l = Line(random_point(), random_point())
        assert approx_equals(a.line_distance(l), l.distance(a))


def test_line_intersect():
    for _ in range(1000):
        l1 = Line(random_point(), random_point())
        l2 = Line(random_point(), random_point())

        if l1.smallest_angle_between(l2) > 0.01:
            p = l1.intersect_line(l2)
            assert approx_equals(
                l1.distance(p), 0
            ), f'Point {p} not on line {l1} (angle={l1.smallest_angle_between(l2)})!'
            assert approx_equals(
                l2.distance(p), 0
            ), f'Point {p} not on line {l2} (angle={l1.smallest_angle_between(l2)})!'


def test_line_circle_intersect():
    for _ in range(1000):
        l = Line(random_point(), random_point())
        center = random_point()
        rad = l.distance(center)
        rad += torch.abs(torch.randn_like(rad))
        c = Circle(center, rad)

        p1, p2 = l.intersect_circle(c)
        assert approx_equals(p1.line_distance(l), 0), f'Point {p1} not on line {l}: {p1.line_distance(l)}!'
        assert approx_equals(p2.line_distance(l), 0), f'Point {p2} not on line {l}: {p2.line_distance(l)}!'
        assert approx_equals(c.eval_equation(p1), 0)
        assert approx_equals(c.eval_equation(p2), 0)


def test_circle_circle_intersect():
    for _ in range(1000):
        c1 = Circle(random_point(), torch.randn(()) ** 2)
        c2 = Circle(random_point(), torch.randn(()) ** 2)
        dist = c1.center.distance(c2.center)
        if c2.radius > c1.radius + dist - 1e-3:
            continue
        if c1.radius > c2.radius + dist - 1e-3:
            continue
        if dist > c1.radius + c2.radius - 1e-3:
            continue

        p1, p2 = c1.intersect_circle(c2)

        assert approx_equals(
            c1.eval_equation(p1), 0
        ), f'Intersection point not on c1: {c1=} {c2=} {p1=} err={c1.eval_equation(p1)}'
        assert approx_equals(
            c1.eval_equation(p2), 0
        ), f'Intersection point not on c1: {c1=} {c2=} {p2=} err={c1.eval_equation(p2)}'
        assert approx_equals(
            c2.eval_equation(p1), 0
        ), f'Intersection point not on c2: {c1=} {c2=} {p1=} err={c2.eval_equation(p1)}'
        assert approx_equals(
            c2.eval_equation(p2), 0
        ), f'Intersection point not on c2: {c1=} {c2=} {p2=} err={c2.eval_equation(p2)}'


if __name__ == '__main__':
    # test_distance_example()
    # test_distance()
    # test_project()
    # test_bisector()
    # test_distance()
    # test_line_intersect()
    # test_line_circle_intersect()
    test_circle_circle_intersect()
