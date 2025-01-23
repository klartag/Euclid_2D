Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
A in c
B in c
C in c
D in c
f == Line(D, B)
E == midpoint(C, A)
F == midpoint(C, D)
d == Circle(C, B, E)
G == midpoint(F, E)
H in f, d

Need to prove:
collinear(F, H, G)

Proof:
