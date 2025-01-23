Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == external_angle_bisector(A, B, C)
E == midpoint(D, C)
F == projection(A, j)
k == internal_angle_bisector(B, C, D)
l == parallel_line(E, i)
G == line_intersection(j, h)
H == line_intersection(k, l)

Need to prove:
concyclic(C, F, G, H)

Proof:
