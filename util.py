from os.path import dirname, abspath
from pathlib import Path
from typing import Generic, TypeVar

BASE_PATH = Path(dirname(abspath(__file__)))

K = TypeVar('K')
V = TypeVar('V')


class Bijection(Generic[K, V]):
    """
    A dictionary for a one-to-one mapping, allowing finding the inverse of every value.
    """

    forward: dict[K, V]
    back: dict[V, K]

    def __init__(self, forward: dict[K, V] | None = None, back: dict[V, K] | None = None):
        self.forward = forward or {}
        self.back = back or {}

    def rev(self) -> 'Bijection[V, K]':
        """
        Returns the reverse bijection, mapping values to keys.
        """
        return Bijection(self.back, self.forward)

    def backward(self, v: V) -> K:
        return self.back[v]

    def contains_value(self, v: V) -> bool:
        """
        Checks if the given value is in the image of the bijection.
        """
        return v in self.back

    def __getitem__(self, k: K):
        return self.forward[k]

    def __setitem__(self, k: K, v: V):
        assert v not in self.back, f'Attempted to use the target value {v} twice, for the keys {self.back[v]} and {k}.'
        if k in self.forward:
            del self.back[self.forward[k]]
        self.forward[k] = v
        self.back[v] = k

    def __delitem__(self, k: K):
        v = self.forward[k]
        del self.forward[k]
        del self.back[v]

    def __contains__(self, key: K) -> bool:
        return key in self.forward

    def __len__(self) -> int:
        return len(self.forward)

    def __repr__(self) -> str:
        return repr(self.forward)

    def __str__(self) -> str:
        return str(self.forward)

    def clone(self) -> 'Bijection[K, V]':
        return Bijection(dict(self.forward), dict(self.back))
