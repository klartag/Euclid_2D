Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d, e)
A in c
B in c
C in c
f == Line(A, B)
D == center(c)
d == Circle(B, D, C)
e == Circle(A, C, D)
E in f, e
F == center(d)
G == midpoint(F, D)

Need to prove:
collinear(G, D, E)

Proof:
