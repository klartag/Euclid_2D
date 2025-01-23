Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(c, d)
f == external_angle_bisector(A, B, C)
c == Circle(C, A, B)
D in f, c
E == center(c)
F == midpoint(C, A)
d == Circle(D, C, F)
G == center(d)

Need to prove:
concyclic(C, E, F, G)

Proof:
