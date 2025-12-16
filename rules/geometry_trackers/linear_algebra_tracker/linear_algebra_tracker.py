from typing import Dict, List, Optional, Self, Tuple, TypeVar
from fractions import Fraction

from ...indexed_set import IndexedSet

from ...permutations import try_match_permutation

from ...predicates.predicate import Predicate

from ...embeddings.embedding import Embedding
from ...embeddings.embedded_objects.scalar import EmbeddedScalar

from ...geometry_objects.literal import ONE, Literal
from ...geometry_objects.construction_object import ConstructionObject
from ...geometry_objects.equation_object import EquationObject
from ...geometry_objects.geo_object import GeoObject

from ...linear_algebra.matrix import Matrix
from ...linear_algebra.vectors.augmented_vectors.augmented_vector_2 import AugmentedVector2
from ...linear_algebra.vectors.sparse_vector import SparseVector
from ...linear_algebra.vectors.constant_vector import ConstantVector

from .linear_expression import LinearExpression

class LinearAlgebraTracker:
    matrix: Matrix[SparseVector]

    keys: IndexedSet[GeoObject]
    predicates: list[Predicate]

    def __init__(self):
        self.matrix = Matrix(SparseVector, 0)
        self.keys = IndexedSet()
        self._add_key(ONE)
        self.predicates = []

    def _add_key(self, key: GeoObject):
        self.keys.add(key)
        self.matrix.extend_row_length(1)

    def add_relation(self, linear_expression: LinearExpression, value: int | Fraction, embedding: Embedding, predicate: Optional[Predicate]):
        '''
        TODO: The `embedding` parameter is not required,
        but we will keep it here *for now* because it allows us to raise an error whenever we add an incorrect relation.
        '''
        value = Fraction(value)

        for geo_object in linear_expression.inner.keys():
            if geo_object not in self.keys:
                self._add_key(geo_object)

        (linear_expression, automatic_residue) = self.evaluate_automatic_part_of_expression(
            linear_expression, embedding
        )

        linear_expression_object = linear_expression.to_equation_object()

        scalars = embedding.evaluate_object(linear_expression_object)
        if len(scalars) != 1:
            raise ValueError("Failed to embed the linear expression.")
        scalar = scalars[0]
        if not isinstance(scalar, EmbeddedScalar):
            raise ValueError("Evaluated object did not end up being a scalar.")

        value -= automatic_residue
        if not scalar.is_equal(EmbeddedScalar(value)):
            raise ValueError("The` embedding does not agree with the correctness of the relation.")

        self.cached_sparse_combinations = None

        if self.matrix.add_row(
            AugmentedVector2(
                SparseVector(
                    {self.keys.index(k): v for (k, v) in linear_expression.items()}, self.matrix.row_length
                ),
                ConstantVector(value),
            )
        ) is not None and predicate is not None:
            self.predicates.append(predicate)

    def add_relation_mod(
        self, linear_expression: LinearExpression, value: int | Fraction, modulus: int, embedding: Embedding, predicate: Optional[Predicate]
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

        self.add_relation(linear_expression, value, embedding, predicate)

    def explain_relation(self, linear_expression: LinearExpression) -> List[Predicate]:
        row = SparseVector({self.keys.index(k): v for (k, v) in linear_expression.items() if v != 0 and not LinearAlgebraTracker.is_automatically_evaluated(k)}, self.matrix.row_length)
        projected_row = self.matrix.project_to_orthogonal_complement(AugmentedVector2(row, ConstantVector(Fraction(0))))
        predicate_indices = [i for i in range(len(projected_row.inner2)) if projected_row.inner2[i] != 0]
        return [self.predicates[i] for i in predicate_indices]

    def try_evaluate(self, linear_expression: LinearExpression, embedding: Embedding) -> Optional[Fraction]:
        linear_expression = LinearExpression({k: v for (k, v) in linear_expression.items() if v != 0})

        (linear_expression, automatic_residue) = self.evaluate_automatic_part_of_expression(
            linear_expression, embedding
        )

        if any([k not in self.keys for k in linear_expression]):
            return None

        row = SparseVector({self.keys.index(k): v for (k, v) in linear_expression.items()}, self.matrix.row_length)
        projected_row = self.matrix.project_to_orthogonal_complement(AugmentedVector2(row, ConstantVector(Fraction(0))))

        if projected_row.inner0.first_nonzero_index() is not None:
            return None
        return automatic_residue - projected_row.inner1.inner

    def evaluate_automatic_part_of_expression(
        self, linear_expression: LinearExpression, embedding: Embedding
    ) -> Tuple[LinearExpression, int]:
        automatic_part = LinearExpression(
            {k: v for (k, v) in linear_expression.items() if LinearAlgebraTracker.is_automatically_evaluated(k)}
        )

        residue = LinearExpression({k: v for (k, v) in linear_expression.items() if k not in automatic_part})
        scalars = embedding.evaluate_object(automatic_part.to_equation_object())
        if len(scalars) != 1:
            raise ValueError("Failed to embed the linear expression.")
        scalar = scalars[0]
        if not isinstance(scalar, EmbeddedScalar):
            raise ValueError("Embedded expression is not a scalar.")
        rounded_scalar = round(scalar.value)
        if not scalar.is_equal(EmbeddedScalar(rounded_scalar)):
            raise ValueError("Automatic expressions must be evaluated as integers.")

        return (residue, rounded_scalar)

    @staticmethod
    def is_automatically_evaluated(obj: GeoObject) -> bool:
        if isinstance(obj, Literal):
            return True
        if isinstance(obj, ConstructionObject):
            return obj.constructor.name == 'orientation'
        elif isinstance(obj, EquationObject):
            return LinearAlgebraTracker.is_automatically_evaluated(obj.left) and LinearAlgebraTracker.is_automatically_evaluated(obj.right)
        return False

    def get_sparse_integer_linear_combinations(self, factors: List[int]) -> List[List[GeoObject]]:
        matrix_combinations = self.matrix.get_sparse_integer_linear_combinations(factors)
        return [[self.keys[i] for i in combination] for combination in matrix_combinations]

    def try_match_factors(self, linear_expression: LinearExpression, factors: List[int]) -> Optional[List[GeoObject]]:
        if len(linear_expression) != len(factors):
            return None
        expression_items = list(linear_expression.items())
        expression_items.sort(key=lambda item: item[0])
        
        expression_factors = [item[1] for item in expression_items]
        
        permutation = try_match_permutation(expression_factors, [Fraction(i) for i in factors])
        if permutation is None:
            return None
        
        return [expression_items[i][0] for i in permutation]

    def clone(self) -> 'LinearAlgebraTracker':
        cloned_tracker = LinearAlgebraTracker()
        cloned_tracker.matrix = self.matrix.clone()
        cloned_tracker.keys = self.keys.clone()
        return cloned_tracker
