Assumptions:
A, B, C, D, E, F, P: Point
distinct(A, B, C, D, E, F, P)
P in Circle(A, B, C)
D == projection(P, Line(B, C))
E == projection(P, Line(A, C))
F == projection(P, Line(A, B))

Need to prove:
collinear(D, E, F)

Proof:
