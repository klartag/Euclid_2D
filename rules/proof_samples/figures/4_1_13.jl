Assumptions:
A, B, C, D, E, F, X, Y, Z: Point

distinct(A, B, C, D, E, F, X, Y, Z)

not_collinear(A, B, C)

D == projection(A, Line(B, C))
E == projection(B, Line(A, C))
F == projection(C, Line(A, B))

X == midpoint(B, C)
Y == midpoint(B, E)
Z == midpoint(C, F)

Need to prove:
concyclic(D, X, Y, Z)

Proof:
