from ...geometry_trackers.congruence_closure_tracker.text_congruence_closure_tracker import TextCongruenceClosureTracker

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

TEXT_CONGRUENCE_PROBLEMS = [CongruenceClosureProblem(TextCongruenceClosureTracker, problem[0], problem[1]) for problem in _TEXT_CONGRUENCE_PROBLEMS]
