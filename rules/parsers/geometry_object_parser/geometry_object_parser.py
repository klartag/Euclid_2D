from typing import Optional

from ...geometry_objects.geo_type import Signature
from ...geometry_objects.geo_object import GeoObject

from ..abstract_geometry_parser import AbstractGeometryParser

from .implementations.atom_parser import AtomParser
from .implementations.literal_parser import LiteralParser
from .implementations.construction_object_parser import ConstructionObjectParser
from .implementations.equation_object_parser import EquationObjectParser


class GeometryObjectParser(AbstractGeometryParser[GeoObject]):
    signature: Signature
    parsers: list[AbstractGeometryParser[GeoObject]]

    def __init__(self, signature: Signature):
        self.signature = signature
        self.parsers = [
            AtomParser(signature),
            LiteralParser(),
            ConstructionObjectParser(self.try_parse),
            EquationObjectParser(self.try_parse),
        ]

    def try_parse(self, text: str) -> Optional[GeoObject]:
        for parser in self.parsers:
            geometry_object = parser.try_parse(text)
            if geometry_object is not None:
                return geometry_object
        return None
