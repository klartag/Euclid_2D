import re
from typing import Optional

from ...geometry_objects.geo_type import Signature
from ...geometry_objects.construction_object import Construction, ConstructionObject

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser


class ConstructionObjectParser(AbstractGeometryObjectParser[ConstructionObject]):
    def try_parse(self, data: str, signature: Signature) -> Optional[ConstructionObject]:
        const_name, arg_str = data[:-1].split('(', 1)
        args = tuple(parse_geo_object(arg, obj_map) for arg in split_args(arg_str))
        return ConstructionObject.from_args(const_name, args)
