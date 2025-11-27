from typing import NamedTuple
import pytest

from ..predicates.predicate import Predicate
from ..geometry_objects.geo_object import GeoObject

from ..geometry_trackers.congruence_closure_tracker.text_congruence_closure_tracker import TextCongruenceClosureTracker
from ..geometry_trackers.congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker


TextCongruenceProblem = NamedTuple('TextCongruenceProblem', [('input', list[str]), ('output', list[str])])
GeometryCongruenceProblem = NamedTuple('TextCongruenceProblem', [('input', list[Predicate]), ('output', list[Predicate])])


TEXT_CONGRUENCE_PROBLEMS: list[TextCongruenceProblem] = [
    TextCongruenceProblem(
        ['b = d', 'f(b) = d', 'f(d) = a'],
        ['a = b', 'f(f(f(f(f(f(f(f(f(f(b)))))))))) = f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(d))))))))))))))))))))']
    ),
    TextCongruenceProblem(    
        ['1 = 8', '7 = 2', '3 = 13', '7 = 1', '6 = 7', '9 = 5', '9 = 3', '14 = 11', '10 = 4', '12 = 9', '4 = 11', '10 = 7'],
        ['1 = 4']  
    ),
    TextCongruenceProblem(
        ['f(g, h) = d', 'c = d', 'f(g, d) = a', 'e = c', 'e = b', 'b = h'],
        ['a = b', 'f(g, f(g, f(g, f(g, f(g, h))))) = c']
    ),
    TextCongruenceProblem(
        ['a = b1', 'b1 = b2', 'b2 = b3', 'b3 = c'],
        ['a = c']
    ),
    TextCongruenceProblem(
        ['f(a1, a1) = a', 'f(c1, c1) = c', 'a1 = c1'],
        ['a = c', 'f(a1, c1) = f(c1, a1)']
    ),
    TextCongruenceProblem(
        ['a = b1', 'b1 = b2', 'b2 = b3', 'b3 = c', 'f(a1, a1) = a', 'f(c1, c1) = c', 'a1 = c1'],
        ['a = c', 'f(a1, c1) = f(c1, a1)']
    )
]

GEOMETRY_CONGRUENCE_PROBLEMS: list[GeometryCongruenceProblem] = []


@pytest.mark.parametrize('problem', TEXT_CONGRUENCE_PROBLEMS)
def test_text_congruence_closure_tracker(problem: TextCongruenceProblem):
    congruence_closure_tracker = TextCongruenceClosureTracker()
    
    for congruence in problem.input:
        congruence_closure_tracker.merge(congruence)
        
    for congruence in problem.output:
        left, right = congruence_closure_tracker.deconstruct_predicate(congruence)
        assert congruence_closure_tracker.are_congruent(left, right)


@pytest.mark.parametrize('problem', GEOMETRY_CONGRUENCE_PROBLEMS)
def test_geometry_congruence_closure_tracker(problem: GeometryCongruenceProblem):
    congruence_closure_tracker = CongruenceClosureTracker()
    
    for congruence in problem.input:
        congruence_closure_tracker.merge(congruence)
        
    for congruence in problem.output:
        left, right = congruence_closure_tracker.deconstruct_predicate(congruence)
        assert congruence_closure_tracker.are_congruent(left, right)

@pytest.mark.parametrize('problem', TEXT_CONGRUENCE_PROBLEMS)
def test_text_congruence_closure_explaining(problem: TextCongruenceProblem):
    congruence_closure_tracker = TextCongruenceClosureTracker()
    
    for congruence in problem.input:
        congruence_closure_tracker.merge(congruence)
        
    for congruence in problem.output:
        left, right = congruence_closure_tracker.deconstruct_predicate(congruence)
        explanation = congruence_closure_tracker.explain(left, right)
        
        checker = TextCongruenceClosureTracker()
        for explanation_predicate in explanation:
            assert explanation_predicate in problem.input
            checker.merge(explanation_predicate)
        
        assert checker.are_congruent(left, right)
        
        for i in range(len(explanation)):
            smaller_explanation = explanation[:]
            del smaller_explanation[i]
            
            checker = TextCongruenceClosureTracker()
            for explanation_predicate in smaller_explanation:
                checker.merge(explanation_predicate)
            
            assert not checker.are_congruent(left, right)
