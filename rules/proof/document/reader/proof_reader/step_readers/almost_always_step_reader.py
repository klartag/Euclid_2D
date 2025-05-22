from re import Match

from rules.geometry_objects.geo_type import Signature
from rules.parsers.predicate_parser.predicate_parser import PredicateParser

from ......expression_parse_utils import split_args

from .....steps.almost_always_step import AlmostAlwaysStep

from ..abstract_step_reader import AbstractStepReader


class AlmostAlwaysStepReader(AbstractStepReader[AlmostAlwaysStep]):
    pattern = r'It is almost always true that (.*)$'

    predicate_parser: PredicateParser

    def __init__(self, signature: Signature):
        self.predicate_parser = PredicateParser(signature)

    def read(self, line: str, match: Match[str]) -> AlmostAlwaysStep:
        preds_text = match.group(1)
        preds = [self.predicate_parser.try_parse(part) for part in split_args(preds_text)]
        return AlmostAlwaysStep(preds)
