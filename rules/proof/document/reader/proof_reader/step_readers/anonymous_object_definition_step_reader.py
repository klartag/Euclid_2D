from re import Match

from ......geometry_objects.geo_object import GeoObject
from ......geometry_objects.parse import parse_geo_object

from .....steps.object_define_step import ObjDefineStep

from ..abstract_step_reader import AbstractStepReader


class AnonymousObjectDefinitionStepReader(AbstractStepReader[ObjDefineStep]):
    pattern = rf'We introduce (.*)$'

    def read(self, line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> ObjDefineStep:
        obj = match.group(1)
        obj = parse_geo_object(obj, obj_map)
        obj_map[obj.name] = obj
        return ObjDefineStep(obj)
