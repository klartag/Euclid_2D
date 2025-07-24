from ..geometry_objects.geo_object import GeoObject
from ..geometry_objects.literal import ONE

from ..proof_checker_utils import get_eqn_key
from ..rust_code.rust_sparse_linear import BaseSolver, BoolLinearSolver, ModLinearSolver, RLinearSolver


class OldLinearAlgebraTracker:
    """
    A class that checks that a proof is valid.
    """

    """An object tracking linear equations in R."""
    real_equations: RLinearSolver[GeoObject]
    """An object tracking linear equations in Z/360."""
    mod_360_equations: ModLinearSolver[GeoObject]
    """An object tracking linear equations over the booleans."""
    bool_equations: BoolLinearSolver[GeoObject]

    def __init__(self):
        one_key = get_eqn_key(ONE)
        self.real_equations = RLinearSolver(one_key)

        self.mod_360_equations = ModLinearSolver(one_key)
        self.mod_360_equations.add_relation({ONE: 360})

        self.bool_equations = BoolLinearSolver(one_key)
        self.bool_equations.add_objects([ONE])

    def trackers(self) -> list[BaseSolver]:
        """
        Returns the list of trackers of the proof checker.
        """
        return [self.bool_equations, self.mod_360_equations, self.real_equations]

    def clone(self) -> 'OldLinearAlgebraTracker':
        """
        Returns a deep copy of the linear algebra tracker.
        """
        res = OldLinearAlgebraTracker()
        res.real_equations = self.real_equations.clone()
        res.mod_360_equations = self.mod_360_equations.clone()
        res.bool_equations = self.bool_equations.clone()
        return res
