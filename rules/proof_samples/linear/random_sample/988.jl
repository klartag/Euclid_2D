Assumptions:
A, B, C, D, E, F, G, H: Point
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
A in c
B in c
C == center(c)
D == midpoint(A, B)
E == midpoint(B, C)
d == Circle(A, C, E)
F == midpoint(E, D)
G in d, c
H == midpoint(C, G)

Need to prove:
collinear(H, F, B)

Proof:
