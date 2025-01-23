Assumptions:
A, B, C, D, E, F: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(c, d)
A in c
B in c
C in c
f == internal_angle_bisector(C, A, B)
D == midpoint(B, C)
E == projection(B, f)
d == Circle(B, E, D)
F in d, c

Need to prove:
collinear(A, F, E)

Proof:
