import abc
from typing import Any, Generic, TypeVar

from util import Bijection

from . import linear_b

T = TypeVar('T', float, int, bool)
O = TypeVar('O')


def sparse_repr(rel: dict):
    """
    Represents a dictionary mapping objects to their coefficients in the equation.
    """
    res = ''
    for key, val in rel.items():
        if val == 0:
            continue
        if res:
            if val > 0:
                res += ' + '
            elif val < 0:
                res += ' - '
                val = -val

        if val == 1:
            res += str(key)
        else:
            res += f'{val}*{key}'
    return res


class BaseSolver(abc.ABC, Generic[T, O]):
    solver: Any
    id_map: Bijection[O, int]

    @abc.abstractmethod
    def dtype(self) -> type: ...

    def get_id(self, obj: O) -> int:
        """
        Gets the Rust ID of the object.
        """
        if obj in self.id_map:
            return self.id_map[obj]
        h = hash(obj)
        self.id_map[obj] = h
        return h

    def add_objects(self, objects: list[O]):
        self.solver.add_objects([self.get_id(obj) for obj in objects])

    def add_relation(self, v: dict[O, Any]):
        return self.solver.add_relation(self.normalize_rel(v))

    def add_nonzero(self, v: dict[O, Any]):
        return self.solver.add_nonzero(self.normalize_rel(v))

    def contains_relation(self, v: dict[O, Any]) -> bool:
        return self.solver.contains_relation(self.normalize_rel(v))

    def contains_nonzero(self, v: dict[O, Any]):
        res = self.solver.contains_nonzero(self.normalize_rel(v))
        return res

    def contains(self, obj: O):
        return self.solver.contains(self.get_id(obj))

    def get_value(self, rel: dict[O, Any]) -> T | None:
        return self.solver.get_value(self.normalize_rel(rel))

    def indices(self) -> dict[O, int]:
        return self.solver.indices()

    def normalize(self, v: Any) -> T:
        return self.dtype()(v)

    def normalize_rel(self, rel: dict[O, Any]) -> dict[int, T]:
        res = {}
        for key, val in rel.items():
            res[self.get_id(key)] = self.normalize(val)
        return res

    def print(self):
        """
        Prints a pretty representation of the linear solver.
        """
        print(type(self))
        print('Relations:')
        rels: list[list[tuple[int, T]]] = self.solver.relations()
        for rel in rels:
            print(sparse_repr({self.id_map.backward(k): v for k, v in rel}))
        print('Nonzeroes:')
        nonz: list[list[tuple[int, T]]] = self.solver.nonzeroes()
        for rel in nonz:
            print(sparse_repr({self.id_map.backward(k): v for k, v in rel}), '!= 0')

    def find_combinations(self, coefficients: list, const_coefficient, coef_objects: list[list[O]]) -> list[list[O]]:
        """
        Finds all combinations of variables in the linear solver that satisfy the given relation.

        Parameters:
        * `coefficients`: The coefficients in the linear equation. For 2x + 3y + 5, that would be [2, 3].
        * `const_coefficient`: The coefficient of the constant term in the linear equation. For 2x + 3y + 5, that would be 5.
        * `coef_objects`: A list of objects that can be placed in place of each variable of the equation.

        Return:

        A list of lists of objects with which the variables can be substituted such that the equation holds.
        """
        coefficients = [self.normalize(v) for v in coefficients]
        const_coefficient = self.normalize(const_coefficient)
        coef_keys = [[self.get_id(o) for o in lst] for lst in coef_objects]
        res: list[list[int]] = self.solver.find_combinations(coefficients, const_coefficient, coef_keys)

        return [[self.id_map.backward(o) for o in lst] for lst in res]

    def reduce(self, rel: dict[O, Any]) -> dict[O, Any]:
        """
        Transforms the given relation to a canonical representative modulo the relations.
        """
        return {self.id_map.backward(key): val for key, val in self.solver.reduce(self.normalize_rel(rel)).items()}


class RLinearSolver(Generic[O], BaseSolver[float, O]):
    def __init__(self, const_idx: int | None = None, solver=None, id_map: Bijection[O, int] | None = None):
        if solver is None:
            self.solver = linear_b.RSparseLinearSolver(const_idx)
            self.id_map = Bijection()
        else:
            self.solver = solver
            assert id_map is not None
            self.id_map = id_map

    def clone(self) -> 'RLinearSolver[O]':
        return RLinearSolver(solver=self.solver.clone(), id_map=self.id_map.clone())

    def dtype(self) -> type:
        return float

    def __copy__(self) -> 'RLinearSolver[O]':
        return self.clone()

    def __deepcopy__(self, memo) -> 'RLinearSolver[O]':
        if id(self) in memo:
            return memo[id(self)]
        res = self.clone()
        memo[id(self)] = res
        return res


class ModLinearSolver(Generic[O], BaseSolver[int, O]):
    def __init__(self, const_idx: int | None = None, solver=None, id_map: Bijection[O, int] | None = None):
        if solver is None:
            self.solver = linear_b.ModSparseLinearSolver(const_idx)
            self.id_map = Bijection()
        else:
            self.solver = solver
            assert id_map is not None
            self.id_map = id_map

    def clone(self) -> 'ModLinearSolver[O]':
        return ModLinearSolver(solver=self.solver.clone(), id_map=self.id_map.clone())

    def dtype(self) -> type:
        return int

    def __copy__(self) -> 'ModLinearSolver[O]':
        return self.clone()

    def __deepcopy__(self, memo) -> 'ModLinearSolver[O]':
        if id(self) in memo:
            return memo[id(self)]
        res = self.clone()
        memo[id(self)] = res
        return res


class BoolLinearSolver(Generic[O], BaseSolver[bool, O]):
    def __init__(self, const_idx: int | None = None, solver=None, id_map: Bijection[O, int] | None = None):
        if solver is None:
            self.solver = linear_b.BoolSparseLinearSolver(const_idx)
            self.id_map = Bijection()
        else:
            self.solver = solver
            assert id_map is not None
            self.id_map = id_map

    def normalize(self, v: Any) -> bool:
        if isinstance(v, int):
            return bool(v % 2)
        return bool(v)

    def dtype(self) -> type:
        return bool

    def clone(self) -> 'BoolLinearSolver[O]':
        return BoolLinearSolver(solver=self.solver.clone(), id_map=self.id_map.clone())

    def __copy__(self) -> 'BoolLinearSolver[O]':
        return self.clone()

    def __deepcopy__(self, memo) -> 'BoolLinearSolver[O]':
        if id(self) in memo:
            return memo[id(self)]
        res = self.clone()
        memo[id(self)] = res
        return res
