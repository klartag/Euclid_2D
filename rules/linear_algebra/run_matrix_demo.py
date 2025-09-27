from __future__ import annotations
import os
import sys
from fractions import Fraction

# Adjust REPO_ROOT if this file lives elsewhere.
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# --- Project imports ---
from rules.linear_algebra.matrix import Matrix
from rules.linear_algebra.vectors.augmented_vector import AugmentedVector
from rules.linear_algebra.vectors.sparse_vector import SparseVector


def build_sample_matrix() -> Matrix[SparseVector]:
    """
    Build a tiny matrix with 5 columns (objects) and two relations:

      R1: e0 - e1 = 0
      R2: 2*e2 + e3 - e4 = 0

    Constants are zero (pure column relations).
    """
    m = Matrix[SparseVector](row_length=5)

    # e0 - e1 = 0
    row1 = AugmentedVector(
        SparseVector({0: 1, 1: -1}, length=m.row_length),
        Fraction(0),
    )
    m.add_row(row1)

    # 2*e2 + e3 - e4 = 0
    row2 = AugmentedVector(
        SparseVector({2: 2, 3: 1, 4: -1}, length=m.row_length),
        Fraction(0),
    )
    m.add_row(row2)

    # e0 + e1 - e2 - e3 = 0
    row3 = AugmentedVector(
        SparseVector({0: 1, 1: 1, 2: -1, 3: -1}, m.row_length),
        Fraction(0),
    )
    m.add_row(row3)

    return m


def pretty_print_results(title: str, tuples: list[list[int]]):
    print(f"\n{title} (count={len(tuples)}):")
    for t in sorted(map(tuple, tuples)):
        print("  ", t)


def sanity_check_projection(m: Matrix[SparseVector], factors: list[int], tpl: list[int]) -> bool:
    """
    Verifies directly that sum(factors[t] * e_{tpl[t]}) projects to zero (vector part only).
    """
    vec = SparseVector({}, m.row_length)
    for c, idx in zip(factors, tpl):
        vec = vec + SparseVector({idx: c}, m.row_length)
    projected_vec = m.project_to_orthogonal_complement(AugmentedVector(vec, Fraction(0))).vector
    return projected_vec.first_nonzero_index() is None  # ignoring augmented constant


def main():
    m = build_sample_matrix()

    print("Current matrix (Gaussian-eliminated rows):")
    print(m or "<empty>")

    # Example 1: equality
    factors_eq = [1, -1]
    pairs = m.get_sparse_integer_linear_combinations(factors_eq)
    pretty_print_results("Results for factors [1, -1]", pairs)

    # Example 2: triple relation
    factors_triple = [2, 1, -1]
    triples = m.get_sparse_integer_linear_combinations(factors_triple)
    pretty_print_results("Results for factors [2, 1, -1]", triples)

    # Example 3: quad relation
    factors_quad = [1, 1, -1, -1]
    quads = m.get_sparse_integer_linear_combinations(factors_quad)
    pretty_print_results("Results for factors [1, 1, -1, -1]", quads)

    # Optional: sanity check a few tuples with direct projection
    print("\nSanity checks (projected sum should be zero):")
    for factors, tuples in [
        (factors_eq, pairs),
        (factors_triple, triples),
        (factors_quad, quads),
    ]:
        for tpl in tuples[:5]:  # just first few for brevity
            ok = sanity_check_projection(m, factors, tpl)
            print(f"  factors={factors}, tuple={tpl} -> {'OK' if ok else 'FAIL'}")

    print("\nDone.")


if __name__ == "__main__":
    main()
