from dataclasses import dataclass
from typing import Optional

from ..embeddings import Embedding

from .statement import Statement
from .proof import Proof


@dataclass
class GeometryProblem:
    statement: Optional[Statement]
    embedding: Optional[Embedding]
    proof: Optional[Proof]

    def shallow_copy(self) -> 'GeometryProblem':
        assumptions = None if self.statement is None else self.statement.shallow_copy()
        need_to_prove = None if self.need_to_prove is None else self.need_to_prove.shallow_copy()
        embedding = None if self.embedding is None else self.embedding.shallow_copy()
        proof = None if self.proof is None else self.proof.shallow_copy()

        return GeometryProblem(assumptions, need_to_prove, embedding, proof)
