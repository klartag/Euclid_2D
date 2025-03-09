from dataclasses import dataclass
from typing import Self, Tuple

from ....geometry_objects.geo_object import GeoObject

from ...method_dictionaries import CONSTRUCTION_METHOD_DICTIONARY

from .method_dictionary import EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY


@dataclass
class EmbeddedGeoObject:
    construction_name: str
    components: Tuple[Self | GeoObject, ...]

    def __post_init__(self):
        if self.construction_name not in CONSTRUCTION_METHOD_DICTIONARY \
            and self.construction_name not in EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY:
                raise ValueError(f"Construction name '{self.construction_name}' not recognized.")


    def construction_method(self):
        if self.construction_name not in CONSTRUCTION_METHOD_DICTIONARY:
            return CONSTRUCTION_METHOD_DICTIONARY[self.construction_name]
        else:
            return EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY[self.construction_name]
