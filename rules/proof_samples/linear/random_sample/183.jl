Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
f == internal_angle_bisector(A, B, C)
g == external_angle_bisector(A, B, C)
D == midpoint(B, C)
E == projection(C, f)
c == Circle(B, C, E)
F in g, c

Need to prove:
collinear(E, F, D)

Proof:
