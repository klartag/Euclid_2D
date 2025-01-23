Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d, e)
A in c
B in c
C in c
f == Line(C, A)
D == midpoint(A, B)
E == center(c)
d == Circle(E, A, C)
e == Circle(A, E, D)
F == center(d)
G in f, e
H == midpoint(F, E)

Need to prove:
collinear(H, G, E)

Proof:
