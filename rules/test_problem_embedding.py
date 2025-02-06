"""
This is a test file that should be run using PyTest.
It should absolutely never be imported.
"""

import pytest
from contextlib import nullcontext

from .embeddings.embedder.embedder import DiagramEmbedder

from .pred_config import load_constructions_and_macros
from .proof import Proof

from util import BASE_PATH


@pytest.fixture(autouse=True)
def load_constructions_and_macros_for_tests():
    load_constructions_and_macros()


RANDOM_SAMPLE_INCORRECT_PROBLEMS = [
    7,
    84,
    94,
    128,
    129,
    185,
    198,
    337,
    402,
    405,
    406,
    427,
    466,
    499,
    504,
    693,
    712,
    838,
    852,
    862,
    933,
    979,
    998,
]

UNCHECKED_INCORRECT_PROBLEMS = [
    6,
    9,
    20,
    76,
    78,
    135,
    193,
    232,
    235,
    286,
    325,
    387,
    393,
    418,
    464,
    492,
    497,
    561,
    567,
    572,
    590,
    643,
    657,
    679,
    765,
    780,
    816,
    876,
    887,
    937,
    952,
    958,
]

RANDOM_SAMPLE_INCORRECT_PROBLEMS.extend(UNCHECKED_INCORRECT_PROBLEMS)

RANDOM_SAMPLE_PARTIALLY_INCORRECT_PROBLEMS = [86, 682]
UNCHECKED_PARTIALLY_INCORRECT_PROBLEMS = [240, 270, 631, 750, 766, 838]

RANDOM_SAMPLE_PARTIALLY_INCORRECT_PROBLEMS.extend(UNCHECKED_PARTIALLY_INCORRECT_PROBLEMS)

RANDOM_SAMPLE_CORRECT_PROBLEMS = sorted(
    set(range(1000)) - set(RANDOM_SAMPLE_INCORRECT_PROBLEMS + RANDOM_SAMPLE_PARTIALLY_INCORRECT_PROBLEMS)
)


@pytest.mark.parametrize("problem_id", range(1000))
def test_problem_embedding(problem_id: str):
    '''
    Tests that the DiagramEmbedder can figure out in what order
    objects need to be built, in order to create an embedding.
    '''
    if problem_id in RANDOM_SAMPLE_PARTIALLY_INCORRECT_PROBLEMS:
        pytest.skip()

    expecting_failure = problem_id in RANDOM_SAMPLE_INCORRECT_PROBLEMS

    with pytest.raises(AssertionError) if expecting_failure else nullcontext():
        problem_path = BASE_PATH / 'rules' / 'proof_samples' / 'linear' / 'random_sample' / f'{problem_id}.jl'
        proof = Proof.parse(open(problem_path, 'r').read(), parse_proof_body=False)
        diagram_embedder = DiagramEmbedder()

        embedding = diagram_embedder.embed(proof)
        assert embedding is not None
        
        for target_predicate in proof.target_predicates:
            assert embedding.evaluate_predicate(target_predicate)
