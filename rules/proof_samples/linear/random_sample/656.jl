Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
A in c
B in c
f == Line(A, B)
C == center(c)
D == midpoint(A, C)
E == projection(C, f)
d == Circle(C, B, E)
F == midpoint(B, D)
G == center(d)

Need to prove:
collinear(E, G, F)

Proof:
