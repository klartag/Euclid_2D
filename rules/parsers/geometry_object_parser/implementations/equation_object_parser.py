from typing import Optional

from rules.expression_parse_utils import alternating_merge_string, generic_split_args, is_valid_parenthesis
from rules.geometry_objects.geo_type import EQN_TYPES

from ....geometry_objects.geo_object import GeoObject
from ....geometry_objects.equation_object import EqOp, EquationObject

from ...abstract_recursive_geometry_parser import AbstractRecursiveGeometryParser


class EquationObjectParser(AbstractRecursiveGeometryParser[EquationObject, EqOp, GeoObject]):
    def _try_split_components(self, text: str) -> Optional[tuple[EqOp, tuple[str, ...]]]:
        result = generic_split_args(text, '+-')
        if result is None or len(result[0]) == 1:
            result = generic_split_args(text, '*/')
        if result is None or len(result[0]) == 1:
            return None

        (arguments, separators) = result

        left = remove_extra_parenthesis(alternating_merge_string(arguments[:-1], separators[:-1]))
        operation = EqOp(separators[-1])
        right = remove_extra_parenthesis(arguments[-1])

        if left == '':
            left = '0'

        return (operation, (left, right))

    def _build(self, data: EqOp, components: tuple[GeoObject, ...]) -> EquationObject:
        if len(components) != 2:
            raise ValueError(
                f"Equation objects require 2 components as inputs, but {len(components)} components were found."
            )
        for component in components:
            if not component.type in EQN_TYPES:
                raise ValueError(f"Components should all be scalars, but {component} is a {component.type}.")
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
        if not is_valid_parenthesis(text[1:-1].strip()):
            break
        text = text[1:-1]
    return text
