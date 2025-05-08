from collections import defaultdict
from typing import Dict, List, Optional

from .document_section import DocumentSection


class GeometryDocument:
    sections: Dict[DocumentSection, List[str]]

    def __init__(self, text: str):
        sections = defaultdict(list)
        current_header = DocumentSection.DEFAULT
        for line in text.splitlines():
            maybe_header = self.try_parse_section_header(line)
            if maybe_header is not None:
                current_header = maybe_header
            else:
                sections[current_header].append(line)
        self.sections = dict(sections)

    def try_parse_section_header(self, header: str) -> Optional[DocumentSection]:
        header = header.strip()
        if not (len(header) > 0 and header[-1] == ':'):
            return None
        header = header[:-1]
        if not header in DocumentSection:
            return None
        return DocumentSection(header)

    def get_text(self) -> str:
        lines = []
        for section in DocumentSection:
            lines.extend(self.get_section_text(section))
        return '\n'.join(lines)

    def get_section_text(self, section: DocumentSection) -> List[str]:
        if section not in self.sections:
            return []
        lines = [f'#{section.value}:'] if section != DocumentSection.DEFAULT else []
        lines.extend(self.sections[section])
        return lines
