import itertools
from typing import Generic, Iterable, TypeVar

import numpy as np

K = TypeVar('K')
V = TypeVar('V')

EPSILON = 1e-9


# Types
SCALAR = 'Scalar'
POINT = 'Point'
LINE = 'Line'
ANGLE = 'Angle'
ORIENTATION = 'Orientation'
LITERAL = 'Literal'
CIRCLE = 'Circle'
NULL = 'Null'
"""The null type is the type of GeoObjects which are just placeholders for other things."""

R_EQN_TYPES = (SCALAR, ANGLE)
EQN_TYPES = (SCALAR, ANGLE, LITERAL, ORIENTATION)
ALL_TYPES = (SCALAR, POINT, LINE, ANGLE, ORIENTATION, LITERAL, CIRCLE, NULL)

class GeometryError(RuntimeError):
    """
    A generic error for the geometry project.
    """

class ProofParseError(GeometryError):
    """
    An error raised when attempting to parse data results in invalid objects.
    """

class ProofCheckError(GeometryError):
    """
    An error in proof checking. Shows that the proof is incorrect.
    """

class IllegalObjectError(ProofCheckError):
    """
    An error in proof checking. Shows that the proof is incorrect.
    """
#####################
# General utilities #
#####################

def count(iter: Iterable) -> int:
    """
    Counts the number of objects in the given iterable.
    """
    return sum(1 for _ in iter)


#################
# Parsing tools #
#################
    
def unpack_dict(d: dict[str, str]) -> tuple[str, str]:
    """
    Given a dictionary of length 1, returns the (key, value) tuple.
    """
    assert isinstance(d, dict) and len(d) == 1, f'Failed to unpack {d}'
    return next(iter(d.items()))

def split_args(s: str) -> list[str]:
    """
    Splits the given string using commas, while ignoring commas inside parentheses.
    """
    paren_depth = 0
    split_indices = [-1]
    for idx, c in enumerate(s):
        match c:
            case ',':
                if paren_depth == 0:
                    split_indices.append(idx)
            case '(' | '[' | '{':
                paren_depth += 1
            case ')' | ']' | '}':
                paren_depth -= 1
    split_indices.append(len(s))
    return [s[i+1:j].strip() for i, j in zip(split_indices, split_indices[1:])]

####################################
# Proof-Checker specific utilities #
####################################



####################
# Dictionary tools #
####################


def union(sets: Iterable[set[V]]) -> set[V]:
    """
    Computes the union of all given sets.
    """
    res = set()
    for s in sets:
        res |= s
    return res


class NpContext(Generic[K, V]):
    """
    A mapping of objects to ints.
    """
    src_objects: list[K]
    src_objects_idx: dict[K, int]
    tar_objects: list[V]
    tar_objects_idx: dict[V, int]

    def __init__(self, src_objects: list[K], tar_objects: list[V]):
        self.src_objects = src_objects
        self.src_objects_idx = {obj: idx for idx, obj in enumerate(src_objects)}
        self.tar_objects = tar_objects
        self.tar_objects_idx = {obj: idx for idx, obj in enumerate(tar_objects)}

