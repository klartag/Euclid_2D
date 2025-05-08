from .....geometry_objects.geo_object import GeoObject
from .....rule_utils import ProofParseError

from ....steps.step import Step

from .abstract_step_parser import AbstractStepParser

from .step_parsers import (
    AlmostAlwaysStepParser,
    AnonymousObjectDefinitionStepParser,
    AssertStepParser,
    CommentStepParser,
    NullTheoremStepParser,
    ObjectDefinitionStepParser,
)


class BodyParser:
    step_parsers: list[AbstractStepParser]

    def __init__(self):
        self.step_parsers = [
            AlmostAlwaysStepParser(),
            CommentStepParser(),
            AnonymousObjectDefinitionStepParser(),
            # The assert pattern has the same prefix as the null theorem, so it must come first.
            AssertStepParser(),
            NullTheoremStepParser(),
            ObjectDefinitionStepParser(),
        ]

    def parse(self, lines: list[str], obj_map: dict[str, GeoObject]) -> list[Step]:
        """
        Parses the body of the proof.
        This step is used recursively when parsing if-steps.
        """
        lines = list(self.preprocess_lines(lines))

        try:
            steps = []
            for line in lines:
                steps.append(self.parse_step(line, obj_map))
            return steps
        except Exception as e:
            raise ProofParseError(f'Error when parsing line {line} ====> Because of {e}') from e

    def parse_step(self, line: str, obj_map: dict[str, GeoObject]) -> Step:
        for parser in self.step_parsers:
            step = parser.try_parse(line, obj_map)
            if step is not None:
                return step
        raise ProofParseError(f'Failed to parse proof: line {line} fits no pattern!')
