Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
k == parallel_line(E, j)
l == parallel_line(A, k)
G == projection(E, l)

Need to prove:
collinear(E, F, G)

Proof:
