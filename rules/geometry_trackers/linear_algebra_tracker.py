from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.literal import ONE

from ..proof_checker_utils import get_eqn_key
from ..rust_code.rust_sparse_linear import BaseSolver, BoolLinearSolver, ModLinearSolver, RLinearSolver


class LinearAlgebraTracker:
    """
    A class that checks that a proof is valid.
    """

    """An object tracking linear equations in R."""
    _real_equations: RLinearSolver[GeoObject]
    """An object tracking linear equations in Z/360."""
    _mod_360_equations: ModLinearSolver[GeoObject]
    """An object tracking linear equations over the booleans."""
    _bool_equations: BoolLinearSolver[GeoObject]

    def __init__(self):
        one_key = get_eqn_key(ONE)
        self._real_equations = RLinearSolver(one_key)
        self._real_equations.add_nonzero({ONE: 1})

        self._mod_360_equations = ModLinearSolver(one_key)
        self._mod_360_equations.add_relation({ONE: 360})
        self._mod_360_equations.add_nonzero({ONE: 180})
        self._mod_360_equations.add_nonzero({ONE: 120})
        self._mod_360_equations.add_nonzero({ONE: 72})

        self._bool_equations = BoolLinearSolver(one_key)
        self._bool_equations.add_objects([ONE])

    def trackers(self) -> list[BaseSolver]:
        """
        Returns the list of trackers of the proof checker.
        """
        return [self._bool_equations, self._mod_360_equations, self._real_equations]

    def add_real_relation(self, relation):
        self._real_equations.add_relation(relation)
        self._mod_360_equations.add_relation(relation)

    def add_mod_360_relation(self, relation):
        self._mod_360_equations.add_relation(relation)

    def add_bool_relation(self, relation):
        self._bool_equations.add_relation(relation)

    def add_real_nonzero(self, relation):
        self._real_equations.add_nonzero(relation)

    def add_mod_360_nonzero(self, relation):
        self._real_equations.add_nonzero(relation)
        self._mod_360_equations.add_nonzero(relation)

    def add_bool_nonzero(self, relation):
        self._bool_equations.add_nonzero(relation)

    def clone(self) -> 'LinearAlgebraTracker':
        """
        Returns a deep copy of the linear algebra tracker.
        """
        res = LinearAlgebraTracker()
        res._real_equations = self._real_equations.clone()
        res._mod_360_equations = self._mod_360_equations.clone()
        res._bool_equations = self._bool_equations.clone()
        return res
