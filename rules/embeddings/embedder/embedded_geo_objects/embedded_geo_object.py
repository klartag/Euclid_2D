from dataclasses import dataclass, field
from typing import Self, Tuple

from rules.predicates.global_predicates import get_constructions

from ....geometry_objects.geo_object import GeoObject

from ...method_dictionaries import CONSTRUCTION_METHOD_DICTIONARY

from .method_dictionary import EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY


@dataclass
class EmbeddedGeoObject:
    type: str = field(init=False)
    is_in_construction_dictionary: bool = field(init=False)
    construction_name: str
    components: Tuple[Self | GeoObject, ...]

    def __post_init__(self):
        if self.construction_name in CONSTRUCTION_METHOD_DICTIONARY:
            construction = get_constructions().get(self.construction_name, None)
            if construction is None:
                raise ValueError(f"Illegal construction name '{self.construction_name}' used in the CONSTRUCTION_METHOD_DICTIONARY.")
            self.is_in_construction_dictionary = True
            self.type = construction.res.type
        elif self.construction_name in EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY:
            self.is_in_construction_dictionary = False
            self.type = EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY[self.construction_name].type
        else:
            raise ValueError(f"Construction name '{self.construction_name}' not recognized.")


    def construction_method(self):
        if self.is_in_construction_dictionary:
            return CONSTRUCTION_METHOD_DICTIONARY[self.construction_name]
        else:
            return EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY[self.construction_name].method


ExtendedGeoObject = GeoObject | EmbeddedGeoObject
