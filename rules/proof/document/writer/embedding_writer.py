import json
from typing import List, Optional

from rules.proof.document.document_section import DocumentSection

from ....embeddings.embedding import Embedding

from ...geometry_problem import GeometryProblem

from .document_section_writer import DocumentSectionWriter


class EmbeddingWriter(DocumentSectionWriter[Embedding]):
    section = DocumentSection.EMBEDDING

    def get_section_value(self, problem: GeometryProblem) -> Optional[Embedding]:
        return problem.embedding

    def to_lines(self, embedding: Embedding) -> List[str]:
        return [f'{name} := {json.dumps(object_.to_dict())}' for name, object_ in embedding.items()]
