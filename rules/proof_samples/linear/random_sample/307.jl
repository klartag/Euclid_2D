Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == Line(C, A)
g == parallel_line(B, f)
h == external_angle_bisector(A, C, B)
D == midpoint(B, C)
E == line_intersection(h, g)
i == external_angle_bisector(E, B, D)
F == line_intersection(f, i)

Need to prove:
collinear(E, F, D)

Proof:
