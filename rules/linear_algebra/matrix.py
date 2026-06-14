from typing import List, Optional, TypeVar, Generic

import itertools
from collections import defaultdict

from fractions import Fraction

from .vectors.abstract_iterable_vector import AbstractIterableVector
from .vectors.constant_vector import ConstantVector
from .vectors.augmented_vectors.augmented_vector_2 import AugmentedVector2
from .vectors.augmented_vectors.augmented_vector_3 import AugmentedVector3

V = TypeVar('V', bound=AbstractIterableVector)


class Matrix(Generic[V]):
    """
    Keeps track of a Matrix, in canonical form.
    
    vector_class:       The type of the vector depicting each row in the matrix.
    diagonal_indices:   In each row, the index of the first nonzero value.
                        (This list is strictly increasing, since `Matrix` is always in canonical form.)
    rows:               The rows of the matrix.
    row_length:         The length of each row in the matrix.
    """

    vector_class: type[V]
    diagonal_indices: List[int]
    rows: List[AugmentedVector3[V, ConstantVector, V]]
    row_length: int

    def __init__(self, vector_class: type[V], row_length: int):
        self.vector_class = vector_class
        self.diagonal_indices = []
        self.rows = []
        self.row_length = row_length

    def extend_row_length(self, amount: int):
        """Adds `amount` columns to the matrix."""
        for row in self.rows:
            row.inner0.extend_length(amount)
        self.row_length += amount

    def project_to_orthogonal_complement(self, vector: AugmentedVector2[V, ConstantVector]) -> AugmentedVector3[V, ConstantVector, V]:
        """
        Does the first stage of Gaussian elimination to a vector,
        removing all values in the vector in the indices that appear in `self.diagonal_indices`.
        
        Returns the projected vector, and appends to it a vector describing the linear combination of rows that produces this projection.
        """
        extended_vector: AugmentedVector3[V, ConstantVector, V] = AugmentedVector3(vector.inner0, vector.inner1, self.vector_class.create_empty(len(self.rows)))
        for i in range(len(self.rows)):
            if vector.inner0[self.diagonal_indices[i]] != 0:
                extended_vector -= self.rows[i] * vector.inner0[self.diagonal_indices[i]]
        return extended_vector

    def in_span(self, row: AugmentedVector2[V, ConstantVector]):
        """Returns whether a vector is contained within the linear span of the matrix rows."""
        projected_row = self.project_to_orthogonal_complement(row)
        return projected_row.inner0.first_nonzero_index() is None and not projected_row.inner1

    def add_row(self, row: AugmentedVector2[V, ConstantVector]) -> Optional[int]:
        """
        Adds a row to the matrix, perserving the canonical form of the matrix.
        If a new row of the matrix was added (i.e., if the given vector was *not* in the linear span of the matrix rows),
        returns an index that represents the given row.
        """
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

    def get_sparse_integer_linear_combinations(self, factors: List[int]) -> List[List[int]]:
        """
        Return all index tuples [i1, ..., ij] (1 <= j <= 4) such that
            sum_t factors[t] * e_{i_t}  ≡  0  (mod span(self.rows))
        Equivalence is tested by projecting basis columns with
        project_to_orthogonal_complement and comparing only the vector part
        (ignore constants).
        """

        if len(factors) == 0:
            return [[]]
        if 0 in factors:
            raise Exception("Cannot search linear combinations when one of the factors is zero.")

        coefficients = [Fraction(f) for f in factors]

        # --- Precompute P_i = projection of basis column i (vector part only) ---
        basis_projection: list[V] = []
        for i in range(self.row_length):
            basis = AugmentedVector2(self.vector_class.create_single(i, self.row_length), ConstantVector(Fraction(0)))
            proj = self.project_to_orthogonal_complement(basis).inner0
            basis_projection.append(proj)

        def enumerate_block(block_coeffs: list[Fraction], should_negate_signature: bool) -> dict[int, list[tuple[int, ...]]]:
            """
            Enumerate weighted sums for a contiguous block of coefficients.
            Returns: signature -> list of index tuples (in the order given by `block_coeffs`)
            """
            if len(block_coeffs) == 0:
                return { hash(self.vector_class.create_empty(0)): [()] }
            out: dict[int, list[tuple[int, ...]]] = defaultdict(list)

            for indices in itertools.combinations_with_replacement(range(self.row_length), len(block_coeffs)):
                v = self.vector_class.create_empty(self.row_length)
                for c, idx in zip(block_coeffs, indices):
                    v += (basis_projection[idx] * c)
                if should_negate_signature:
                    v *= Fraction(-1)
                out[hash(v)].append(tuple(indices))
            return out

        # Splitting the coefficients into two:
        k = len(factors) // 2
        left_coefficients = coefficients[:k]
        right_coefficients = coefficients[k:]

        right_map = enumerate_block(right_coefficients, True)
        left_map = enumerate_block(left_coefficients, False)

        # Join and build results in original order (left part then right part)
        results_set: list[list[int]] = []
        for signature, left_lists in left_map.items():
            right_lists = right_map.get(signature)
            if right_lists is None:
                continue
            for l in left_lists:
                for r in right_lists:
                    results_set.append(list(l + r))
        return results_set

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
        cloned_matrix = Matrix(self.vector_class, self.row_length)
        cloned_matrix.diagonal_indices = self.diagonal_indices[:]
        cloned_matrix.rows = self.rows[:]
        return cloned_matrix

    def __repr__(self) -> str:
        return f'Matrix[{', '.join([str(row) for row in self.rows])}]'
