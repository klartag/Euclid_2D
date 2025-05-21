from typing import Optional

from ...geometry_objects.geo_type import Signature
from ...geometry_objects.geo_object import GeoObject

from ..immediate_geometry_object_parser import ImmediateGeometryObjectParser
from ..delayed_geometry_object_parser import DelayedGeometryObjectParser

from .atom_parser import AtomParser
from .literal_parser import LiteralParser
from .construction_object_parser import ConstructionObjectParser
from .equation_object_parser import EquationObjectParser


class GeometryObjectParser(ImmediateGeometryObjectParser[GeoObject]):
    immediate_parsers: list[ImmediateGeometryObjectParser[GeoObject]]
    delayed_parsers: list[DelayedGeometryObjectParser]

    def __init__(self):
        self.immediate_parsers = [AtomParser(), LiteralParser()]
        self.delayed_parsers = [ConstructionObjectParser(), EquationObjectParser()]

    def try_parse(self, text: str, signature: Signature) -> Optional[GeoObject]:
        for parser in self.immediate_parsers:
            geometry_object = parser.try_parse(text, signature)
            if geometry_object is not None:
                return geometry_object
        for parser in self.delayed_parsers:
            result = parser.try_split_components(text)
            if result is not None:
                (data, components) = result
                parsed_components = tuple([self.try_parse(component, signature) for component in components])
                return parser.build(data, parsed_components)
        return None
