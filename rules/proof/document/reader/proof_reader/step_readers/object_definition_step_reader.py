from re import Match

from rules.geometry_objects.atom import Atom

from ......rule_utils import ProofParseError
from ......geometry_objects.geo_object import GeoObject
from ......geometry_objects.parse import parse_geo_object

from .....steps.object_define_step import ObjDefineStep

from ..abstract_step_reader import AbstractStepReader


OBJECT_NAME_PATTERN = rf'([\w\']+)'
OBJECT_DEFINITION_PATTERN = rf'Let {OBJECT_NAME_PATTERN} := (.*)$'


class ObjectDefinitionStepReader(AbstractStepReader[ObjDefineStep]):
    pattern = OBJECT_DEFINITION_PATTERN

    def read(self, line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> ObjDefineStep:
        left, right = match.groups()
        right_obj = parse_geo_object(right, obj_map)
        left_obj = Atom(left, right_obj.type)
        if left_obj.name in obj_map:
            raise ProofParseError(f'Object {left_obj.name} redefined in line {line}!')

        obj_map[left_obj.name] = left_obj
        return ObjDefineStep(left_obj, right_obj)
