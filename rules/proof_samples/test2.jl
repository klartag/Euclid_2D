Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l, m: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l, m)
A in f # (defining f)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
k == external_angle_bisector(G, D, B)
l == parallel_line(A, k)
m == internal_angle_bisector(G, F, E)
H == line_intersection(m, l)

Need to prove:
concyclic(D, F, G, H)

Proof:
