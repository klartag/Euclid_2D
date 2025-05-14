from typing import Optional

from ...geometry_problem import GeometryProblem

from ..document_section import DocumentSection
from ..geometry_document import GeometryDocument

from .document_section_writer import DocumentSectionWriter
from .assumptions_writer import AssumptionsWriter
from .embedding_writer import EmbeddingWriter
from .problem_target_writer import ProblemTargetWriter
from .proof_writer import ProofWriter


class DocumentWriter:
    def __init__(self):
        self.assumptions_writer = AssumptionsWriter()
        self.embedding_writer = EmbeddingWriter()
        self.target_writer = ProblemTargetWriter()
        self.proof_writer = ProofWriter()

    def write_sections(self, problem: GeometryProblem, document: GeometryDocument, *sections: list[DocumentSection]):
        for section in sections:
            writer = self.get_section_writer(section)
            writer.write(problem, document)

    def get_section_writer(self, section: DocumentSection) -> Optional[DocumentSectionWriter]:
        match section:
            case DocumentSection.ASSUMPTION:
                return self.assumptions_writer
            case DocumentSection.EMBEDDING:
                return self.embedding_writer
            case DocumentSection.TARGET:
                return self.target_writer
            case DocumentSection.PROOF:
                return self.proof_writer
            case _:
                return None
