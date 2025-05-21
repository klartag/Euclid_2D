from typing import Optional

from ...geometry_objects.geo_type import Signature
from ...geometry_objects.geo_object import GeoObject

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser

from .atom_parser import AtomParser
from .literal_parser import LiteralParser


class GeometryObjectParser(AbstractGeometryObjectParser[GeoObject]):
    parsers: list[AbstractGeometryObjectParser[GeoObject]]

    def __init__(self):
        self.parsers = [AtomParser(), LiteralParser()]

    def try_parse(self, data: str, signature: Signature) -> Optional[GeoObject]:
        for parser in self.parsers:
            geometry_object = parser.try_parse(data, signature)
            if geometry_object is not None:
                return geometry_object
        raise ValueError("Unable to parse the current object.")
