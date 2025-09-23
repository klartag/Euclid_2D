from fractions import Fraction
from typing import Dict, List, TypeVar, Generic

from .vectors.abstract_vector import AbstractVector
from .vectors.augmented_vector import AugmentedVector

A = TypeVar('A', bound=AbstractVector)


class Matrix(Generic[A]):
    diagonal_indices: List[int]
    rows: List[AugmentedVector[A, Fraction]]
    row_length: int

    def __init__(self, row_length: int):
        self.diagonal_indices = []
        self.rows = []
        self.constants = []
        self.row_length = row_length

    def extend_row_length(self, amount: int):
        for row in self.rows:
            row.extend_length(amount)
        self.row_length += amount

    def permute_columns(self, permutation: list[int]):
        self.rows = [row.permute(permutation) for row in self.rows]

    def project_to_orthogonal_complement(self, vector: AugmentedVector[A, Fraction]) -> AugmentedVector[A, Fraction]:
        for i in range(len(self.rows)):
            if vector[self.diagonal_indices[i]] != 0:
                vector -= self.rows[i] * vector[self.diagonal_indices[i]]
        return vector

    def in_span(self, row: AugmentedVector[A, Fraction]):
        projected_row = self.project_to_orthogonal_complement(row)
        return projected_row.first_nonzero_index() is None and not projected_row.constant

    def add_row(self, row: AugmentedVector[A, Fraction]):
        if not isinstance(row.constant, Fraction) or not all(
            [isinstance(row.vector[i], Fraction) for i in range(len(row.vector))]
        ):
            a = 1

        temp_row = row
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
        
    def get_sparse_integer_linear_combinations(self, factors: List[int]) -> List[List[int]]:
        # TODO: Implement
        raise NotImplementedError()

    def __str__(self) -> str:
        nonzero_keys = [i for i in range(self.row_length) if any([row[i] != 0 for row in self.rows])]
        if len(nonzero_keys) == 0:
            return ''
        table = [nonzero_keys + ['.']] + [[row[i] or '' for i in nonzero_keys] + [row.constant] for row in self.rows]
        table_repr = [[str(cell) for cell in row] for row in table]
        column_lengths = [max([len(row[i]) for row in table_repr]) for i in range(len(table_repr[0]))]
        padded_table_reprs = [
            [f'{cell:>{column_lengths[column_index] + 4}}' for (column_index, cell) in enumerate(row)]
            for row in table_repr
        ]
        table_row_reprs = [''.join(row) for row in padded_table_reprs]
        table_row_reprs.insert(1, '-' * len(table_row_reprs[0]))
        return '\n'.join(table_row_reprs)

    def clone(self) -> 'Matrix':
        cloned_matrix = Matrix(self.row_length)
        cloned_matrix.diagonal_indices = self.diagonal_indices[:]
        cloned_matrix.rows = self.rows[:]

    def __repr__(self) -> str:
        return f'Matrix[{', '.join([str(row) for row in self.rows])}]'
