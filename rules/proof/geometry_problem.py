from typing import Optional

from .assumptions import Assumptions
from ..embeddings import Embedding
from .problem_target import ProblemTarget
from .proof import Proof


class GeometryProblem:
    assumptions: Optional[Assumptions]
    embedding: Optional[Embedding]
    need_to_prove: Optional[ProblemTarget]
    proof: Optional[Proof]
