Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
f == Line(C, A)
g == external_angle_bisector(C, A, B)
h == parallel_line(B, g)
D == midpoint(C, A)
i == internal_angle_bisector(A, C, B)
j == internal_angle_bisector(D, A, B)
E == line_intersection(i, j)
F == line_intersection(f, h)

Need to prove:
concyclic(B, C, E, F)

Proof:
