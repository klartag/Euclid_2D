import pytest


from .congruence_closure_problems.congruence_closure_problem import CongruenceClosureProblem
from .congruence_closure_problems.congruence_closure_problems import CONGRUENCE_CLOSURE_PROBLEMS


@pytest.mark.parametrize('problem', CONGRUENCE_CLOSURE_PROBLEMS)
def test_congruence_closure_tracker(problem: CongruenceClosureProblem):
    '''
    TODO: DOCUMENT
    '''
    assert problem.check()


@pytest.mark.parametrize('problem', CONGRUENCE_CLOSURE_PROBLEMS)
def test_congruence_closure_explanation(problem: CongruenceClosureProblem):
    '''
    TODO: Document
    '''
    tracker = problem.initialize_tracker()
    
    for congruence in problem.output_predicates:
        left, right = tracker.deconstruct_predicate(congruence)
        explanation = tracker._explain(left, right)        
        assert CongruenceClosureProblem(problem.tracker_class, explanation, [congruence]).check(), f'Asserting that f{explanation} is an explanation of {congruence}.'


@pytest.mark.parametrize('problem', CONGRUENCE_CLOSURE_PROBLEMS)
def test_congruence_closure_explanation_minimality(problem: CongruenceClosureProblem):
    '''
    TODO: Document
    '''
    tracker = problem.initialize_tracker()

    for congruence in problem.output_predicates:
        left, right = tracker.deconstruct_predicate(congruence)
        explanation = tracker.explain(left, right)

        for i in range(len(explanation)):
            smaller_explanation = explanation[:]
            del smaller_explanation[i]
            
            assert not CongruenceClosureProblem(problem.tracker_class, smaller_explanation, [congruence]).check(), f'Asserting you cannot remove item {i} from the explanation {explanation} of {congruence}.'
