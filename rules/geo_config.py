from matplotlib import pyplot as plt
import scipy
from sympy import N, Predicate
import numpy as np
from scipy.optimize import minimize
from typing import List, Dict
from adjustText import adjust_text
import sympy

from .geometry_objects.geo_object import GeoObject


def get_sympy_objects(obj_map):
    sympy_obj_map = {}
    sympy_symbols = []
    for name, geo_object in obj_map.items():
        name = geo_object.name
        type = geo_object.type
        match type:
            case "Point":
                symbols = sympy.symbols(f"{name}_x {name}_y")
                sympy_object = sympy.Point2D(symbols[:])
            case "Line":
                symbols = sympy.symbols(f"{name}_p1_x {name}_p1_y {name}_p2_x {name}_p2_y")
                sympy_object = sympy.Line2D(sympy.Point2D(symbols[:2]), sympy.Point2D(symbols[2:4]))
            case "Triangle":
                symbols = sympy.symbols(f"{name}_p1_x {name}_p1_y {name}_p2_x {name}_p2_y {name}_p3_x {name}_p3_y")
                sympy_object = sympy.Triangle(
                    sympy.Point2D(symbols[:2]), sympy.Point2D(symbols[2:4]), sympy.Point2D(symbols[4:6])
                )
            case "Circle":
                symbols = symbols = (
                    list(sympy.symbols(f"{name}_O_x {name}_O_y"))
                    + [sympy.Symbol(f"{name}_radius", positive=True)]
                    + [sympy.Symbol(f"{name}_radius", positive=True)]
                )
                sympy_object = sympy.Circle(sympy.Point2D(symbols[:2]), symbols[2])
            case "Scalar":
                symbols = [sympy.Symbol(f"{name}")]
                sympy_object = symbols[0]
        sympy_obj_map[name] = sympy_object
        sympy_symbols.extend(symbols)
    return sympy_obj_map, sympy_symbols


class GeoConfig:
    def __init__(self, obj_map: Dict[str, GeoObject]):

        self.sympy_obj_map, self.sympy_symbols = get_sympy_objects(obj_map)
        self.pairs = None
        self.predicates: list[Predicate] = []

    def solve(self, predicates):
        for p in predicates:
            unpacked = p.unpack()
            if isinstance(unpacked, List):
                self.predicates.extend(unpacked)
            else:
                self.predicates.append(unpacked)

        expr = sum(p.potential(self.sympy_obj_map) for p in self.predicates)

        x0 = np.random.randn(len(self.sympy_symbols))

        bounds = []
        for idx, symbol in enumerate(self.sympy_symbols):
            if 'positive' in symbol.assumptions0 and symbol.assumptions0['positive']:
                bounds.append((0, scipy.inf))
                x0[idx] = np.abs(x0[idx])
            else:
                bounds.append((-scipy.inf, scipy.inf))

        def func(x):
            if isinstance(expr, sympy.Expr):
                return expr.subs(zip(self.sympy_symbols, x))
            else:
                return float(expr)

        result = minimize(func, x0, bounds=bounds)
        self.pairs = list(zip(self.sympy_symbols, result.x))
        if np.abs(result.fun) < 1e-6:
            return True, result
        else:
            return False, result

    def verify_predicates(self, predicates):
        assert self.pairs is not None
        all_predicates = []
        for p in predicates:
            unpacked = p.unpack()
            if isinstance(unpacked, List):
                all_predicates.extend(unpacked)
            else:
                all_predicates.append(unpacked)
        return [N(p.potential(self.sympy_obj_map).subs(self.pairs)) for p in all_predicates]

    def plot(self, fig=None):
        assert self.pairs is not None
        if not fig:
            fig, ax = plt.subplots()
        else:
            ax = fig.gca()

        texts = []
        for name, object in self.sympy_obj_map.items():
            if isinstance(object, sympy.Point):
                point = object
                x, y = float(N(point.x.subs(self.pairs))), float(N(point.y.subs(self.pairs)))
                ax.plot(x, y, marker='o')
                texts.append(ax.text(x, y, name))
                # ax.annotate(name, (x+0.05, y+0.05))
            elif isinstance(object, sympy.Line):
                p0, p1 = object.points
                ax.plot(
                    [N(p0.x.subs(self.pairs)), N(p1.x.subs(self.pairs))],
                    [N(p0.y.subs(self.pairs)), N(p1.y.subs(self.pairs))],
                )
            elif isinstance(object, sympy.Triangle):
                p0, p1, p2 = object.vertices
                ax.plot(
                    [
                        N(p0.x.subs(self.pairs)),
                        N(p1.x.subs(self.pairs)),
                        N(p2.x.subs(self.pairs)),
                        N(p0.x.subs(self.pairs)),
                    ],
                    [
                        N(p0.y.subs(self.pairs), p1.y.subs(self.pairs)),
                        N(p2.y.subs(self.pairs)),
                        N(p0.y.subs(self.pairs)),
                    ],
                )
            elif isinstance(object, sympy.Circle):
                center = object.center
                radius = N(object.radius.subs(self.pairs))
                Ox, Oy = N(center.x.subs(self.pairs)), N(center.y.subs(self.pairs))
                patch = plt.Circle((Ox, Oy), radius, fill=False)
                texts.append(ax.text(Ox, Oy, f"O_{name}"))
                ax.add_patch(patch)

        adjust_text(texts)
        ax.set_aspect('equal')
        return fig


def test_geo_config():
    from .theorem import Theorem
    from pathlib import Path

    theorems = Theorem.read(Path("rules/theorems/circles.yml"))

    theorem = theorems[0]
    obj_map = {}
    for obj in theorem.signature:
        obj_map[obj.name] = obj

    config = GeoConfig(obj_map)
    success, result = config.solve(theorem.required_predicates)
    print(success)
    if success:
        test_loss = config.verify_predicates(theorem.result_predicates)
        if not all(loss < 1e-6 for loss in test_loss):
            print("Fail!")
            print(theorem.name)
        else:
            fig = plt.figure()
            fig = config.plot()
            fig.show()


if __name__ == "__main__":
    test_geo_config()
