from ...geometry_trackers.congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker

from ...predicates.predicate import Predicate

from .congruence_closure_problem import CongruenceClosureProblem


_GEOMETRY_CONGRUENCE_PROBLEMS: list[tuple[list[Predicate], list[Predicate]]] = [
    (
        [],
        []
    )
]

GEOMETRY_CONGRUENCE_PROBLEMS = [CongruenceClosureProblem(CongruenceClosureTracker, problem[0], problem[1]) for problem in _GEOMETRY_CONGRUENCE_PROBLEMS]
