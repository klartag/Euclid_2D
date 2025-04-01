Assumptions:
A, B, C, D, E, F, G, H: Point
distinct(A, B, C, D, E, F, G, H)

concyclic(A, B, C, D)
convex(A, B, C, D)

E in Line(A, C), Line(B, D)
F in Line(A, D), Line(B, C)

parallelogram(E, C, G, D)
Line(A, D) == perpendicular_bisector(H, E)

Need to prove:
concyclic(D, H, F, G)

Proof:
