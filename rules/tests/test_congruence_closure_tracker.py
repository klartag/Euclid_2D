from typing import NamedTuple
import pytest

from ..predicates.predicate import Predicate
from ..geometry_objects.geo_object import GeoObject

from ..geometry_trackers.congruence_closure_tracker.abstract_congruence_closure_tracker import AbstractCongruenceClosureTracker
from ..geometry_trackers.congruence_closure_tracker.text_congruence_closure_tracker import TextCongruenceClosureTracker
from ..geometry_trackers.congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker

from .congruence_closure_problem import CongruenceClosureProblem


_TEXT_CONGRUENCE_PROBLEMS: list[tuple[list[str], list[str]]] = [
    (
        ['b = d', 'f(b) = d', 'f(d) = a'],
        ['a = b', 'f(f(f(f(f(f(f(f(f(f(b)))))))))) = f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(d))))))))))))))))))))']
    ),
    (    
        ['1 = 8', '7 = 2', '3 = 13', '7 = 1', '6 = 7', '9 = 5', '9 = 3', '14 = 11', '10 = 4', '12 = 9', '4 = 11', '10 = 7'],
        ['1 = 4']  
    ),
    (
        ['f(g, h) = d', 'c = d', 'f(g, d) = a', 'e = c', 'e = b', 'b = h'],
        ['a = b', 'f(g, f(g, f(g, f(g, f(g, h))))) = c']
    ),
    (
        ['a = b1', 'b1 = b2', 'b2 = b3', 'b3 = c'],
        ['a = c']
    ),
    (
        ['f(a1, a1) = a', 'f(c1, c1) = c', 'a1 = c1'],
        ['a = c', 'f(a1, c1) = f(c1, a1)']
    ),
    (
        ['a = b1', 'b1 = b2', 'b2 = b3', 'b3 = c', 'f(a1, a1) = a', 'f(c1, c1) = c', 'a1 = c1'],
        ['a = c', 'f(a1, c1) = f(c1, a1)']
    )
]

_GEOMETRY_CONGRUENCE_PROBLEMS: list[tuple[list[Predicate], list[Predicate]]] = []

TEXT_CONGRUENCE_PROBLEMS = [CongruenceClosureProblem(TextCongruenceClosureTracker, problem[0], problem[1]) for problem in _TEXT_CONGRUENCE_PROBLEMS]
GEOMETRY_CONGRUENCE_PROBLEMS = [CongruenceClosureProblem(CongruenceClosureTracker, problem[0], problem[1]) for problem in _GEOMETRY_CONGRUENCE_PROBLEMS]

CONGRUENCE_CLOSURE_PROBLEMS = TEXT_CONGRUENCE_PROBLEMS + GEOMETRY_CONGRUENCE_PROBLEMS

@pytest.mark.parametrize('problem', CONGRUENCE_CLOSURE_PROBLEMS)
def test_congruence_closure_tracker(problem: CongruenceClosureProblem):
    '''
    TODO: DOCUMENT
    '''
    congruence_closure_tracker = tracker_from_predicates(problem.tracker_class, problem.input_predicates)

    for congruence in problem.output_predicates:
        left, right = congruence_closure_tracker.deconstruct_predicate(congruence)
        assert congruence_closure_tracker.are_congruent(left, right)


@pytest.mark.parametrize('problem', CONGRUENCE_CLOSURE_PROBLEMS)
def test_congruence_closure_explanation(problem: CongruenceClosureProblem):
    '''
    TODO: Document
    '''
    congruence_closure_tracker = tracker_from_predicates(problem.tracker_class, problem.input_predicates)

    for congruence in problem.output_predicates:
        left, right = congruence_closure_tracker.deconstruct_predicate(congruence)
        explanation = congruence_closure_tracker.explain(left, right)
        
        checker = tracker_from_predicates(problem.tracker_class, explanation)
        assert checker.are_congruent(left, right)


@pytest.mark.parametrize('problem', CONGRUENCE_CLOSURE_PROBLEMS)
def test_congruence_closure_explanation_minimality(problem: CongruenceClosureProblem):
    '''
    TODO: Document
    '''
    congruence_closure_tracker = tracker_from_predicates(problem.tracker_class, problem.input_predicates)

    for congruence in problem.output_predicates:
        left, right = congruence_closure_tracker.deconstruct_predicate(congruence)
        explanation = congruence_closure_tracker.explain(left, right)
        
        for i in range(len(explanation)):
            smaller_explanation = explanation[:]
            del smaller_explanation[i]

            checker = tracker_from_predicates(problem.tracker_class, smaller_explanation)
            assert not checker.are_congruent(left, right)


def tracker_from_predicates[Atom, NonAtom, Predicate](
    congruence_closure_tracker_class: type[AbstractCongruenceClosureTracker[Atom, NonAtom, Predicate]],
    predicates: list[Predicate]
) -> AbstractCongruenceClosureTracker[Atom, NonAtom, Predicate]:
    congruence_closure_tracker = congruence_closure_tracker_class()
    for predicate in predicates:
        congruence_closure_tracker.merge(predicate)
    return congruence_closure_tracker
