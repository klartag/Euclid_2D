Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G)
D == midpoint(C, A)
c == Circle(B, D, C)
f == external_angle_bisector(A, C, B)
E in f, c
F == midpoint(E, B)
G == midpoint(D, E)

Need to prove:
concyclic(B, D, F, G)

Proof:
