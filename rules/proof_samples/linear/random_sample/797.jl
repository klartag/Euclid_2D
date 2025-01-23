Assumptions:
A, B, C, D, E, F: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F)
D == midpoint(B, A)
c == Circle(B, D, C)
E == center(c)
f == internal_angle_bisector(D, E, B)
F == projection(B, f)

Need to prove:
collinear(F, D, A)

Proof:
