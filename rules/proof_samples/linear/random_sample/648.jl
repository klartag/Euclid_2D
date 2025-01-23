Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
f == internal_angle_bisector(A, B, C)
D == midpoint(B, A)
E == midpoint(D, C)
c == Circle(C, B, D)
F in f, c
G == midpoint(F, D)
d == Circle(E, C, F)
H == center(d)

Need to prove:
concyclic(C, D, G, H)

Proof:
