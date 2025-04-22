Assumptions:
A, B, C, D, E, F, M, X: Point
distinct(A, B, C, D, E, F, M, X)
convex(A, B, C, D, E)

F in Line(A, C)
perpendicular(Line(F, B), Line(B, C))

angle(F, A, B) == angle(F, B, A) mod 360
angle(F, B, A) == angle(D, A, C) mod 360
angle(D, A, C) == angle(D, C, A) mod 360
angle(D, C, A) == angle(E, A, D) mod 360
angle(E, A, D) == angle(E, D, A) mod 360

M == midpoint(C, F)
parallelogram(A, M, X, E)

Need to prove:
concurrent(Line(B, D), Line(E, M), Line(F, X))

Proof:
