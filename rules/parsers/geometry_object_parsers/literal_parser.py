import re
from typing import Literal, Optional

from ...geometry_objects.geo_object import GeoObject

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser


LITERAL_PATTERN = r'(-?\d+(\.\d+)?)'


class LiteralParser(AbstractGeometryObjectParser[Literal]):
    def try_parse(self, data: str) -> Optional[GeoObject]:
        if re.fullmatch(LITERAL_PATTERN, data) is None:
            return None
        return Literal(data)
