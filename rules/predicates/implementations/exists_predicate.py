from typing import Mapping
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from .symmetric_predicate import SymmetricPredicate


class ExistsPredicate(SymmetricPredicate):
    """
    The exists(...) predicate is used to indicate nothing in particular, other than to assert
    that this geometry object is relevant, and that other theorems may use it as input.
    
    In a sense, it is alike to saying "I marked this object in the diagram."
    
    It is used in the following cases:
    * When attempting to prove a problem, all objects in the problem statement are immediately assumed to exist.
    * When a theorem step is applied, any new objects introduced by the theorem are immediately assumed to exist.
    * Sometimes, a theorem will only conclue an `exists` predicate.
      See the theorems in "rules/theorems/angles/drawing_heuristics.yml" for examples of this.
    * For a theorem step to be applied, it is required that all of the input objects have an `exists` predicate to be true on them.
    """
    NAME = 'exists'

    def __init__(self, objects: tuple[GeoObject, ...]):
        super().__init__(ExistsPredicate.NAME, objects)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return ExistsPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def is_valid(self) -> bool:
        return True

    def unpack(self) -> list[Predicate]:
        return [ExistsPredicate((obj,)) for obj in self.components]
