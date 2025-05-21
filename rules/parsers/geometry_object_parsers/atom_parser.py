import re
from typing import Optional

from ...errors import IllegalObjectError
from ...geometry_objects.geo_type import Signature
from ...geometry_objects.atom import Atom

from ..immediate_geometry_object_parser import ImmediateGeometryObjectParser

ATOM_PATTERN = r'[A-Za-z_][A-Za-z_0-9\']*'


class AtomParser(ImmediateGeometryObjectParser[Atom]):
    def try_parse(self, text: str, signature: Signature) -> Optional[Atom]:
        if re.fullmatch(ATOM_PATTERN, text) is None:
            return None
        if text not in signature:
            raise IllegalObjectError(f"The type of the Atom with the name `{text}` is not known.")
        return Atom(text, signature[text])
