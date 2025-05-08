from typing import Iterable

from ....geometry_objects.geo_object import GeoObject
from ....predicates.predicate import Predicate
from ....predicates.predicate_factory import predicate_from_args

from ... import Proof

from ..document_section import DocumentSection
from ..geometry_document import GeometryDocument

from .proof_parser.proof_parser import ProofParser
from .embedding_parser import EmbeddingParser
from .problem_statement_parser import ProblemStatementParser


class DocumentParser:
    def __init__(self):
        self.problem_statement_parser = ProblemStatementParser()
        self.proof_parser = ProofParser()
        self.embedding_parser = EmbeddingParser()

    def parse(self, document: GeometryDocument, parse_proof_body: bool) -> Proof:
        """
        Parses a string representing a proof.
        """
        assumption_objects, assumption_preds = self.problem_statement_parser.parse_assumptions(
            document.get_section_text(DocumentSection.ASSUMPTION)
        )

        target_objects, target_preds = self.problem_statement_parser.parse_targets(
            document.get_section_text(DocumentSection.TARGET), dict(assumption_objects)
        )
        auxiliary_preds: list[Predicate] = []

        exist_objects: set[GeoObject] = set()

        # Marking objects in the 'Assumptions' and in the 'Need To Prove' sections as existing.
        for obj in set(assumption_objects.values()) | set(target_objects.values()):
            exist_objects.add(obj)

        # Marking objects in predicates from the 'Assumptions' and 'Need To Prove' sections as existing.
        for pred in assumption_preds + target_preds:
            for obj in pred.involved_objects():
                exist_objects.add(obj)

        auxiliary_preds.append(predicate_from_args('exists', tuple(exist_objects)))

        steps = (
            self.proof_parser.parse(document.get_section_text(DocumentSection.PROOF), dict(assumption_objects))
            if parse_proof_body
            else []
        )

        embedding_lines = document.get_section_text(DocumentSection.EMBEDDING)

        embedding = (
            self.embedding_parser.parse(embedding_lines, assumption_objects) if len(embedding_lines) > 0 else None
        )

        return Proof(
            assumption_objects | target_objects,
            assumption_objects,
            assumption_preds,
            auxiliary_preds,
            target_objects,
            target_preds,
            embedding,
            steps,
        )

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