class NpMatch:
    """
    An attempt to build the matchings based on numpy arrays.
    The indices of the array are [match_idx, src_idx], and the value is [tar_idx].
    The target indices must not be -1, as -1 is used for the unmatched value.
    """
    _EMPTY = -1
    
    arr: np.ndarray
    context: NpContext

    """An int array specifying the legal matchings."""
    def __init__(self, arr: np.ndarray, context: NpContext):
        self.arr = arr
        self.context = context

    @staticmethod
    def empty(context: NpContext) -> 'NpMatch':
        """
        Returns a matching with no data.
        """
        return NpMatch(np.full((1, len(context.src_objects)), -1, dtype=int), context)
    
    @staticmethod
    def illegal(context: NpContext) -> 'NpMatch':
        """
        Returns a matching specifying that no matching is possible.
        """
        return NpMatch(np.full((0, len(context.src_objects)), -1, dtype=int), context)

    @staticmethod
    def of(key, value, context: NpContext) -> 'NpMatch':
        res = NpMatch.empty(context)
        if key not in context.src_objects_idx:
            raise KeyError(f'{key=} not in context!')
        if value not in context.tar_objects_idx:
            raise KeyError(f'{value=} not in context!')
        res.arr[0][context.src_objects_idx[key]] = context.tar_objects_idx[value]
        return res

    def product(self, other: 'NpMatch') -> 'NpMatch':
        """
        Merges two match objects.
        If the matches do not agree on some mapping, returns none.
        """
        if len(self.arr) == 0 or other.is_empty():
            return self
        if len(other.arr) == 0 or self.is_empty():
            return other
        if len(self.arr) * len(other.arr) > 5000:
            return self._fast_product(other)
        self_reshape = self.arr[:, np.newaxis, :]
        other_reshape = other.arr[np.newaxis, :, :]
        merge = self_reshape & other_reshape
        cell_match = (self_reshape == other_reshape) | (self_reshape == NpMatch._EMPTY) | (other_reshape == NpMatch._EMPTY)
        row_match = np.all(cell_match, axis=-1)

        return NpMatch(merge[row_match.nonzero()], self.context)
    
    def _fast_product(self, other):
        self_reshape = self.arr[:, np.newaxis, :]
        other_reshape = other.arr[np.newaxis, :, :]
        merge = self_reshape & other_reshape
        cell_match = (self_reshape == other_reshape) | (self_reshape == NpMatch._EMPTY) | (other_reshape == NpMatch._EMPTY)
        row_match = np.all(cell_match, axis=-1)

        res = NpMatch(merge[row_match.nonzero()], self.context)
        # print('Prod fin')
        return res

    def is_empty(self) -> bool:
        return len(self.arr) == 1 and bool(np.all(self.arr == NpMatch._EMPTY))

    def to_dict(self) -> list[dict]:
        """
        Converts the NpMatch to a list of dictionaries.
        """
        res = []
        for row in self.arr:
            res.append({self.context.src_objects[src]: self.context.tar_objects[tar] for src, tar in enumerate(row) if tar != NpMatch._EMPTY})
        return res
    
    @staticmethod
    def concat(matches: list['NpMatch'], context: NpContext) -> 'NpMatch':
        """
        Returns the union of all given matches.
        """
        if len(matches) == 0:
            return NpMatch.illegal(context)
        
        return NpMatch(np.concatenate([match.arr for match in matches]), context)

    def is_illegal(self) -> bool:
        """
        Returns if there is a legal match in the assignment.
        """
        return len(self.arr) == 0

    def __len__(self) -> int:
        return len(self.arr)


def dicts_match(d1: dict[K, V], d2: dict[K, V]) -> bool:
    """
    Checks if the dicts agree on the intersection of their keys.
    """
    return all(k not in d2 or d2[k] == v for k, v in d1.items())

def dict_union(*v: dict[K, V] | None) -> dict[K, V] | None:
    """
    Merges a list of dictionaries into a single dictionary if they match, and returns None if they don't.
    """
    if any(x is None for x in v):
        return None
    
    res = {}
    for d in v:
        if d is None:
            return None

        for key, value in d.items():
            if key in res and res[key] != value:
                return None
            else:
                res[key] = value
    return res

def dicts_cross_product(v: list[dict[K, V]], w: list[dict[K, V]]) -> list[dict[K, V]]:
    """
    Goes over the cross-product of the two lists of dictionaries,
    and returns a list of the unions of all consistent pairs
    """
    res = []
    for x in v:
        for y in w:
            if (d := dict_union(x, y)) is not None:
                res.append(d)

    # print(len(v), len(v[0] if v else []), len(w), len(res))
    return res
