import sympy
from dataclasses import dataclass, field
from typing import List, Union, Optional
from .geo_object import GeoObject


@dataclass(frozen=True, order=True)
class SympyObject(GeoObject):

    sympy_object: Union[sympy.Point2D, sympy.Line2D, sympy.Triangle, sympy.Circle]
    symbols: Optional[List[sympy.Symbol]]

    @classmethod
    def from_geo_object(cls, geo_object):
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
                symbols = sympy.symbols(f"{name}_O_x {name}_O_y {name}_radius")
                sympy_object = sympy.Circle(sympy.Point2D(symbols[:2]), symbols[2])
            case "Scalar":
                symbols = [sympy.Symbol(f"{name}")]
                sympy_object = symbols[0]

        return cls(name, type, sympy_object, symbols)
