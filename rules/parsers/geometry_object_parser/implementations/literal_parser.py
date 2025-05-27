import re
from typing import Optional

from ....geometry_objects.literal import Literal

from ...abstract_geometry_parser import AbstractGeometryParser


LITERAL_PATTERN = r'(-?\d+(\.\d+)?)'


class LiteralParser(AbstractGeometryParser[Literal]):
    def try_parse(self, text: str) -> Optional[Literal]:
        if re.fullmatch(LITERAL_PATTERN, text) is None:
            return None
        return Literal(text)
