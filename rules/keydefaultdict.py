from typing import Callable


class KeyDefaultDict[K, V](dict[K, V]):
    default_factory: Callable[[K], V]

    def __init__(self, default_factory: Callable[[K], V]):
        self.default_factory = default_factory

    def __missing__(self, key: K) -> V:
        return self.default_factory(key)
