Assumptions:
A, B, C, D, E, F: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(c, d)
c == Circle(C, A, B)
D == center(c)
f == internal_angle_bisector(A, D, B)
d == Circle(C, D, A)
E in f, d
F == midpoint(E, C)

Need to prove:
collinear(C, B, F)

Proof:
