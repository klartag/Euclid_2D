Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
E == projection(D, f)
F == projection(A, h)
G == projection(C, h)
j == Line(C, G)
k == parallel_line(E, i)
H == line_intersection(j, k)

Need to prove:
concyclic(E, F, G, H)

Proof:
