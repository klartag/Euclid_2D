from typing import Dict, List, Optional
from fractions import Fraction

from ...embeddings.embedding import Embedding
from ...embeddings.embedded_objects.scalar import EmbeddedScalar

from ...geometry_objects.literal import ONE
from ...geometry_objects.geo_object import GeoObject

from ...linear_algebra.matrix import Matrix
from ...linear_algebra.vectors.augmented_vector import AugmentedVector
from ...linear_algebra.vectors.sparse_vector import SparseVector

from .linear_expression import LinearExpression


class LinearAlgebraTracker:
    matrix: Matrix[SparseVector]

    _keys: List[GeoObject]
    _reverse_keys: Dict[GeoObject, int]

    def __init__(self):
        self.matrix = Matrix(0)
        self._keys = []
        self._reverse_keys = {}
        self._add_key(ONE)
        self.add_relation(LinearExpression({ONE: 1}), 1)

    def _add_key(self, key: GeoObject):
        self._reverse_keys[key] = len(self._keys)
        self._keys.append(key)
        self.matrix.extend_row_length(1)

    def contains_key(self, key: GeoObject):
        return key in self._reverse_keys

    def add_relation(
        self, linear_expression: LinearExpression, value: int | Fraction, embedding: Optional[Embedding] = None
    ):
        '''
        TODO: The `embedding` parameter is not required,
        but we will keep it here *for now* because it allows us to raise an error whenever we add an incorrect relation.
        '''
        value = Fraction(value)

        for geo_object in linear_expression.inner.keys():
            if geo_object not in self._reverse_keys:
                self._add_key(geo_object)

        linear_expression_object = linear_expression.to_equation_object()

        if embedding is not None:
            scalars = embedding.evaluate_object(linear_expression_object)
            if len(scalars) != 1:
                raise ValueError("Failed to embed the linear expression.")
            scalar = scalars[0]
            if not scalar.is_equal(EmbeddedScalar(value)):
                raise ValueError("The` embedding does not agree with the correctness of the relation.")

        self.matrix.add_row(
            AugmentedVector(
                SparseVector(
                    {self._reverse_keys[k]: v for (k, v) in linear_expression.items()}, self.matrix.row_length
                ),
                value,
            )
        )

    def add_relation_mod(
        self, linear_expression: LinearExpression, value: int | Fraction, modulus: int, embedding: Embedding
    ):
        value = Fraction(value)

        linear_expression_object = linear_expression.to_equation_object()
        scalars = embedding.evaluate_object(linear_expression_object)
        if len(scalars) != 1:
            raise ValueError("Failed to embed the linear expression.")
        scalar = scalars[0]
        if not scalar.is_equal_mod(EmbeddedScalar(value), EmbeddedScalar(modulus)):
            raise ValueError("The embedding does not agree with the correctness of the relation.")

        value += Fraction(round((scalar.value - value) / modulus) * modulus)

        self.add_relation(linear_expression, value)

    def try_evaluate(self, linear_expression: LinearExpression) -> Optional[Fraction]:
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

    def clone(self) -> 'LinearAlgebraTracker':
        cloned_tracker = LinearAlgebraTracker()
        cloned_tracker.matrix = self.matrix.clone()
        cloned_tracker._keys = self._keys[:]
        cloned_tracker._reverse_keys = dict(self._reverse_keys)
