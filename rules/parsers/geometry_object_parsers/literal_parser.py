import re
from typing import Optional

from ...geometry_objects.geo_type import Signature
from ...geometry_objects.literal import Literal

from ..immediate_geometry_object_parser import ImmediateGeometryObjectParser


LITERAL_PATTERN = r'(-?\d+(\.\d+)?)'


class LiteralParser(ImmediateGeometryObjectParser[Literal]):
    def try_parse(self, text: str, signature: Signature) -> Optional[Literal]:
        if re.fullmatch(LITERAL_PATTERN, text) is None:
            return None
        return Literal(text)
