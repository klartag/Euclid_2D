from typing import Mapping
from .symmetric_predicate import SymmetricPredicate
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_objects.geo_object import GeoObject
from ..predicate import Predicate
from ...rule_utils import GeoType
from ...symmetry import Symmetry


class TangentPredicate(Predicate):
    NAME = 'tangent'

    def __init__(self, objects: tuple[GeoObject, ...]):
        if all(comp.type == GeoType.CIRCLE for comp in objects) or len(objects) != 2:
            # Initializing the tangent predicate for two circles, in which case it is symmetric,
            # and for the invalid cases.
            super().__init__(TangentPredicate.NAME, objects, Symmetry.ALL)
        else:
            # Initializing the tangent predicate for a line and a circle, in which case there is no symmetry and the
            # line comes first.
            a, b = objects
            if a.type == GeoType.CIRCLE:
                a, b = b, a
            super().__init__(TangentPredicate.NAME, (a, b), Symmetry.NONE)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return TangentPredicate(tuple(obj.substitute(replacements) for obj in self.components))

    def is_valid(self) -> bool:
        return (
            len(self.components) == 2
            and all(comp.type in (GeoType.LINE, GeoType.CIRCLE) for comp in self.components)
            and any(comp.type == GeoType.CIRCLE for comp in self.components)
        )

    def unpack(self) -> list[Predicate]:
        a, b = self.components
        if a.type == GeoType.CIRCLE and b.type == GeoType.CIRCLE:
            return [
                self,
                SymmetricPredicate(
                    'not_equals',
                    (ConstructionObject.from_args('center', (a,)), ConstructionObject.from_args('center', (b,))),
                ),
            ]
        return [self]
