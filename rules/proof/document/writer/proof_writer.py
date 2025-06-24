from typing import Optional

from ...geometry_problem import GeometryProblem
from ...proof import Proof

from ..document_section import DocumentSection

from .document_section_writer import DocumentSectionWriter


class ProofWriter(DocumentSectionWriter[Proof]):
    """
    TODO: Document
    """

    section = DocumentSection.PROOF

    def get_section_value(self, problem: GeometryProblem) -> Optional[Proof]:
        return problem.proof

    def to_lines(self, proof: Proof) -> list[str]:
        return [step.to_language_format() for step in proof.steps]
