"""
This is a test file that should be run using PyTest.
It should absolutely never be imported.
"""

from pathlib import Path
import pytest
from contextlib import nullcontext

from .proof.document.geometry_document import GeometryDocument
from .proof.document.reader.document_reader import DocumentReader

from .embeddings.embedder.embedder import DiagramEmbedder
from .embeddings.embedded_predicate_value import EmbeddedPredicateValue

from .pred_config import load_constructions_and_macros

from .test_proofs import GEVA_PROBLEM_NAMES, FIGURES_PROBLEM_NAMES, IMO_SHORTLIST_PROBLEMS


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
def test_linear_problem_embedding(problem_id: str):
    '''
    Tests that the DiagramEmbedder can figure out in what order
    objects need to be built, in order to create an embedding.
    '''
    if problem_id in RANDOM_SAMPLE_PARTIALLY_INCORRECT_PROBLEMS:
        pytest.skip()

    expecting_failure = problem_id in RANDOM_SAMPLE_INCORRECT_PROBLEMS

    with pytest.raises(AssertionError) if expecting_failure else nullcontext():
        problem_name = Path('linear') / 'random_sample' / f'{problem_id}.jl'
        assert_problem_embedding_possible(problem_name)


@pytest.mark.parametrize(
    "problem_name",
    GEVA_PROBLEM_NAMES + FIGURES_PROBLEM_NAMES + IMO_SHORTLIST_PROBLEMS,
)
def test_difficult_problem_embedding(problem_name: str):
    assert_problem_embedding_possible(problem_name)


def assert_problem_embedding_possible(problem_name: str):
    document = GeometryDocument.open(problem_name)
    problem = DocumentReader().read(document, read_proof_body=False)
    diagram_embedder = DiagramEmbedder()

    embedding = diagram_embedder.embed(problem)
    assert embedding is not None

    for target_predicate in problem.statement.target_predicates:
        assert embedding.evaluate_predicate(target_predicate) == EmbeddedPredicateValue.Correct
