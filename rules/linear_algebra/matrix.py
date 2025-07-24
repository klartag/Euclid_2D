from numbers import Rational
from typing import Dict, List, TypeVar, Generic

from .vectors.abstract_vector import AbstractVector
from .vectors.sparse_vector import SparseVector
from .vectors.augmented_vector import AugmentedVector

A = TypeVar('A', bound=AbstractVector)
C = TypeVar('C')


class Matrix(Generic[A, C]):
    diagonal_indices: List[int]
    rows: List[AugmentedVector[A, C]]
    row_length: int

    def __init__(self, row_length: int):
        self.diagonal_indices = []
        self.rows = []
        self.constants = []
        self.row_length = row_length

    def extend_row_length(self, amount: int):
        for row in self.rows:
            row.extend_length(amount)
        row_length += amount

    def permute_columns(self, permutation: list[int]):
        self.rows = [row.permute(permutation) for row in self.rows]

    def project_to_orthogonal_complement(self, vector: AugmentedVector[A, C]) -> AugmentedVector[A, C]:
        for i in range(len(self.rows)):
            if vector[self.diagonal_indices[i]] != 0:
                vector -= self.rows[i] * vector[self.diagonal_indices[i]]
        return vector

    def in_span(self, row: AugmentedVector[A, C]):
        projected_row = self.project_to_orthogonal_complement(row)
        return projected_row.first_nonzero_index() is None and not projected_row.constant

    def add_row(self, row: AugmentedVector[A, C]):
        row = self.project_to_orthogonal_complement(row)

        if not row.vector and row.constant:
            raise ValueError("Adding a row caused a contradiction in the augmented matrix.")

        first_nonzero_index = row.first_nonzero_index()
        if first_nonzero_index is None:
            return

        row /= row[first_nonzero_index]
        for i in range(len(self.rows)):
            if self.rows[i][first_nonzero_index] != 0:
                self.rows[i] -= row * self.rows[i][first_nonzero_index]

        row_index = 0
        while row_index < len(self.rows) and self.diagonal_indices[row_index] < first_nonzero_index:
            row_index += 1

        self.diagonal_indices.insert(row_index, first_nonzero_index)
        self.rows.insert(row_index, row)

    def get_sparse_integer_linear_combinations(
        self, max_coefficient_count: int, max_coefficient_sum: int
    ) -> List[Dict[int, Rational]]:
        combinations: List[AugmentedVector[A, C]] = []
        for row_index in range(len(self.rows)):
            diagonal_index_start = self.diagonal_indices[row_index]
            diagonal_index_end = (
                self.diagonal_indices[row_index + 1] if row_index < len(self.rows) - 1 else self.row_length
            )
            new_combinations: List[AugmentedVector[A, C]] = []

            row = self.rows[row_index]
            # `row *= gcd([x.denominator for x in row[:diagonal_index_bound]])` # So that we end up with an *integer* combination.
            if row.count_nonzero_indices(diagonal_index_end) <= max_coefficient_count:
                for i in range(max_coefficient_sum // row.taxicab_norm(diagonal_index_end)):
                    new_combinations.append(row * (i + 1))
            for old_combination in combinations:
                old_combination -= row * old_combination[diagonal_index_start]
                for i in range(-max_coefficient_sum, max_coefficient_sum + 1):
                    potential_new_combination = old_combination + row * i
                    if (
                        potential_new_combination.count_nonzero_indices(diagonal_index_end) <= max_coefficient_count
                        and potential_new_combination.taxicab_norm(diagonal_index_end) <= max_coefficient_sum
                    ):
                        new_combinations.append(potential_new_combination)
            combinations = new_combinations
            print(len(combinations))

        combinations = [
            combination
            for combination in combinations
            if combination.vector.count_nonzero_indices() <= max_coefficient_count
            and combination.vector.taxicab_norm() <= max_coefficient_sum
        ]
        return combinations

    def __str__(self) -> str:
        nonzero_keys = [i for i in range(self.row_length) if any([row[i] != 0 for row in self.rows])]
        if len(nonzero_keys) == 0:
            return ''
        table = [nonzero_keys] + [[row[i] or '' for i in nonzero_keys] for row in self.rows]
        table_repr = [[str(cell) for cell in row] for row in table]
        column_lengths = [max([len(str(row[i])) for row in table]) for i in range(len(nonzero_keys))]
        padded_table_reprs = [
            [f'{cell:>{column_lengths[column_index] + 4}}' for (column_index, cell) in enumerate(row)]
            for row in table_repr
        ]
        table_row_reprs = [''.join(row) for row in padded_table_reprs]
        table_row_reprs.insert(1, '-' * len(table_row_reprs[0]))
        return '\n'.join(table_row_reprs)

    def __repr__(self) -> str:
        return f'Matrix[{', '.join([str(row) for row in self.rows])}]'
