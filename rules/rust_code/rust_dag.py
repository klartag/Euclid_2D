from typing import Generic, TypeVar
from linear_b import RustPredicate, RustPattern, RustSignatureDag


class RPredicate:
    """
    A wrapper around the Rust predicate.
    """

    internal: RustPredicate

    def __init__(self, id: int | None = None, args: list[int] | None = None, internal: RustPredicate | None = None):
        if internal is not None:
            self.internal = internal
        else:
            self.internal = RustPredicate(id, args)

    def id(self) -> int:
        return self.internal.pred_id()

    def args(self) -> list[int]:
        return self.internal.arg_ids()

    def __repr__(self) -> str:
        return f'RPredicate({self.id()}, {self.args()})'

    def __str__(self) -> str:
        return self.__repr__()


class RPattern:
    """
    A wrapper around the Rust pattern.
    """

    pattern: RustPattern

    def __init__(self, pattern: RustPattern):
        self.pattern = pattern

    def __repr__(self):
        return self.pattern.to_string()


T = TypeVar('T')


class RDag(Generic[T]):
    """
    A wrapper around the Rust signature DAG.
    """

    internal: RustSignatureDag
    outputs: dict[int, T]

    def __init__(self) -> None:
        self.internal = RustSignatureDag()
        self.outputs = {}

    def get_predicate_pattern(self, pred: RPredicate) -> RPattern:
        """
        Gets the pattern corresponding to the given predicate.
        """
        return RPattern(self.internal.get_predicate_pattern(pred.internal))

    def get_intersection_pattern(self, patterns: list[RPattern]) -> RPattern:
        """
        Gets the pattern corresponding to the intersection of the given set of patterns.
        """
        return RPattern(self.internal.get_intersection_pattern([pattern.pattern for pattern in patterns]))

    def add_predicate(self, pred: RPredicate):
        """
        Adds the given predicate to the list of tracked predicates.
        """
        self.internal.add_predicate(pred.internal)

    def add_out_pattern(self, pattern: RPattern, out: T):
        """
        Links the given pattern to the given output.
        """
        idx = len(self.outputs)
        self.outputs[idx] = out
        self.internal.add_out_pattern(pattern.pattern, idx)

    def update(self) -> list[tuple[T, list[int]]]:
        """
        Returns the new matches to the patterns in the RustDag.
        """
        return [(self.outputs[idx], args) for idx, args in self.internal.update()]

    def sorted_patterns(self) -> list[RPattern]:
        """
        Returns all the patterns in the DAG.
        """
        return [RPattern(pattern) for pattern in self.internal.sorted_patterns()]
