from typing import List, TypeVar, Generic

import itertools
from collections import defaultdict

from fractions import Fraction

from .vectors.abstract_vector import AbstractVector
from .vectors.sparse_vector import SparseVector
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
        basis_projection: list[A] = []
        for i in range(self.row_length):
            basis = AugmentedVector(SparseVector({i: 1}, self.row_length), Fraction(0))
            proj = self.project_to_orthogonal_complement(basis).vector
            basis_projection.append(proj)

        # --- Local helpers  ---
        def sig(v: SparseVector) -> tuple[tuple[int, Fraction], ...]:
            """Canonical, hashable signature of a sparse vector."""
            inner = v.inner
            if not inner:
                return ()
            return tuple(sorted((k, inner[k]) for k in inner.keys() if inner[k] != 0))

        def enumerate_block(block_coeffs: list[Fraction]) -> dict[tuple, list[tuple[int, ...]]]:
            """
            Enumerate weighted sums for a contiguous block of coefficients,
            keeping only index-tuples that are strictly increasing across the block
            (this implies within-block distinctness).
            Returns: signature -> list of index tuples (in block order).
            """
            if len(block_coeffs) == 0:
                return { (): [()] }
            out: dict[tuple, list[tuple[int, ...]]] = defaultdict(list)

            for indices in itertools.combinations_with_replacement(range(self.row_length), len(block_coeffs)):
                v = SparseVector({}, self.row_length)
                for c, idx in zip(block_coeffs, indices):
                    v = v + (basis_projection[idx] * c)
                out[sig(v)].append(tuple(indices))
            return out

        # --- Meet-in-the-middle join ---
        k = len(factors) // 2
        left_coeffs = coefficients[:k]
        right_coeffs = coefficients[k:]

        left_map = enumerate_block(left_coeffs)
        # For the right map we store signatures of the NEGATED sum so that
        # we can match left_sum == -(right_sum).
        right_map_raw = enumerate_block(right_coeffs)
        right_map: dict[tuple, list[tuple[int, ...]]] = defaultdict(list)
        for s, idx_lists in right_map_raw.items():
            # Reconstruct a SparseVector to negate its signature robustly
            if s == ():
                neg_sig = ()
            else:
                # s is a tuple[(i, val)], all Fractions → negation is trivial
                neg_sig = tuple((i, -val) for (i, val) in s)
            right_map[neg_sig].extend(idx_lists)

        # Join and build results in original order (left part then right part)
        results_set: set[tuple[int, ...]] = set()
        if not left_coeffs:
            # whole thing on the right; nothing to join
            for s, r_lists in right_map.items():
                if s == ():
                    for r in r_lists:
                        # r already canonical within its block; just accept (no left side)
                        results_set.add(tuple(r))
        elif not right_coeffs:
            for s, l_lists in left_map.items():
                if s == ():
                    for l in l_lists:
                        results_set.add(tuple(l))
        else:
            for s, l_lists in left_map.items():
                r_lists = right_map.get(s)
                if not r_lists:
                    continue
                for l in l_lists:
                    for r in r_lists:
                        # STRICT GLOBAL ORDER: all l’s then all r’s must be increasing
                        if l and r and not (l[-1] < r[0]):
                            continue
                        results_set.add(tuple(l + r))

        return [list(t) for t in results_set]

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
