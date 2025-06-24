from dataclasses import dataclass
from typing import Mapping

from ..global_predicates import get_macros

from ..predicate import Predicate

from ...geometry_objects.geo_object import GeoObject
from ...symmetry import Symmetry


@dataclass
class MacroData:
    """
    TODO: Document
    """

    name: str
    symmetry: Symmetry
    objects: list[GeoObject]
    predicates: list[Predicate]
    possible_conclusions: list[tuple[list[Predicate], list[Predicate]]]
    conclude_self: bool


class MacroPredicate(Predicate):
    """
    A predicate that is a combination of other predicates.
    """

    macro_data: MacroData

    def __init__(self, name: str, objects: tuple[GeoObject, ...]):
        self.macro_data = get_macros()[name]
        super().__init__(name, objects, self.macro_data.symmetry)

    def substitute(self, replacements: Mapping[GeoObject, GeoObject]) -> Predicate:
        return MacroPredicate(self.name, tuple(obj.substitute(replacements) for obj in self.components))

    def unpack(self) -> list[Predicate]:
        if self.macro_data.conclude_self:
            return [self]
        else:
            subs = {base_obj: obj for base_obj, obj in zip(self.macro_data.objects, self.components)}
            return [conc.substitute(subs) for conc in self.macro_data.predicates]

    def is_valid(self) -> bool:
        """
        Checks that the macro is valid.
        """
        return (len(self.components) == len(self.macro_data.objects)) and all(
            obj.type == macro_obj.type for obj, macro_obj in zip(self.components, self.macro_data.objects)
        )

    def possible_conclusions(self) -> list[tuple[list[Predicate], list[Predicate]]]:
        """
        Returns the list of predicates created by the construction object.
        """
        subs = {sig: comp for sig, comp in zip(self.macro_data.objects, self.components)}
        return [
            ([pred.substitute(subs) for pred in left], [pred.substitute(subs) for pred in right])
            for left, right in self.macro_data.possible_conclusions
        ]
