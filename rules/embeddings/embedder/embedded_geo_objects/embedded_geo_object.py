from dataclasses import dataclass, field
from typing import Self, Tuple

from ....predicates.global_predicates import get_constructions
from ....geometry_objects.geo_object import GeoObject

from ...method_dictionaries import CONSTRUCTION_METHOD_DICTIONARY

from .method_dictionary import EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY


@dataclass
class EmbeddedGeoObject:
    """
    Represents a GeoObject that is constructed by some construction,
    with parameters being either GeoObjects or other EmbeddedGeoObjects.
    
    The construction need not be a construction from the `CONSTRUCTION_METHOD_DICTIONARY`
    that we use to define GeoObjects during a proof,
    and may instead be a method taken from `EMBEDDED_GEO_OBJECT_CONSTRUCTION_DICTIONARY`,
    which is a list of constructions used only for embeddings.
    """

    type: str = field(init=False)
    is_in_construction_dictionary: bool = field(init=False)
    construction_name: str
    components: Tuple[Self | GeoObject, ...]

    def __post_init__(self):
        if self.construction_name in CONSTRUCTION_METHOD_DICTIONARY:
            construction = get_constructions().get(self.construction_name, None)
            if construction is None:
                raise ValueError(
                    f"Illegal construction name '{self.construction_name}' used in the CONSTRUCTION_METHOD_DICTIONARY."
                )
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
