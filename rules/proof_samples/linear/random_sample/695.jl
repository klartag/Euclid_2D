Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j)
f == Line(C, A)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
E == projection(B, i)
j == parallel_line(E, f)
F == line_intersection(j, g)

Need to prove:
concyclic(B, D, E, F)

Proof:
