Assumptions:
A, B, C, D, E, F, G, H: Point
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
D == midpoint(C, A)
E == midpoint(D, B)
F == midpoint(D, A)
c == Circle(B, D, C)
G == midpoint(F, E)
d == Circle(E, D, F)
H in c, d

Need to prove:
concyclic(A, F, G, H)

Proof:
