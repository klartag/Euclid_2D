Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == internal_angle_bisector(C, A, B)
g == internal_angle_bisector(A, B, C)
D == line_intersection(f, g)
E == midpoint(C, D)
c == Circle(D, B, A)
F == center(c)
G == midpoint(F, D)

Need to prove:
collinear(F, E, G)

Proof:
