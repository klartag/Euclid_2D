Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d, e)
c == Circle(C, A, B)
D == midpoint(C, A)
f == Line(C, A)
E == center(c)
d == Circle(A, B, D)
F == center(d)
e == Circle(F, B, D)
G in f, e

Need to prove:
collinear(G, E, F)

Proof:
