from typing import Optional

from rules.geometry_objects.geo_object import GeoObject
from rules.predicates.global_predicates import get_constructions

from ...geometry_objects.construction_object import Construction, ConstructionObject

from ..delayed_geometry_object_parser import DelayedGeometryObjectParser


class ConstructionObjectParser(DelayedGeometryObjectParser[Construction, ConstructionObject]):
    def try_split_components(self, data: str) -> Optional[tuple[Construction, tuple[str, ...]]]:
        data = data.strip()
        if '(' not in data:
            return None
        if data[-1] != ')':
            return None

        construction_name, argument_string = data[:-1].split('(', 1)

        construction = get_constructions().get(construction_name, None)
        if construction is None:
            return None

        parenthesis_depth = 0
        comma_locations = [-1]
        for i, c in enumerate(argument_string):
            match c:
                case '(':
                    parenthesis_depth += 1
                case ')':
                    parenthesis_depth -= 1
                case ',':
                    if parenthesis_depth == 0:
                        comma_locations.append(i)
            if parenthesis_depth < 0:
                return None

        comma_locations.append(len(argument_string))
        arguments = tuple(
            [argument_string[start + 1 : end].strip() for (start, end) in zip(comma_locations, comma_locations[1:])]
        )
        return (construction, arguments)

    def build(self, data: Construction, components: tuple[GeoObject, ...]) -> ConstructionObject:
        return data(*components)
