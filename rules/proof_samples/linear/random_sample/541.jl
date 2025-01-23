Assumptions:
A, B, C, D, E, F: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(c, d)
c == Circle(C, A, B)
D == midpoint(B, A)
f == internal_angle_bisector(A, B, C)
E == projection(A, f)
d == Circle(A, E, D)
F in d, c

Need to prove:
collinear(F, C, E)

Proof:
