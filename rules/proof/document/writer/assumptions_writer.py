from collections import defaultdict
from typing import List, Optional

from ...assumptions import Assumptions
from ...geometry_problem import GeometryProblem

from ..document_section import DocumentSection

from .document_section_writer import DocumentSectionWriter


class AssumptionsWriter(DocumentSectionWriter[Assumptions]):
    section = DocumentSection.ASSUMPTION

    def get_section_value(self, problem: GeometryProblem) -> Optional[Assumptions]:
        return problem.assumptions

    def to_lines(self, assumptions: Assumptions) -> List[str]:
        objects_by_type = defaultdict(list)
        for obj in assumptions.assumption_objects.values():
            if obj not in self.target_objects:
                objects_by_type[obj.type].append(obj)

        object_declaration_lines = []

        for type_, objects in objects_by_type.items():
            object_declaration_lines.append(', '.join(obj.name for obj in objects) + ': ' + type_)

        predicate_lines = [predicate.to_language_format() for predicate in assumptions.predicates]

        return object_declaration_lines + [""] + predicate_lines
