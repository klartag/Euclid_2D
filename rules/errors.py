class GeometryError(RuntimeError):
    """
    A generic error for the geometry project.
    """


class ProofParseError(GeometryError):
    """
    An error raised when attempting to parse data results in invalid objects.
    """


class ProofCheckError(GeometryError):
    """
    An error in proof checking. Shows that the proof is incorrect.
    """


class IllegalObjectError(ProofCheckError):
    """
    An error in proof checking. Shows that the proof is incorrect.
    """
