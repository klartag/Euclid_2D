Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
f == internal_angle_bisector(C, A, B)
g == internal_angle_bisector(A, C, B)
h == external_angle_bisector(C, A, B)
D == line_intersection(f, g)
E == line_intersection(h, g)
c == Circle(E, D, B)
F == center(c)

Need to prove:
collinear(C, F, E)

Proof:
