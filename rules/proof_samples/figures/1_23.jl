Assumptions:
A, B, C, D, X, Y, Z: Point
distinct(A, B, C, D, X, Y, Z)

concyclic(A, B, C, D)

between(X, A, B)
between(X, D, C)

between(B, C, Y)
between(A, D, Y)

Line(X, Z) == internal_angle_bisector(A, X, D)
Line(Y, Z) == internal_angle_bisector(C, Y, D)

Need to prove:
perpendicular(Line(X, Z), Line(Y, Z))

Proof:
