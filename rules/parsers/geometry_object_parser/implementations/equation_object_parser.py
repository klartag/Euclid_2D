from typing import Optional

from ....geometry_objects.geo_object import GeoObject
from ....geometry_objects.equation_object import EqOp, EquationObject

from ...abstract_recursive_geometry_parser import AbstractRecursiveGeometryParser


class EquationObjectParser(AbstractRecursiveGeometryParser[EqOp, EquationObject]):
    def _try_split_components(self, text: str) -> Optional[tuple[EqOp, tuple[str, ...]]]:
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
                        if operation_data is None or operation.priority() <= operation_data[1].priority():
                            operation_data = (i, operation)

        if operation_data is None:
            return None

        left_text = remove_extra_parenthesis(text[: operation_data[0]])
        right_text = remove_extra_parenthesis(text[operation_data[0] + 1 :])

        if left_text == '':
            left_text = '0'

        return (operation_data[1], (left_text, right_text))

    def _build(self, data: EqOp, components: tuple[GeoObject, ...]) -> EquationObject:
        if len(components) != 2:
            raise ValueError(
                f"Equation objects require 2 components as inputs, but {len(components)} components were found."
            )
        return EquationObject(components[0], components[1], data)


def remove_extra_parenthesis(text: str) -> str:
    length = len(text) + 1
    while length > len(text):
        length = len(text)
        text = text.strip()
        if text == '':
            break
        if text[0] != '(' or text[-1] != ')':
            break
        parenthesis_depth = 0
        for c in enumerate(text[1:-1]):
            match c:
                case '(':
                    parenthesis_depth += 1
                case ')':
                    parenthesis_depth -= 1
            if parenthesis_depth < 0:
                break
        text = text[1:-1]
    return text
