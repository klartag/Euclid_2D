from typing import Optional

from ....expression_parse_utils import split_args
from ....geometry_objects.geo_object import GeoObject
from ....predicates.global_predicates import get_constructions
from ....geometry_objects.construction_object import Construction, ConstructionObject

from ...abstract_recursive_geometry_parser import AbstractRecursiveGeometryParser


class ConstructionObjectParser(AbstractRecursiveGeometryParser[ConstructionObject, Construction, GeoObject]):
    def _try_split_components(self, data: str) -> Optional[tuple[Construction, tuple[str, ...]]]:
        if '(' not in data:
            return None
        if data[-1] != ')':
            return None

        construction_name, argument_string = data[:-1].split('(', 1)

        construction = get_constructions().get(construction_name, None)
        if construction is None:
            return None
        arguments = split_args(argument_string)
        if arguments is None:
            return None
        return (construction, tuple(arguments))

    def _build(self, data: Construction, components: tuple[GeoObject, ...]) -> ConstructionObject:
        return data(*components)
