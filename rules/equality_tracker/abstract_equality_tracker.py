from abc import ABC, abstractmethod
from collections import defaultdict
from typing import DefaultDict, Optional

from ..keydefaultdict import KeyDefaultDict

from .types import Equation, Apply

class AbstractEqualityTracker[T, S](ABC):
    pending: list[Equation[S, S] | tuple[Equation[Apply[S, S], S], Equation[Apply[S, S], S]]]
    representatives: KeyDefaultDict[S, S]
    class_lists: KeyDefaultDict[S, list[S]]
    use_lists: DefaultDict[S, list[Equation[Apply[S, S], S]]]
    lookup_table: DefaultDict[(S, S), Optional[Equation[Apply[S, S], S]]]

    def __init__(self):
        self.pending = []
        self.representatives = KeyDefaultDict(lambda s: s)
        self.class_lists = KeyDefaultDict(lambda s: [s])
        self.use_lists = defaultdict(list)
        self.lookup_table = defaultdict(lambda: None)

    def merge(self, x: T, y: T):
        _x = self.currify(x)
        _y = self.currify(y)
        raise NotImplementedError()

    def _propogate(self):
        while len(self.pending) > 0:
            e = self.pending.pop()
            if isinstance(e, Equation):
                a, b = e.lhs, e.rhs
            else:
                a, b = e[0].rhs, e[1].rhs
            a_repr = self.representatives[a]
            b_repr = self.representatives[b]
            if a_repr == b_repr:
                continue
            if len(self.class_lists[b_repr]) < len(self.class_lists[a_repr]):
                a_repr, b_repr = b_repr, a_repr
            a_repr_old = a_repr
            for c in self.class_lists[a_repr_old]:
                self.representatives[c] = b_repr
                self.class_lists[b_repr].append(c)
                self.class_lists[a_repr].remove(c)
            for equation in list(self.use_lists[a_repr_old]):
                equation_representatives = Equation(self.representatives[equation.lhs[0]], self.representatives[equation.rhs[1]])
                lookup = self.lookup_table[
                    
                ]
                if lookup is not None:
                    self.pending.append((equation, lookup))
                    self.use_lists[a_repr_old].remove(equation)
                else:
                    self.lookup_table[()]

    def normalize(self, x: T) -> T:
        _x = self.currify(x)
        raise NotImplementedError()
        y = self.decurrify(_x)
        return y

    def are_congruent(self, x: T, y: T) -> bool:
        _x = self.currify(x)
        _y = self.currify(y)
        raise NotImplementedError()

    @abstractmethod
    def currify(self, x: T) -> S: ...

    @abstractmethod
    def decurrify(self, x: S) -> T: ...
