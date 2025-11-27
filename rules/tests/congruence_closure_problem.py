from dataclasses import dataclass

from ..geometry_trackers.congruence_closure_tracker.abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker


@dataclass
class CongruenceClosureProblem[Atom, NonAtom, Predicate]:
    tracker_class: type[AbstractCongruenceClosureTracker[Atom, NonAtom, Predicate]]
    input_predicates: list[Predicate]
    output_predicates: list[Predicate]
