Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
k == parallel_line(A, g)
l == Line(E, F)
G == line_intersection(k, j)
H == midpoint(G, C)

Need to prove:
H in l

Proof:
