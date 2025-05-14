from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from util import BASE_PATH

from .document_section import DocumentSection


@dataclass
class GeometryDocument:
    path: Path
    sections: Dict[DocumentSection, List[str]]

    @staticmethod
    def open(path: str) -> 'GeometryDocument':
        path = GeometryDocument.get_full_problem_path(path)
        text = open(path, 'r').read()
        sections = GeometryDocument.parse_sections(text)
        return GeometryDocument(path, sections)

    def get_text(self) -> str:
        lines = []
        for section in DocumentSection:
            if section in self.sections:
                lines.extend(self.get_section_header(section))
                lines.extend(self.get_section_content(section))
                lines.append('')
        return '\n'.join(lines)

    def get_section_header(self, section: DocumentSection) -> List[str]:
        if section == DocumentSection.DEFAULT or section not in self.sections:
            return []
        return [f'{section.value}:']

    def get_section_content(self, section: DocumentSection) -> List[str]:
        return self.sections.get(section, [])

    def save(self):
        text = self.get_text()
        open(self.path, 'w').write(text)

    @staticmethod
    def get_full_problem_path(path_base: str) -> Path:
        full_path_options = [BASE_PATH / 'rules' / 'proof_samples' / path_base, BASE_PATH / path_base, Path(path_base)]

        for path_base in full_path_options:
            if path_base.exists():
                return path_base
        else:
            raise Exception(f'Proof file for {path_base} was not found.')

    @staticmethod
    def parse_sections(text: str) -> Dict[DocumentSection, List[str]]:
        sections = {}
        current_header = DocumentSection.DEFAULT
        for line in text.splitlines():
            maybe_header = GeometryDocument.try_parse_section_header(line)
            if maybe_header is not None:
                current_header = maybe_header
            else:
                if current_header not in sections:
                    sections[current_header] = []
                sections[current_header].append(line)
        return sections

    @staticmethod
    def try_parse_section_header(header: str) -> Optional[DocumentSection]:
        header = header.strip()
        if not (len(header) > 0 and header[-1] == ':'):
            return None
        header = header[:-1]
        if not header in DocumentSection:
            return None
        return DocumentSection(header)
