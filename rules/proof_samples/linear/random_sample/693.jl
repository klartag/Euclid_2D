Assumptions:
A, B, C, D, E, F, G: Point
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d, e)
D == midpoint(B, C)
c == Circle(C, A, B)
E == midpoint(B, A)
F == center(c)
d == Circle(C, F, E)
e == Circle(B, D, E)
G in d, e

Need to prove:
false() # collinear(A, F, G)

Proof:
