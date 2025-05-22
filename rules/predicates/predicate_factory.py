import re

from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.parse import parse_geo_object
from ..expression_parse_utils import split_args
from ..errors import ProofParseError

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


def parse_predicate(predicate_data: str, obj_map: dict[str, GeoObject]) -> Predicate:
    """
    Parses a string representation of a predicate.
    The string representation of the predicate is in the format name(x, y, z).
    The names in the predicate might include unnamed objects, such as Line(a, b) or distance(a, b).

    There are four special predicate formats:
    - equals, which can be stated as ==
    - not_equals, which can be stated as !=
    - equals_mod, which can be stated as A == B mod C
    - in, which can be stated as A in B.
    """
    predicate_data = predicate_data.strip()
    # Attempting to match A == B mod C
    if (match := re.fullmatch(PREDICATE_EQ_MOD_PATTERN, predicate_data)) is not None:
        left, right, mod = match.groups()
        left = parse_geo_object(left, obj_map)
        right = parse_geo_object(right, obj_map)
        return predicate_from_args(f'equals_mod_{mod}', (left, right))

    # Attempting to match A == B
    if (match := re.fullmatch(PREDICATE_EQ_PATTERN, predicate_data)) is not None:
        left, right = match.groups()
        left = parse_geo_object(left, obj_map)
        right = parse_geo_object(right, obj_map)
        return predicate_from_args('equals', (left, right))

    # Attempting to match A != B mod C
    if (match := re.fullmatch(PREDICATE_NE_MOD_PATTERN, predicate_data)) is not None:
        left, right, mod = match.groups()
        left = parse_geo_object(left, obj_map)
        right = parse_geo_object(right, obj_map)
        return predicate_from_args(f'not_equals_mod_{mod}', (left, right))

    # Attempting to match A != B
    if (match := re.fullmatch(PREDICATE_NE_PATTERN, predicate_data)) is not None:
        left, right = match.groups()
        left = parse_geo_object(left, obj_map)
        right = parse_geo_object(right, obj_map)
        return predicate_from_args('not_equals', (left, right))

    # Attempting to match A in B
    if (match := re.fullmatch(PREDICATE_NOT_IN_PATTERN, predicate_data)) is not None:
        left, right = match.groups()
        left = parse_geo_object(left, obj_map)
        right = parse_geo_object(right, obj_map)
        return predicate_from_args('not_in', (left, right))

    # Attempting to match A in B
    if (match := re.fullmatch(PREDICATE_IN_PATTERN, predicate_data)) is not None:
        left, right = match.groups()
        args = []
        for l in split_args(left):
            args.append(parse_geo_object(l, obj_map))
        for r in split_args(right):
            args.append(parse_geo_object(r, obj_map))
        return predicate_from_args('in', tuple(args))
    # Matching the general pattern.
    match = re.fullmatch(PREDICATE_GENERAL_PATTERN, predicate_data)
    if match is None:
        raise ProofParseError(f'Failed to parse predicate: {predicate_data}!')

    name, args = match.groups()
    if args.strip():
        objects = tuple(parse_geo_object(arg, obj_map) for arg in split_args(args))
    else:
        objects = ()
    return predicate_from_args(name, objects)
