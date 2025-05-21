from typing import Optional

from ...geometry_objects.geo_object import GeoObject

from ..abstract_geometry_object_parser import AbstractGeometryObjectParser


class GeometryObjectParser(AbstractGeometryObjectParser[GeoObject]):
    def try_parse(self, data: str) -> Optional[GeoObject]:
        raise NotImplementedError()
