from typing import Callable, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class ExtendedDefaultDict[K, V](dict[K, V]):
    default_factory: Callable[[K], V]

    def __init__(self, default_factory: Callable[[K], V]):
        self.default_factory = default_factory

    def __missing__(self, key: K) -> V:
        self[key] = self.default_factory(key)
        return self[key]
