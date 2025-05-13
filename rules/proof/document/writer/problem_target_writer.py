from typing import Optional

from rules.proof.statement import Statement

from ...geometry_problem import GeometryProblem

from ..document_section import DocumentSection

from .document_section_writer import DocumentSectionWriter


class ProblemTargetWriter(DocumentSectionWriter[Statement]):
    section = DocumentSection.TARGET

    def get_section_value(self, problem: GeometryProblem) -> Optional[Statement]:
        return problem.statement

    def to_lines(self, statement: Statement) -> list[str]:
        return [predicate.to_language_format() for predicate in statement.target_predicates]
