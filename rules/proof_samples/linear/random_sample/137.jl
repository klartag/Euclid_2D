Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
E == projection(D, f)
j == parallel_line(B, g)
k == parallel_line(E, h)
F == line_intersection(j, i)
G == line_intersection(j, k)

Need to prove:
concyclic(D, E, F, G)

Proof:
