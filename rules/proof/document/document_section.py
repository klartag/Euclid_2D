from enum import Enum


class DocumentSection(Enum):
    """
    TODO: Document
    """

    DEFAULT = None
    ASSUMPTION = 'Assumptions'
    EMBEDDING = 'Embedding'
    TARGET = 'Need to prove'
    PROOF = 'Proof'
    ERROR = 'Error'
