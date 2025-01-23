Assumptions:
A, B, C, D, E, F, G: Point
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
A in c
B in c
C == midpoint(A, B)
D == center(c)
E == midpoint(C, D)
F == midpoint(C, E)
d == Circle(D, B, F)
G in d, c

Need to prove:
collinear(G, F, A)

Proof:
