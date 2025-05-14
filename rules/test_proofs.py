"""
This is a test file that should be run using PyTest.
It should absolutely never be imported.
"""

import pytest

from .proof.document.geometry_document import GeometryDocument
from .proof.document.reader.document_reader import DocumentReader

from .pred_config import load_constructions_and_macros

from .predicates.global_predicates import get_constructions

from .geometry_objects.atom import Atom
from .geometry_objects.parse import parse_geo_object

from .geometry_objects.construction_object import ConstructionObject
from .rule_utils import POINT, SCALAR
from .proof_checker import ProofChecker, check_proof
from .proof_gen.proof_generator import prove


# Problems from Yoel Geva
GEVA_PROBLEM_NAMES = ['geva/p288_1.jl', 'geva/p292_4.jl', 'geva/p301_8.jl']

# Problems from the Geometry in Figures book
FIGURES_PROBLEM_NAMES = [
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
]

# Problems from IMOs
IMO_G1_PROBLEMS = [
    'IMO/2008/G1.jl',
    'IMO/2010/G1.jl',
    'IMO/2012/G1.jl',
    'IMO/2013/G1.jl',
    'IMO/2014/G1.jl',
    'IMO/2015/G1.jl',
    'IMO/2016/G1.jl',
    'IMO/2017/G1.jl',
    'IMO/2018/G1.jl',
    'IMO/2019/G1.jl',
    'IMO/2020/G1.jl',
    'IMO/2021/G1.jl',
    'IMO/2022/G1.jl',
    'IMO/2023/G1.jl',
]

IMO_G2_PROBLEMS = [
    'IMO/2006/G2.jl',
    'IMO/2007/G2.jl',
    'IMO/2008/G2.jl',
    'IMO/2008/G2_converse.jl',
    'IMO/2009/G2.jl',
    'IMO/2010/G2.jl',
    'IMO/2010/G2_converse.jl',
    'IMO/2012/G2.jl',
    'IMO/2013/G2.jl',
    'IMO/2015/G2.jl',
    'IMO/2016/G2.jl',
    'IMO/2017/G2.jl',
    'IMO/2018/G2.jl',
    'IMO/2019/G2.jl',
    'IMO/2020/G2.jl',
    'IMO/2021/G2.jl',
    'IMO/2022/G2.jl',
    'IMO/2023/G2.jl',
]

IMO_G3_PROBLEMS = [
    'IMO/2019/G3.jl',
]

IMO_SHORTLIST_PROBLEMS = IMO_G1_PROBLEMS + IMO_G2_PROBLEMS + IMO_G3_PROBLEMS


@pytest.fixture(autouse=True)
def load_constructions_and_macros_for_tests():
    load_constructions_and_macros()


@pytest.mark.parametrize(
    "problem_name",
    GEVA_PROBLEM_NAMES + FIGURES_PROBLEM_NAMES + IMO_SHORTLIST_PROBLEMS,
)
def test_check_proof(problem_name: str):
    '''
    Tests that the Proof Checker works on a geometry problem.
    '''
    if problem_name.startswith('IMO'):
        pytest.skip('Currently disabling proof checking of all IMO problems.')

    check_proof(problem_name)


@pytest.mark.parametrize(
    "problem_name",
    GEVA_PROBLEM_NAMES
    + [
        # Some problems from the Geometry in Figures book
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
    document = GeometryDocument.open(problem_name)
    problem = DocumentReader().read(document, read_proof_body=False)
    solved_problem = prove(problem, interactive=False, verbose=False)
    checker = ProofChecker(solved_problem)
    checker.check()


def test_constructions():
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
        'A': Atom('A', POINT),
        'B': Atom('B', POINT),
        'C': Atom('C', POINT),
        'r': Atom('r', SCALAR),
        's': Atom('s', SCALAR),
    }
    p = parse_geo_object('2*(r) * s', objects)
    ConstructionObject.from_args('log', (p,))

    parse_geo_object('2*(r+s) + s/1.5', objects)
    parse_geo_object('-r', objects)
