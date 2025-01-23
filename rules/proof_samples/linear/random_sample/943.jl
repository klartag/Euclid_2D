Assumptions:
A, B, C, D, E, F, G: Point
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
c == Circle(C, A, B)
D == midpoint(B, A)
E == center(c)
d == Circle(E, B, A)
F == center(d)
G == midpoint(C, E)

Need to prove:
concyclic(C, D, F, G)

Proof:
