from typing import Optional

from ...geometry_problem import GeometryProblem
from ...problem_target import ProblemTarget

from ..document_section import DocumentSection

from .document_section_writer import DocumentSectionWriter


class ProblemTargetWriter(DocumentSectionWriter[ProblemTarget]):
    section = DocumentSection.TARGET

    def get_section_value(self, problem: GeometryProblem) -> Optional[ProblemTarget]:
        return problem.need_to_prove

    def to_lines(self, target: ProblemTarget) -> list[str]:
        return [predicate.to_language_format() for predicate in target.predicates]
