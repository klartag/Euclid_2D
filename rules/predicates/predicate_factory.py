from ..geometry_objects.geo_object import GeoObject

from .implementations.between_predicate import BetweenPredicate
from .implementations.convex_predicate import ConvexPredicate
from .implementations.distinct_predicate import DistinctPredicate
from .implementations.exists_predicate import ExistsPredicate
from .implementations.identical_predicate import IdenticalPredicate
from .implementations.in_predicate import InPredicate
from .implementations.macro_predicate import MacroPredicate
from .implementations.not_one_of_predicate import NotOneOfPredicate
from .predicate import Predicate
from .global_predicates import get_macros
from .implementations.symmetric_predicate import SIMPLE_SYMMETRIC_PREDICATE_NAMES, SymmetricPredicate
from .implementations.tangent_predicate import TangentPredicate


PREDICATE_EQ_MOD_PATTERN = r'(.*) == (.*) mod (\d+)'
PREDICATE_NE_MOD_PATTERN = r'(.*) != (.*) mod (\d+)'
PREDICATE_NOT_IN_PATTERN = r'(.*) not in (.*)'
PREDICATE_IN_PATTERN = r'(.*) in (.*)'
PREDICATE_EQ_PATTERN = r'(.*) == (.*)'
PREDICATE_NE_PATTERN = r'(.*) != (.*)'
PREDICATE_GENERAL_PATTERN = r'(.*?)\((.*)\)'


def predicate_from_args(name: str, objects: tuple[GeoObject, ...]) -> Predicate:
    """
    Constructs a predicate.
    This function delegates the predicate construction to the proper classes, and allows building predicates safely.
    @param name: The name of the predicate
    @param args: The arguments for the predicate.
    @return: A predicate object of the specified type acting on the specified objects.
    """
    match name:
        case _ if name in SIMPLE_SYMMETRIC_PREDICATE_NAMES:
            return SymmetricPredicate(name, objects)
        case BetweenPredicate.NAME:
            return BetweenPredicate(objects)
        case DistinctPredicate.NAME:
            return DistinctPredicate(objects)
        case ExistsPredicate.NAME:
            return ExistsPredicate(objects)
        case IdenticalPredicate.NAME:
            return IdenticalPredicate(objects)
        case NotOneOfPredicate.NAME:
            return NotOneOfPredicate(objects)
        case ConvexPredicate.NAME:
            return ConvexPredicate(objects)
        case InPredicate.NAME:
            return InPredicate(objects)
        case TangentPredicate.NAME:
            return TangentPredicate(objects)
        case _ if name in get_macros():
            return MacroPredicate(name, objects)
        case _:
            return Predicate(name, objects)
