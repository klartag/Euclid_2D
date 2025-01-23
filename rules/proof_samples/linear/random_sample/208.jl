Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d, e)
c == Circle(C, A, B)
f == internal_angle_bisector(A, C, B)
D == center(c)
E in f, c
F == midpoint(E, A)
d == Circle(F, C, A)
G == midpoint(E, C)
e == Circle(B, C, D)
H in d, e

Need to prove:
concyclic(D, F, G, H)

Proof:
