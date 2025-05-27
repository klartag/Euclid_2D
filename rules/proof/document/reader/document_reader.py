from typing import Iterable

from ...geometry_problem import GeometryProblem

from ..document_section import DocumentSection
from ..geometry_document import GeometryDocument

from .proof_reader.proof_reader import ProofReader
from .embedding_reader import EmbeddingReader
from .problem_statement_reader import ProblemStatementReader


class DocumentReader:
    def read(self, document: GeometryDocument, read_proof_body: bool) -> GeometryProblem:
        """
        Parses a string representing a proof.
        """
        problem_statement_reader = ProblemStatementReader()
        statement = problem_statement_reader.read(document)

        proof_reader = ProofReader(statement.signature)
        embedding_reader = EmbeddingReader(statement.signature)

        proof = proof_reader.read(document.get_section_content(DocumentSection.PROOF)) if read_proof_body else None
        embedding_lines = document.get_section_content(DocumentSection.EMBEDDING)
        embedding = embedding_reader.read(embedding_lines) if len(embedding_lines) > 0 else None
        return GeometryProblem(statement, embedding, proof)

    def remove_comments(self, lines: Iterable[str]) -> Iterable[str]:
        """
        Removes comments from the lines and removes empty lines.
        """
        for line in lines:
            if '#' in line:
                line = line.split('#')[0]
            line = line.rstrip()
            if len(line) > 0:
                yield line
