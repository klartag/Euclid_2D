from abc import ABC, abstractmethod
from typing import Optional

from ...geometry_problem import GeometryProblem

from ..document_section import DocumentSection
from ..geometry_document import GeometryDocument


class DocumentSectionWriter[T](ABC):
    @property
    @abstractmethod
    def section(self) -> DocumentSection: ...

    @abstractmethod
    def get_section_value(self, problem: GeometryProblem) -> Optional[T]: ...

    @abstractmethod
    def to_lines(self, section_value: T) -> list[str]: ...

    def write(self, problem: GeometryProblem, document: GeometryDocument):
        section_value = self.get_section_value(problem)

        if section_value is None:
            document.sections.pop(self.section, [])
            return

        lines = self.to_lines(section_value)

        if self.are_all_lines_empty(lines):
            document.sections.pop(self.section, [])
            return

        document.sections[self.section] = lines

    def are_all_lines_empty(self, lines: str) -> bool:
        return not any([line.strip() for line in lines])
