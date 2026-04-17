from enum import Enum


class DocumentSection(Enum):
    """An enum listing the kinds of sections allowed in a GeometryDocument."""
    DEFAULT = None
    ASSUMPTION = 'Assumptions'
    EMBEDDING = 'Embedding'
    TARGET = 'Need to prove'
    PROOF = 'Proof'
    ERROR = 'Error'
