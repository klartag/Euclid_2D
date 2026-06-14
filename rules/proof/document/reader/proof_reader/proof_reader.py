from .....geometry_objects.geo_type import Signature
from .....rule_utils import preprocess_lines
from .....errors import ProofParseError

from ....steps.step import Step
from ....proof import Proof

from .abstract_step_reader import AbstractStepReader

from .step_readers import (
    AlmostAlwaysStepReader,
    AnonymousObjectDefinitionStepReader,
    AssertStepReader,
    CommentStepReader,
    ObjectDefinitionStepReader,
    TheoremStepReader,
)


class ProofReader:
    """Can read a proof."""

    signature: Signature
    step_readers: list[AbstractStepReader]
    """A list of readers for every kind of step that can appear in the proof."""

    def __init__(self, signature: Signature):
        self.signature = signature
        self.step_readers = [
            AlmostAlwaysStepReader(signature),
            CommentStepReader(),
            AnonymousObjectDefinitionStepReader(signature),
            # The assert pattern has the same prefix as the null theorem, so it must come first.
            AssertStepReader(signature),
            ObjectDefinitionStepReader(signature),
            TheoremStepReader(signature),
        ]

    def read(self, lines: list[str]) -> Proof:
        """
        Parses the body of the proof.
        """
        try:
            steps = []
            for line in preprocess_lines(lines):
                steps.append(self.read_step(line))
            return Proof(steps)
        except Exception as e:
            raise ProofParseError(f'Error when parsing line {line} ====> Because of {e}') from e

    def read_step(self, line: str) -> Step:
        """Reads a single step in the proof."""
        for reader in self.step_readers:
            step = reader.try_read(line)
            if step is not None:
                return step
        raise ProofParseError(f'Failed to parse proof: line {line} fits no pattern!')
