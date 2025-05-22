from typing import Iterable, TypeVar

V = TypeVar('V')

EPSILON = 1e-9


def count(iter: Iterable) -> int:
    """
    Counts the number of objects in the given iterable.
    """
    return sum(1 for _ in iter)


def unpack_dict(d: dict[str, str]) -> tuple[str, str]:
    """
    Given a dictionary of length 1, returns the (key, value) tuple.
    """
    assert isinstance(d, dict) and len(d) == 1, f'Failed to unpack {d}'
    return next(iter(d.items()))


def union(sets: Iterable[set[V]]) -> set[V]:
    """
    Computes the union of all given sets.
    """
    res = set()
    for s in sets:
        res |= s
    return res


def preprocess_lines(lines: Iterable[str]) -> Iterable[str]:
    """
    Removes comments from the lines and removes empty lines.
    """
    for line in lines:
        if '#' in line:
            line = line.split('#')[0]
        line = line.rstrip()
        if line:
            yield line
