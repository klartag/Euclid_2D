Assumptions:
A, B, C, D, E, F, G: Point
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
A in c
B in c
C == center(c)
D == midpoint(C, A)
d == Circle(B, D, C)
E in d, c
F == midpoint(E, B)
G == center(d)

Need to prove:
concyclic(A, D, F, G)

Proof:
