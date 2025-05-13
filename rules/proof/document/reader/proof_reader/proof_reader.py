from .....geometry_objects.geo_object import GeoObject
from .....rule_utils import ProofParseError, preprocess_lines

from ....steps.step import Step
from ....proof import Proof

from .abstract_step_reader import AbstractStepReader

from .step_readers import (
    AlmostAlwaysStepReader,
    AnonymousObjectDefinitionStepReader,
    AssertStepReader,
    CommentStepReader,
    NullTheoremStepReader,
    ObjectDefinitionStepReader,
    TheoremStepReader,
)


class ProofReader:
    step_readers: list[AbstractStepReader]

    def __init__(self):
        self.step_readers = [
            AlmostAlwaysStepReader(),
            CommentStepReader(),
            AnonymousObjectDefinitionStepReader(),
            # The assert pattern has the same prefix as the null theorem, so it must come first.
            AssertStepReader(),
            NullTheoremStepReader(),
            ObjectDefinitionStepReader(),
            TheoremStepReader(),
        ]

    def read(self, lines: list[str], obj_map: dict[str, GeoObject]) -> Proof:
        """
        Parses the body of the proof.
        """
        try:
            steps = []
            for line in preprocess_lines(lines):
                steps.append(self.read_step(line, obj_map))
            return Proof(steps)
        except Exception as e:
            raise ProofParseError(f'Error when parsing line {line} ====> Because of {e}') from e

    def read_step(self, line: str, obj_map: dict[str, GeoObject]) -> Step:
        for reader in self.step_readers:
            step = reader.try_read(line, obj_map)
            if step is not None:
                return step
        raise ProofParseError(f'Failed to parse proof: line {line} fits no pattern!')
