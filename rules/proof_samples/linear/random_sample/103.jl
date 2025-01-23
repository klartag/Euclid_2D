Assumptions:
A, B, C, D, E, F: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(c, d)
A in c
B in c
C == midpoint(A, B)
D == center(c)
d == Circle(B, D, C)
E == center(d)
f == external_angle_bisector(E, D, A)
F in f, d

Need to prove:
collinear(F, C, E)

Proof:
