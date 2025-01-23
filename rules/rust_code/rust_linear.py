import abc
from typing import Any, Generic, TypeVar
import linear_b
from ..rule_utils import GeometryError

T = TypeVar('T', float, int, bool)


def repr_row(row: list[T], pos_to_name: dict[int, str]) -> str:
    """
    Represents the row in a readable format.
    """
    res = ''
    for idx, val in enumerate(row):
        name = pos_to_name[idx]
        if val == 0:
            continue
        elif val == 1:
            res += f' + {name}'
        elif val == -1:
            res += f' - {name}'
        elif val < 0 and name != '1':
            res += f' - {abs(val)}*{name}'
        elif val < 0 and name == '1':
            res += f' - {abs(val)}'
        elif val > 0 and name != '1':
            res += f' + {abs(val)}*{name}'
        elif val > 0 and name == '1':
            res += f' + {abs(val)}'
        else:
            res += '+ ???'

    return res


class BaseSolver(abc.ABC, Generic[T]):
    solver: Any

    @abc.abstractmethod
    def dtype(self) -> type: ...

    def add_objects(self, objects: list[int]):
        self.solver.add_objects(objects)

    def reduce(self, v: list[T], normalize=True) -> list[T]:
        if normalize:
            return self.solver.reduce(self.normalize_row(v))
        else:
            return self.solver.reduce(v)

    def reduce_rel(self, v: dict[int, Any]) -> list[T]:
        return self.solver.reduce_rel(self.normalize_rel(v))

    def add_relation(self, v: dict[int, Any]):
        return self.solver.add_relation(self.normalize_rel(v))

    def add_nonzero(self, v: dict[int, Any]):
        return self.solver.add_nonzero(self.normalize_rel(v))

    def contains_relation(self, v: dict[int, Any]) -> bool:
        return self.solver.contains_relation(self.normalize_rel(v))

    def contains_nonzero(self, v: dict[int, Any]):
        res = self.solver.contains_nonzero(self.normalize_rel(v))
        return res

    def contains(self, obj_idx: int):
        return self.solver.contains(obj_idx)

    def get_value(self, rel: dict[int, Any]) -> T | None:
        return self.solver.get_value(rel)

    def indices(self) -> dict[int, int]:
        return self.solver.indices()

    def relations(self) -> list[list[T]]:
        return self.solver.relations()

    def nonzeroes(self) -> list[list[T]]:
        return self.solver.nonzeroes()

    def normalize(self, v: Any) -> T:
        return self.dtype()(v)

    def normalize_row(self, row: list) -> list[T]:
        return [self.normalize(i) for i in row]

    def normalize_rel(self, rel: dict[int, Any]) -> dict[int, T]:
        res = {}
        for key, val in rel.items():
            res[key] = self.normalize(res.get(key, 0) + val)
        return res

    def print_relations(self, names_dict: dict[int, str]):
        """
        Prints all relations in the linear algebra tracker.
        """
        indices: dict[int, int] = self.indices()
        relations: list[list[T]] = self.relations()

        pos_to_name = {pos: names_dict.get(idx, f'?({idx%1000})') for idx, pos in indices.items()}

        for rel in relations:
            print(repr_row(rel, pos_to_name) + ' == 0')

    def print_nonzeroes(self, names_dict: dict[int, str]):
        """
        Prints all nonzeroes in the linear algebra tracker.
        """
        indices: dict[int, int] = self.indices()
        nonzeroes: list[list[T]] = self.nonzeroes()

        pos_to_name = {pos: names_dict.get(idx, f'?({idx%1000})') for idx, pos in indices.items()}

        for rel in nonzeroes:
            print(repr_row(rel, pos_to_name) + ' != 0')


class RLinearSolver(BaseSolver[float]):
    def __init__(self, const_idx: int | None = None, solver=None):
        if solver is None:
            assert const_idx is not None
            self.solver = linear_b.RLinearSolver(const_idx)
            self.add_objects([const_idx])
        else:
            self.solver = solver

    def clone(self) -> 'RLinearSolver':
        return RLinearSolver(solver=self.solver.clone())

    def dtype(self) -> type:
        return float

    def __copy__(self) -> 'RLinearSolver':
        return self.clone()

    def __deepcopy__(self, memo) -> 'RLinearSolver':
        if id(self) in memo:
            return memo[id(self)]
        res = self.clone()
        memo[id(self)] = res
        return res

    def find_combinations(self, coefficients: list, const_coefficient, coef_keys: list[list[int]]) -> list[list[int]]:
        """
        Finds all combinations of variables in the linear solver that satisfy the given relation.
        """
        coefficients = [self.normalize(v) for v in coefficients]
        const_coefficient = self.normalize(const_coefficient)

        return self.solver.find_combinations(coefficients, const_coefficient, coef_keys)


class ModLinearSolver(BaseSolver[int]):
    def __init__(self, const_idx: int | None = None, solver=None):
        if solver is None:
            assert const_idx is not None
            self.solver = linear_b.ModLinearSolver(const_idx)
            self.add_objects([const_idx])
        else:
            self.solver = solver

    def dtype(self) -> type:
        return int

    def normalize(self, v: Any) -> int:
        return round(v)

    def clone(self) -> 'ModLinearSolver':
        return ModLinearSolver(solver=self.solver.clone())

    def __copy__(self) -> 'ModLinearSolver':
        return self.clone()

    def __deepcopy__(self, memo) -> 'ModLinearSolver':
        if id(self) in memo:
            return memo[id(self)]
        res = self.clone()
        memo[id(self)] = res
        return res

    def find_combinations(self, coefficients: list, const_coefficient, coef_keys: list[list[int]]) -> list[list[int]]:
        """
        Finds all combinations of variables in the linear solver that satisfy the given relation.
        """
        coefficients = [self.normalize(v) for v in coefficients]
        const_coefficient = self.normalize(const_coefficient)

        return self.solver.find_combinations(coefficients, const_coefficient, coef_keys)


class BoolLinearSolver(BaseSolver[bool]):
    def __init__(self, const_idx: int | None = None, solver=None):
        if solver is None:
            assert const_idx is not None
            self.solver = linear_b.BoolLinearSolver(const_idx)
            self.add_objects([const_idx])
        else:
            self.solver = solver

    def normalize(self, v: Any) -> bool:
        if isinstance(v, int):
            return bool(v % 2)
        return bool(v)

    def dtype(self) -> type:
        return bool

    def clone(self) -> 'BoolLinearSolver':
        return BoolLinearSolver(solver=self.solver.clone())

    def __copy__(self) -> 'BoolLinearSolver':
        return self.clone()

    def __deepcopy__(self, memo) -> 'BoolLinearSolver':
        if id(self) in memo:
            return memo[id(self)]
        res = self.clone()
        memo[id(self)] = res
        return res

    def find_combinations(self, coefficients: list, const_coefficient, coef_keys: list[list[int]]) -> list[list[int]]:
        """
        Finds all combinations of variables in the linear solver that satisfy the given relation.
        """
        coefficients = [self.normalize(v) for v in coefficients]
        const_coefficient = self.normalize(const_coefficient)

        return self.solver.find_combinations(coefficients, const_coefficient, coef_keys)
