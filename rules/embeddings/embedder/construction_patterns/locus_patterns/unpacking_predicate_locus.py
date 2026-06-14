from abc import abstractmethod
from dataclasses import dataclass
from typing import Callable, Optional, Sequence, Tuple, Unpack, Union

from .....geometry_objects.geo_object import GeoObject
from .....predicates.predicate import Predicate

from ...embedded_geo_objects.embedded_geo_object import EmbeddedGeoObject, ExtendedGeoObject

from .locus_pattern_matcher import LocusPattern


@dataclass
class UnpackingPredicateLocus(LocusPattern):
    """
    A locus pattern that knows to parse a predicate of the type
    `predicate(A, B, C, ...)`
    where one of the arguments should be taken special note of.
    (for example, it might directly equal the object whose locus we want to find.)

    For example, if `predicate_name` is `collinear`,
    and `parameter_index_options` is [1],
    then this instance of UnpackingPredicateLocus will parse locii defined by the predicate `collinear(A, X, B)`,
    where `X` is the object whose locus we are looking to define.
    In this case, `locus_construction_method` would be initialized as the function that takes two points (A, B),
    and returns the object `Line(A, B)`, as this is the locus of points `X` that satisfies `collinear(A, X, B)`.
    """

    locus_construction_method: Callable[[Unpack[Tuple[ExtendedGeoObject, ...]]], EmbeddedGeoObject]
    """
    A method that takes the *rest* of the parameters given to `predicate_name`
    (all the parameters except the object whose locus we want)
    and returns the locus of the object.
    """
    predicate_name: str
    """
    The name of the predicate to parse.
    """
    parameter_index_options: Union[int, Sequence[int], None]
    """
    The indices in the predicate where the object is allowed to appear.
    *   If it is of the type `int`, this is the only index where the object may appear.
    *   If it is of the type `Sequence[int]`, this is the list of indices where the object may appear.
    *   If it is `None`, the object may appear in any index.
    """

    def match(self, object_: GeoObject, predicate: Predicate) -> Optional[ExtendedGeoObject]:
        for parameter_index in unpack_index_options(self.parameter_index_options, len(predicate.components)):
            locus = self.match_predicate_parameter_option(object_, predicate, parameter_index)
            if locus is not None:
                return locus
        return None

    @abstractmethod
    def match_predicate_parameter_option(self, object_: GeoObject, predicate: Predicate, parameter_index: int) -> Optional[ExtendedGeoObject]:
        """
        Identical to `LocusPattern.match`, but specifically attempts to recognize the Locus Pattern in `predicate`,
        given that the special index to find `object_` in is the index `parameter_index`.
        """
        ...

def unpack_index_options(parameter_index_options: Union[int, Sequence[int], None], component_count: int) -> Sequence[int]:
    """
    Takes `parameter_index_options`, and parses it into a `Sequence[int]` describing all possible indices the object whose locus we want
    can take in the predicate we are parsing.
    The rules for parsing are as described in the documentation for `parameter_index_options` in the `UnpackingPredicate` class.
    
    component_count:    The total number of parameters in the predicate we are parsing.
    """
    if parameter_index_options is None:
        return list(range(component_count))
    elif isinstance(parameter_index_options, Sequence):
        return [i for i in parameter_index_options if i < component_count]
    else:
        return [parameter_index_options] if parameter_index_options < component_count else []