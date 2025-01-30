"""
This is a test file that should be run using PyTest.
It should absolutely never be imported.
"""

import pytest

from .pred_config import load_constructions_and_macros

from .predicates.global_predicates import get_constructions

from .geometry_objects.parse import parse_geo_object

from .geometry_objects.construction_object import Construction, ConstructionObject
from .geometry_objects.geo_object import GeoObject
from .rule_utils import POINT, SCALAR
from .proof import Proof
from .proof_checker import ProofChecker, check_proof
from .proof_gen.proof_generator import prove
from util import BASE_PATH


@pytest.fixture(autouse=True)
def load_constructions_and_macros_for_tests():
    load_constructions_and_macros()


@pytest.mark.parametrize(
    "problem_name",
    [
        # Problems from Yoel Geva
        'geva/p288_1.jl',
        'geva/p292_4.jl',
        'geva/p301_8.jl',
        # Problems from the Geometry in Figures book
        # Chapter 1
        'figures/1_1.jl',
        'figures/1_3.jl',
        'figures/1_4.jl',
        'figures/1_5.jl',
        'figures/1_6.jl',
        'figures/1_7.jl',
        'figures/1_8.jl',
        'figures/1_9.jl',
        'figures/1_10.jl',
        'figures/1_11.jl',
        'figures/1_12.jl',
        'figures/1_13.jl',
        'figures/1_15.jl',
        'figures/1_16.jl',
        'figures/1_17.jl',
        'figures/1_18.jl',
        'figures/1_19.jl',
        'figures/1_20.jl',
        'figures/1_21.jl',
        'figures/1_22.jl',
        'figures/1_23.jl',
        'figures/1_24.jl',
        # Chapter 3
        'figures/3_12.jl',
        'figures/3_13.jl',
        # Chapter 4
        'figures/4_1_1.jl',
        'figures/4_3_4.jl',
        'figures/4_6_1.jl',
        # Problems from the IMO 2021 Shortlist
        'IMO/2021/G1.jl',
        'IMO/2021/G2.jl',
        'IMO/2021/G4.jl',
        # Problems from the IMO 2022 Shortlist
        'IMO/2022/G1.jl',
        'IMO/2022/G2.jl',
        'IMO/2022/G3.jl',
        'IMO/2022/G4.jl',
        'IMO/2022/G5.jl',
    ],
)
def test_check_proof(problem_name: str):
    '''
    Tests that the Proof Checker works on a geometry problem.
    '''
    if problem_name.startswith('IMO'):
        pytest.skip('Currently disabling proof checking of all IMO problems.')

    problem_path = BASE_PATH / 'rules' / 'proof_samples' / problem_name
    check_proof(problem_path)


@pytest.mark.parametrize(
    "problem_name",
    [
        # Problems from Yoel Geva
        'geva/p288_1.jl',
        'geva/p292_4.jl',
        'geva/p301_8.jl',
        # Problems from the Geometry in Figures book
        'figures/1_1.jl',
        'figures/1_3.jl',
        'figures/1_4.jl',
        'figures/1_5.jl',
        'figures/1_6.jl',
        'figures/1_7.jl',
    ],
)
def test_proof_generator(problem_name: str):
    '''
    Tests that the Proof Generator works on a geometry problem.
    '''
    problem_path = BASE_PATH / 'rules' / 'proof_samples' / problem_name
    proof_assumptions = Proof.parse(problem_path.open().read())
    proof = prove(proof_assumptions, interactive=False)
    checker = ProofChecker(proof)
    checker.check()


def test_proof_shuffle():
    '''
    Tests that shuffling the names of objects in a proof
    does not make the proof invalid.
    (Specifically, testing this on problem 1.1 from the Geometry in Figures book)
    '''
    proof = Proof.parse((BASE_PATH / 'rules/proof_samples/figures/1_1.jl').open().read())
    shuffled = proof.shuffled()
    checker = ProofChecker(shuffled)
    checker.check()


def validate_constructions():
    bad_constructions = set()
    for con in get_constructions().values():
        for pred in con.result_predicates:
            if con.res not in pred.involved_objects():
                bad_constructions.add(con)
        for _, res in con.possible_conclusions:
            for pred in res:
                if con.res not in pred.involved_objects():
                    bad_constructions.add(con)

    assert len(bad_constructions) == 0, f'Constructions with non-trivial side-effects exist: {bad_constructions}'


def test_parsing():
    objects = {
        'A': GeoObject('A', POINT),
        'B': GeoObject('B', POINT),
        'C': GeoObject('C', POINT),
        'r': GeoObject('r', SCALAR),
        's': GeoObject('s', SCALAR),
    }
    p = parse_geo_object('2*(r) * s', objects)
    ConstructionObject.from_args('log', (p,))

    parse_geo_object('2*(r+s) + s/1.5', objects)
    parse_geo_object('-r', objects)
