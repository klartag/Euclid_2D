Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
f == internal_angle_bisector(A, B, C)
D == midpoint(C, A)
g == internal_angle_bisector(D, C, B)
E == line_intersection(f, g)
c == Circle(B, E, A)
F == center(c)

Need to prove:
collinear(F, E, C)

Proof:
