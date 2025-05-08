from re import Match

from ......rule_utils import split_args
from ......geometry_objects.geo_object import GeoObject
from ......predicates.predicate_factory import parse_predicate

from .....steps.almost_always_step import AlmostAlwaysStep

from ..abstract_step_parser import AbstractStepParser


class AlmostAlwaysStepParser(AbstractStepParser[AlmostAlwaysStep]):
    pattern = r'It is almost always true that (.*)$'

    def parse(line: str, match: Match[str], obj_map: dict[str, GeoObject]) -> AlmostAlwaysStep:
        preds_text = match.group(1)
        preds = [parse_predicate(part, obj_map) for part in split_args(preds_text)]
        return AlmostAlwaysStep(preds)
