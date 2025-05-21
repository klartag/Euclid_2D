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
    return [s[i + 1 : j].strip() for i, j in zip(split_indices, split_indices[1:])]


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
