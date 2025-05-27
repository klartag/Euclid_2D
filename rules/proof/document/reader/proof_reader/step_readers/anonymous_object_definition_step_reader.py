from re import Match

from ......geometry_objects.geo_type import Signature
from ......parsers.predicate_parser.predicate_parser import PredicateParser

from .....steps.object_define_step import ObjDefineStep

from ..abstract_step_reader import AbstractStepReader


class AnonymousObjectDefinitionStepReader(AbstractStepReader[ObjDefineStep]):
    pattern = rf'We introduce (.*)$'
    predicate_parser: PredicateParser

    def __init__(self, signature: Signature):
        self.predicate_parser = PredicateParser(signature)

    def read(self, line: str, match: Match[str]) -> ObjDefineStep:
        obj = match.group(1)
        obj = self.predicate_parser.try_parse(obj)
        obj_map[obj.name] = obj
        return ObjDefineStep(obj)
