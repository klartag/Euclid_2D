import re
from typing import Optional

from ....errors import IllegalObjectError
from ....geometry_objects.geo_type import Signature
from ....geometry_objects.atom import Atom

from ...abstract_geometry_parser import AbstractGeometryParser

ATOM_PATTERN = r'[A-Za-z_][A-Za-z_0-9\']*'


class AtomParser(AbstractGeometryParser[Atom]):
    signature: Signature

    def __init__(self, signature: Signature):
        self.signature = signature

    def try_parse(self, text: str) -> Optional[Atom]:
        if re.fullmatch(ATOM_PATTERN, text) is None:
            return None
        if text not in self.signature:
            raise IllegalObjectError(f"The object `{text}` is an Atom, but no object with this name is known.")
        return Atom(text, self.signature[text])
