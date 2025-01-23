Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == internal_angle_bisector(B, C, D)
E == projection(D, j)
k == Line(D, E)
l == external_angle_bisector(B, A, D)
F == line_intersection(k, f)
G == projection(B, l)

Need to prove:
concyclic(A, E, F, G)

Proof:
