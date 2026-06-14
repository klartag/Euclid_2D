from ..embedded_objects import EmbeddedObject


def exists(*objects: EmbeddedObject) -> bool:
    """
    The embedding should always return `True` when calling the `exists` predicate,
    as `exists` is a predicate relevant to the state of a Proof, and not to a geometrical diagram.  
    """
    return True
