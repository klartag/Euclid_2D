Assumptions:
A, B, C, D, K, L, P, Q: Point
distinct(A, B, C, D, K, L, P, Q)

parallel(Line(A, B), Line(C, D))
convex(A, B, C, D)
distance(A, B) > distance(C, D)

K in Line(A, B)
L in Line(C, D)

concurrent(Line(A, D), Line(B, C), Line(K, L))

between(K, P, L)
between(K, Q, L)
angle(A, P, B) == angle(B, C, D) mod 360
angle(C, Q, D) == angle(A, B, C) mod 360

Need to prove:
concyclic(B, C, P, Q)

Proof:
