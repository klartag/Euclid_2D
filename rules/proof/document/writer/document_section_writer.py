from abc import ABC, abstractmethod
from typing import Optional

from ...geometry_problem import GeometryProblem

from ..document_section import DocumentSection
from ..geometry_document import GeometryDocument


class DocumentSectionWriter[T](ABC):
    """
    A class that knows to write a (specific) section of a GeometryDocument.
    
    The generic `T` specifies the type of an object that can be read from a `GeometryProblem`,
    that specifies the data relevant to the `self.section` section of a GeometryDocument.
    """
    
    @property
    @abstractmethod
    def section(self) -> DocumentSection:
        """The name of the section that this class can write."""
        ...

    @abstractmethod
    def get_section_value(self, problem: GeometryProblem) -> Optional[T]:
        """Reads the property from a `GeometryProblem` that corresponds to the section this class can write."""
        ...

    @abstractmethod
    def to_lines(self, section_value: T) -> list[str]:
        """Converts data into a list of lines that should be written into this class' section of the GeometryDocument."""
        ...

    def write(self, problem: GeometryProblem, document: GeometryDocument):
        """
        Updates a `GeometryDocument` with the section that this class writes.
        Reads the data required to write the section from the `GeometryProblem` parameter.
        """
        section_value = self.get_section_value(problem)

        if section_value is None:
            document.sections.pop(self.section, [])
            return

        lines = self.to_lines(section_value)

        if self.are_all_lines_empty(lines):
            document.sections.pop(self.section, [])
            return

        document.sections[self.section] = lines

    def are_all_lines_empty(self, lines: list[str]) -> bool:
        """Returns whether a list of strings consists only of empty strings and whitespace."""
        return not any([line.strip() for line in lines])
