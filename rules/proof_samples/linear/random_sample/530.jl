Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == external_angle_bisector(A, C, B)
E == line_intersection(j, i)
k == parallel_line(D, j)
F == midpoint(E, C)
G == projection(B, k)

Need to prove:
concyclic(A, B, F, G)

Proof:
