from .embedding_serializer import EmbeddingSerializer
from .problem_statement_serializer import ProblemStatementSerializer
from .proof_serializer import ProofSerializer


class DocumentSerializer:
    def __init__(self):
        self.proof_serializer = ProofSerializer()
        self.problem_statement_serializer = ProblemStatementSerializer()
        self.embedding_serializer = EmbeddingSerializer()
