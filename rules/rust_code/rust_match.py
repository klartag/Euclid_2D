from . import linear_b
from typing import TypeVar, Any

from rules.proof_checker_utils import KNOWN_KEYS


V = TypeVar('V')

class RustMatch:
    """
    A class handling large collections of mappings from one set of objects to another set of objects.
    The mappings behave as dictionaries, all sharing the same set of keys, and are unique.
    """
    _internal: Any

    def __init__(self, _internal):
        self._internal = _internal

    @staticmethod
    def raw(keys: list[int], values: list[list[int]]) -> 'RustMatch':
        return RustMatch(linear_b.MatchingHash(keys, values))

    @staticmethod
    def of(a: int, b: int) -> 'RustMatch':
        """
        Returns an object containing the single mapping {a: b}.
        """
        return RustMatch(linear_b.MatchingHash.of(a, b))

    @staticmethod
    def one() -> 'RustMatch':
        """
        Returns an object containing the empty mapping {}.
        The empty mapping is the equivalent of 1 in the ring.
        """
        return RustMatch(linear_b.MatchingHash.one())

    @staticmethod
    def zero() -> 'RustMatch':
        """
        Returns an object containing no mapping. 
        The illegal mapping is the equivalent of 0 in the ring.
        """
        return RustMatch(linear_b.MatchingHash.zero())
    
    def is_one(self) -> bool:
        """
        Checks if the mapping object is the empty mapping.
        """
        return self._internal.is_one()
    
    def is_zero(self) -> bool:
        """
        Checks if the mapping object contains no mapping.
        """
        return self._internal.is_zero()
    
    def is_nonzero(self) -> bool:
        """
        Checks if the mapping object contains any mapping.
        """
        return self._internal.is_nonzero()

    def product(self, other: 'RustMatch') -> 'RustMatch':
        """
        Returns the product of the mappings:
        For a mapping {k1: v1, ...} and {q1: w1, ...}, the product is defined as {k1: v1, ..., q1: w1, ...} 
        if the two mappings agree on all shared keys, and is nonexistent otherwise.
        """
        return RustMatch(self._internal.product(other._internal))
    
    @staticmethod
    def concat(matchings: 'list[RustMatch]') -> 'RustMatch':
        """
        Concatenates two sets of mappings, deduplicating if necessary.
        """
        return RustMatch(linear_b.MatchingHash.concat([m._internal for m in matchings]))
    
    def keys(self) -> list[int]:
        """
        Returns the internal keys used by the mapping.
        """
        return self._internal.keys()
    
    def values(self) -> list[list[int]]:
        """
        Returns the internal values sued by the mapping.
        """
        return self._internal.matchings()
    
    def to_dict(self, src_objects: dict[int, V], tar_objects: dict[int, V]|None = None) -> list[dict[V, V]]:
        """
        Converts the matchings to a Python-friendly list of dicts.
        @param src_objects: A mapping from unique keys to objects, used to map the source of the match (Usually the objects in the theorems).
        @param tar_objects: A second mapping from keys to objects, used to map the targets of the match (Usually the objects in the checker).
        If none, the src_objects map will be used.
        """
        if tar_objects is None:
            tar_objects = src_objects
        res = []
        keys = self.keys()
        values = self.values()

        for key in keys:
            if key not in src_objects:
                raise KeyError(f'RustMatch::to_dict error! Missing key: {key}. Real obj: {KNOWN_KEYS[key].name if key in KNOWN_KEYS else "???"}')
        key_objects = [src_objects[key] for key in keys]
        for row in values:
            # print('Known keys: ', [KNOWN_KEYS[tar_idx] for tar_idx in row])
            res.append({key_obj: tar_objects[tar_idx] for key_obj, tar_idx in zip(key_objects, row)})
        return res
    
    def __len__(self) -> int:
        """
        Returns the number of mappings stored in the RustMatch object.
        """
        return self._internal.len()
    
    def map_keys(self, map: dict[int, int]) -> 'RustMatch':
        """
        Maps the keys of the matching.
        """
        return RustMatch(self._internal.map_keys(map))

    def subtract(self, other: 'RustMatch') -> 'RustMatch': 
        return RustMatch(self._internal.subtract(other._internal))
    
    def extend(self, other: 'RustMatch'):
        self._internal.extend(other._internal)

    def clone(self) -> 'RustMatch':
        return RustMatch(self._internal.clone())
    
    def __copy__(self) -> 'RustMatch':
        return self.clone()

    def __deepcopy__(self, memo) -> 'RustMatch':
        if id(self) in memo:
            return memo[id(self)]
        res = self.clone()
        memo[id(self)] = res
        return res
