Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
k == parallel_line(E, j)
G == line_intersection(f, k)
l == Line(E, F)
H == line_intersection(i, l)

Need to prove:
concyclic(A, E, G, H)

Proof:
