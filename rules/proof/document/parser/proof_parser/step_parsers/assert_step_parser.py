from re import Match

from ......rule_utils import split_args
from ......geometry_objects.geo_object import GeoObject
from ......predicates.predicate_factory import parse_predicate

from .....steps.assert_step import AssertStep

from ..abstract_step_parser import AbstractStepParser


class AssertStepParser(AbstractStepParser[AssertStep]):
    pattern = r'We have (proved|shown) (.*)$'

    def parse(line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> AssertStep:
        _, preds_text = match.groups()
        preds = [parse_predicate(part, obj_map) for part in split_args(preds_text)]
        return AssertStep(preds)
