import re
from typing import Optional

from ...geometry_objects.geo_type import Signature
from ...geometry_objects.geo_object import GeoObject
from ...geometry_objects.literal import Literal

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser


LITERAL_PATTERN = r'(-?\d+(\.\d+)?)'


class LiteralParser(AbstractGeometryObjectParser[Literal]):
    def try_parse(self, data: str, signature: Signature) -> Optional[GeoObject]:
        if re.fullmatch(LITERAL_PATTERN, data) is None:
            return None
        return Literal(data)
