from fractions import Fraction
from typing import List, Optional, TypeVar, Generic

from .vectors.abstract_iterable_vector import AbstractIterableVector
from .vectors.constant_vector import ConstantVector
from .vectors.augmented_vectors.augmented_vector_2 import AugmentedVector2
from .vectors.augmented_vectors.augmented_vector_3 import AugmentedVector3

V = TypeVar('V', bound=AbstractIterableVector)

class Matrix(Generic[V]):
    _class: type[V]
    diagonal_indices: List[int]
    rows: List[AugmentedVector3[V, ConstantVector, V]]
    row_length: int

    def __init__(self, inner_class: type[V], row_length: int):
        self._class = inner_class
        self.diagonal_indices = []
        self.rows = []
        self.row_length = row_length

    def extend_row_length(self, amount: int):
        for row in self.rows:
            row.inner0.extend_length(amount)
        self.row_length += amount

    def project_to_orthogonal_complement(self, vector: AugmentedVector2[V, ConstantVector]) -> AugmentedVector3[V, ConstantVector, V]:
        extended_vector: AugmentedVector3[V, ConstantVector, V] = AugmentedVector3(vector.inner0, vector.inner1, self._class.zero(len(self.rows)))
        for i in range(len(self.rows)):
            if vector.inner0[self.diagonal_indices[i]] != 0:
                extended_vector -= self.rows[i] * vector.inner0[self.diagonal_indices[i]]
        return extended_vector

    def in_span(self, row: AugmentedVector2[V, ConstantVector]):
        projected_row = self.project_to_orthogonal_complement(row)
        return projected_row.inner0.first_nonzero_index() is None and not projected_row.inner1

    def add_row(self, row: AugmentedVector2[V, ConstantVector]) -> Optional[int]:
        projected_row = self.project_to_orthogonal_complement(row)

        if not projected_row.inner0 and projected_row.inner1:
            raise ValueError("Adding a row caused a contradiction in the augmented matrix.")

        first_nonzero_index = projected_row.inner0.first_nonzero_index()
        if first_nonzero_index is None:
            return None
        
        for matrix_row in self.rows:
            matrix_row.inner2.extend_length(1)
        projected_row.inner2.extend_length(1)
        projected_row.inner2[len(projected_row.inner2) - 1] = Fraction(1)

        projected_row /= projected_row.inner0[first_nonzero_index]
        for i in range(len(self.rows)):
            if self.rows[i].inner0[first_nonzero_index] != 0:
                self.rows[i] -= projected_row * self.rows[i].inner0[first_nonzero_index]

        row_index = 0
        while row_index < len(self.rows) and self.diagonal_indices[row_index] < first_nonzero_index:
            row_index += 1

        self.diagonal_indices.insert(row_index, first_nonzero_index)
        self.rows.insert(row_index, projected_row)
        return len(self.rows) - 1

    def get_sparse_integer_linear_combinations(
        self, max_coefficient_count: int, max_coefficient_sum: int
    ) -> List[AugmentedVector2[V, ConstantVector]]:
        combinations: List[AugmentedVector2[V, ConstantVector]] = []
        for row_index in range(len(self.rows)):
            diagonal_index_start = self.diagonal_indices[row_index]
            diagonal_index_end = (
                self.diagonal_indices[row_index + 1] if row_index < len(self.rows) - 1 else self.row_length
            )
            new_combinations: List[AugmentedVector2[V, ConstantVector]] = []

            row = AugmentedVector2(self.rows[row_index].inner0, self.rows[row_index].inner1)
            if row.inner0.count_nonzero_indices(diagonal_index_end) <= max_coefficient_count:
                for i in range(max_coefficient_sum // row.inner0.taxicab_norm(diagonal_index_end)):
                    new_combinations.append(row * Fraction(i + 1))
            for old_combination in combinations:
                old_combination -= row * old_combination.inner0[diagonal_index_start]
                for i in range(-max_coefficient_sum, max_coefficient_sum + 1):
                    potential_new_combination = old_combination + row * Fraction(i)
                    if (
                        potential_new_combination.inner0.count_nonzero_indices(diagonal_index_end) <= max_coefficient_count
                        and potential_new_combination.inner0.taxicab_norm(diagonal_index_end) <= max_coefficient_sum
                    ):
                        new_combinations.append(potential_new_combination)
            combinations = new_combinations

        combinations = [
            combination
            for combination in combinations
            if combination.inner0.count_nonzero_indices() <= max_coefficient_count
            and combination.inner0.taxicab_norm() <= max_coefficient_sum
        ]
        return combinations

    def __str__(self) -> str:
        nonzero_keys = [i for i in range(self.row_length) if any([row.inner0[i] != 0 for row in self.rows])]
        if len(nonzero_keys) == 0:
            return ''
        table = [nonzero_keys + ['.']] + [[row.inner0[i] or '' for i in nonzero_keys] + [row.inner1.inner] for row in self.rows]
        table_repr = [[str(cell) for cell in row] for row in table]
        column_lengths = [max([len(row[i]) for row in table_repr]) for i in range(len(table_repr[0]))]
        padded_table_reprs = [
            [f'{cell:>{column_lengths[column_index] + 4}}' for (column_index, cell) in enumerate(row)]
            for row in table_repr
        ]
        table_row_reprs = [''.join(row) for row in padded_table_reprs]
        table_row_reprs.insert(1, '-' * len(table_row_reprs[0]))
        return '\n'.join(table_row_reprs)

    def clone(self) -> 'Matrix[V]':
        cloned_matrix = Matrix(self._class, self.row_length)
        cloned_matrix.diagonal_indices = self.diagonal_indices[:]
        cloned_matrix.rows = self.rows[:]
        return cloned_matrix

    def __repr__(self) -> str:
        return f'Matrix[{', '.join([str(row) for row in self.rows])}]'
