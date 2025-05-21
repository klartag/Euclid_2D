import re
from typing import Literal, Optional

from ...geometry_objects.geo_object import GeoObject

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser

ATOM_PATTERN = r'[A-Za-z_][A-Za-z_0-9\']*'


class LiteralParser(AbstractGeometryObjectParser[Literal]):
    def try_parse(self, data: str) -> Optional[GeoObject]:
        if re.fullmatch(ATOM_PATTERN, data) is None:
            return None
        return Literal(data)
