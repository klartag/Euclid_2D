from inspect import Signature
from re import Match

from rules.parsers.predicate_parser.predicate_parser import PredicateParser

from ......expression_parse_utils import split_args

from .....steps.assert_step import AssertStep

from ..abstract_step_reader import AbstractStepReader


class AssertStepReader(AbstractStepReader[AssertStep]):
    pattern = r'We have (proved|shown) (.*)$'

    predicate_parser: PredicateParser

    def __init__(self, signature: Signature):
        self.predicate_parser = PredicateParser(signature)

    def read(self, line: str, match: Match[str]) -> AssertStep:
        _, preds_text = match.groups()
        preds = [self.predicate_parser.try_parse(part) for part in split_args(preds_text)]
        return AssertStep(preds)
