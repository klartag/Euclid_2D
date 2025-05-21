from typing import Optional

from ...geometry_objects.geo_object import GeoObject
from ...geometry_objects.equation_object import EqOp, EquationObject

from ..delayed_geometry_object_parser import DelayedGeometryObjectParser


class EquationObjectParser(DelayedGeometryObjectParser[EqOp, EquationObject]):
    def try_split_components(self, text: str) -> Optional[tuple[EqOp, tuple[str, ...]]]:
        parenthesis_depth = 0
        operation_data: Optional[tuple[int, EqOp]] = None
        for i, c in enumerate(text):
            match c:
                case '(':
                    parenthesis_depth += 1
                case ')':
                    parenthesis_depth -= 1
                case '+' | '-' | '*' | '/':
                    if parenthesis_depth == 0:
                        operation = EqOp(c)
                        if operation_data is None or operation_data[1].priority() < operation.priority():
                            operation_data = (operation, i)

        if operation_data is None:
            return None
        return (operation_data[1], (text[: operation_data[0]], text[operation_data[0] + 1 :]))

    def build(self, data: EqOp, components: tuple[GeoObject, ...]) -> EquationObject:
        if len(components) != 2:
            raise ValueError(
                f"Equation objects require 2 components as inputs, but {len(components)} components were found."
            )
        return EquationObject(components[0], components[1], data)
