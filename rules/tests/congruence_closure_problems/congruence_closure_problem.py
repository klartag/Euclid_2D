from dataclasses import dataclass

from ...geometry_trackers.congruence_closure_tracker.abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker


@dataclass
class CongruenceClosureProblem[Atom, NonAtom, Function, Predicate]:
    '''
    TODO: Document
    '''
    tracker_class: type[AbstractCongruenceClosureTracker[Atom, NonAtom, Function, Predicate]]
    input_predicates: list[Predicate]
    output_predicates: list[Predicate]

    def check(self) -> bool:
        tracker = self.initialize_tracker()
        for predicate in self.output_predicates:
            left, right = tracker.deconstruct_predicate(predicate)
            if not tracker.are_congruent(left, right):
                return False
        return True


    def initialize_tracker(self) -> AbstractCongruenceClosureTracker[Atom, NonAtom, Function, Predicate]:
        congruence_closure_tracker = self.tracker_class()
        for predicate in self.input_predicates:
            congruence_closure_tracker.merge(predicate)
        return congruence_closure_tracker
