Assumptions:
A, B, C, D, E, F, G, H, I: Point
f: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(c, d, e)
f == Line(B, C)
D == midpoint(B, A)
E == midpoint(C, A)
c == Circle(A, E, D)
F == midpoint(D, A)
d == Circle(F, C, A)
G == midpoint(B, C)
H in d, c
e == Circle(F, D, G)
I in f, e

Need to prove:
collinear(H, D, I)

Proof:
