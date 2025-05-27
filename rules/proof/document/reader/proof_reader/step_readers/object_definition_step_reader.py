from re import Match

from ......errors import ProofParseError
from ......parsers.geometry_object_parser.geometry_object_parser import GeometryObjectParser
from ......geometry_objects.atom import Atom
from ......geometry_objects.geo_type import Signature

from .....steps.object_define_step import ObjDefineStep

from ..abstract_step_reader import AbstractStepReader


OBJECT_NAME_PATTERN = rf'([\w\']+)'
OBJECT_DEFINITION_PATTERN = rf'Let {OBJECT_NAME_PATTERN} := (.*)$'


class ObjectDefinitionStepReader(AbstractStepReader[ObjDefineStep]):
    pattern = OBJECT_DEFINITION_PATTERN

    signature: Signature
    geometry_object_parser: GeometryObjectParser

    def __init__(self, signature: Signature):
        self.signature = signature
        self.geometry_object_parser = GeometryObjectParser(signature)

    def read(self, line: str, match: Match[str]) -> ObjDefineStep:
        left, right = match.groups()
        right_obj = self.geometry_object_parser.try_parse(right)
        left_obj = Atom(left, right_obj.type)
        if left_obj.name in self.signature:
            raise ProofParseError(f'Object {left_obj.name} redefined in line {line}!')

        obj_map[left_obj.name] = left_obj
        return ObjDefineStep(left_obj, right_obj)
