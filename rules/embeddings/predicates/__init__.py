from typing import Callable, Dict, Tuple, Unpack

from ..embedded_objects import EmbeddedObject

from .collinear import collinear
from .concurrent import concurrent
from .concyclic import concyclic
from .equality import equals, equals_mod_360


PREDICATE_METHOD_DICTIONARY: Dict[str, Callable[[Unpack[Tuple[EmbeddedObject, ...]]], bool]] = {
    'collinear': collinear,
    'concurrent': concurrent,
    'concyclic': concyclic,
    'equals': equals,
    'equals_mod_360': equals_mod_360,
}
