import pytest
from fractions import Fraction

from .linear_algebra.matrix import Matrix
from .linear_algebra.vectors.augmented_vector import AugmentedVector
from .linear_algebra.vectors.sparse_vector import SparseVector


@pytest.fixture
def sample_matrix() -> Matrix[SparseVector]:
    """
    Build a tiny matrix with 5 columns (objects) and two relations:
        1.  e0 - e1 = 0
        2.  2 * e2 + e3 - e4 = 0
        3.  e0 + e1 - e2 - e3 = 0
    """
    matrix = Matrix(SparseVector, row_length=5)

    vectors = [
        SparseVector({0: 1, 1: -1}, length=matrix.row_length),
        SparseVector({2: 2, 3: 1, 4: -1}, length=matrix.row_length),
        SparseVector({0: 1, 1: 1, 2: -1, 3: -1}, matrix.row_length)
    ]
    
    for vector in vectors:
        row = AugmentedVector(vector, Fraction(0))
        matrix.add_row(row)
    return matrix


@pytest.mark.parametrize('coefficients', [
    [1, -1],
    [2, 1, -1],
    [1, 1, -1, -1]
])
def test_get_sparse_integer_linear_combinations(sample_matrix: Matrix[SparseVector], coefficients: list[int]):
    results = sample_matrix.get_sparse_integer_linear_combinations(coefficients)
    
    vector_sum = SparseVector.create_empty(sample_matrix.row_length)
    
    for result in results:
        for coefficient, index in zip(coefficients, result):
            vector_sum += SparseVector.create_single(index, sample_matrix.row_length) * Fraction(coefficient)
        projection = sample_matrix.project_to_orthogonal_complement(AugmentedVector(vector_sum, Fraction(0))).vector
        assert projection.first_nonzero_index() is None
