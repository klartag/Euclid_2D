Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
f == Line(B, C)
g == parallel_line(A, f)
h == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
c == Circle(B, C, D)
E == midpoint(D, C)
F == center(c)

Need to prove:
collinear(A, F, E)

Proof:
