Assumptions:
A, B, C, D, E, F, G: Point
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
A in c
B in c
C == midpoint(A, B)
D == center(c)
d == Circle(B, D, C)
E == midpoint(A, D)
F == midpoint(E, B)
G == center(d)

Need to prove:
collinear(G, C, F)

Proof:
