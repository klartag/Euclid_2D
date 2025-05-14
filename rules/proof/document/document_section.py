from enum import Enum


class DocumentSection(Enum):
    DEFAULT = None
    ASSUMPTION = 'Assumptions'
    EMBEDDING = 'Embedding'
    TARGET = 'Need to prove'
    PROOF = 'Proof'
    ERROR = 'Error'
