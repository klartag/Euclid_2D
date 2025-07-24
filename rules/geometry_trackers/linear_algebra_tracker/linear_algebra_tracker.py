from typing import Dict, List, Optional

from ...embeddings.embedding import Embedding
from ...embeddings.embedded_objects.scalar import EmbeddedScalar

from ...geometry_objects.equation_object import EquationObject
from ...geometry_objects.geo_object import GeoObject

from ...linear_algebra.matrix import Matrix
from ...linear_algebra.vectors.augmented_vector import AugmentedVector
from ...linear_algebra.vectors.sparse_vector import SparseVector

from .linear_expression import LinearExpression


class LinearAlgebraTracker:
    matrix: Matrix[SparseVector, float]

    _reverse_keys: Dict[GeoObject, int]
    _keys: List[GeoObject]

    def __init__(self):
        self.inner = Matrix(0)

    def add_key(self, key: GeoObject):
        self._reverse_keys[key] = len(self._keys)
        self._keys.append(key)
        self.matrix.extend_row_length(1)

    def add_relation(self, linear_expression: LinearExpression, value: float, embedding: Embedding):
        '''
        TODO: The `embedding` parameter is not required,
        but we will keep it here *for now* because it allows us to raise an error whenever we add an incorrect relation.
        '''
        linear_expression_object = linear_expression.to_equation_object()
        scalars = embedding.evaluate_object(linear_expression_object)
        if len(scalars) != 1:
            raise ValueError("Failed to embed the linear expression.")
        scalar = scalars[0]
        if not scalar.is_equal(EmbeddedScalar(value)):
            raise ValueError("The embedding does not agree with the correctness of the relation.")

        self.matrix.add_row(
            AugmentedVector(
                SparseVector({self._keys[k]: v for (k, v) in linear_expression}, self.matrix.row_length), value
            )
        )

    def add_relation_mod(self, linear_expression: LinearExpression, value: float, modulus: float, embedding: Embedding):
        linear_expression_object = linear_expression.to_equation_object()
        scalars = embedding.evaluate_object(linear_expression_object)
        if len(scalars) != 1:
            raise ValueError("Failed to embed the linear expression.")
        scalar = scalars[0]
        if not scalar.is_equal_mod(EmbeddedScalar(value), EmbeddedScalar(modulus)):
            raise ValueError("The embedding does not agree with the correctness of the relation.")

        self.add_relation(linear_expression, scalar.value)

    def try_evaluate(self, linear_expression: LinearExpression) -> Optional[float]:
        row = SparseVector({self._reverse_keys[k]: v for (k, v) in linear_expression.items()}, self.matrix.row_length)
        projected_row = self.matrix.project_to_orthogonal_complement(AugmentedVector(row, 0))

        if projected_row.first_nonzero_index() is not None:
            return None
        return -projected_row.constant

    def get_sparse_integer_linear_combinations(
        self, max_coefficient_count: int, max_coefficient_sum: int
    ) -> List[LinearExpression]:
        combinations = self.matrix.get_sparse_integer_linear_combinations(max_coefficient_count, max_coefficient_sum)
        return [{self._keys[k]: v for (k, v) in combination.items()} for combination in combinations]
