import pytest

from ..geometry_objects.geo_object import GeoObject

from ..geometry_trackers.congruence_closure_tracker.text_congruence_closure_tracker import TextCongruenceClosureTracker
from ..geometry_trackers.congruence_closure_tracker.congruence_closure_tracker import CongruenceClosureTracker


@pytest.mark.parametrize(['input_congruences', 'output_congruences'],
    [
        (
            [('b', 'd'), ('f(b)', 'd'), ('f(d)', 'a')],
            [('a', 'b'), ('f(f(f(f(f(f(f(f(f(f(b))))))))))', 'f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(d))))))))))))))))))))')]
        ),
        (    
            [('1', '8'), ('7', '2'), ('3', '13'), ('7', '1'), ('6', '7'), ('9', '5'), ('9', '3'), ('14', '11'), ('10', '4'), ('12', '9'), ('4', '11'), ('10', '7')],
            [('1', '4')]  
        ),
        (
            [('f(g, h)', 'd'), ('c', 'd'), ('f(g, d)', 'a'), ('e', 'c'), ('e', 'b'), ('b', 'h')],
            [('a', 'b'), ('f(g, f(g, f(g, f(g, f(g, h)))))', 'c')]
        ),
        (
            [('a', 'b1'), ('b1', 'b2'), ('b2', 'b3'), ('b3', 'c')],
            [('a', 'c')]
        ),
        (
            [('f(a1, a1)', 'a'), ('f(c1, c1)', 'c'), ('a1', 'c1')],
            [('a', 'c'), ('f(a1, c1)', 'f(c1, a1)')]
        ),
        (
            [('a', 'b1'), ('b1', 'b2'), ('b2', 'b3'), ('b3', 'c'), ('f(a1, a1)', 'a'), ('f(c1, c1)', 'c'), ('a1', 'c1')],
            [('a', 'c'), ('f(a1, c1)', 'f(c1, a1)')]
        )
    ]
)
def test_text_congruence_closure_tracker(input_congruences: list[tuple[str, str]], output_congruences: list[tuple[str, str]]):
    congruence_closure_tracker = TextCongruenceClosureTracker()
    
    for input_congruence in input_congruences:
        congruence_closure_tracker.merge(input_congruence[0], input_congruence[1])
        
    for output_congruence in output_congruences:
        assert congruence_closure_tracker.are_congruent(output_congruence[0], output_congruence[1])


@pytest.mark.parametrize(['input_congruences', 'output_congruences'],
    [
    ]
)
def test_geometry_congruence_closure_tracker(input_congruences: list[tuple[GeoObject, GeoObject]], output_congruences: list[tuple[GeoObject, GeoObject]]):
    congruence_closure_tracker = CongruenceClosureTracker()
    
    for input_congruence in input_congruences:
        congruence_closure_tracker.merge(input_congruence[0], input_congruence[1])
        
    for output_congruence in output_congruences:
        assert congruence_closure_tracker.are_congruent(output_congruence[0], output_congruence[1])
