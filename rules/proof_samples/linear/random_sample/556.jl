Assumptions:
A, B, C, D, E, F, G: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G)
f == internal_angle_bisector(A, C, B)
c == Circle(C, A, B)
D in f, c
E == midpoint(B, A)
F == midpoint(E, B)
G == projection(F, f)

Need to prove:
concyclic(D, E, F, G)

Proof:
