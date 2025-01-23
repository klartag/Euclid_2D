Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(B, D)
j == external_angle_bisector(D, E, C)
k == parallel_line(A, j)
F == projection(C, k)

Need to prove:
collinear(F, D, E)

Proof:
