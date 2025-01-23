Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G)
A in c
B in c
f == Line(A, B)
C == center(c)
D == midpoint(A, C)
E == midpoint(B, D)
F == midpoint(C, B)
G == projection(C, f)

Need to prove:
collinear(G, E, F)

Proof:
