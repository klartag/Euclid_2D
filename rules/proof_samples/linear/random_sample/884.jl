Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == internal_angle_bisector(C, D, A)
E == midpoint(B, A)
F == projection(E, j)
k == Line(E, F)
G == line_intersection(k, h)
H == midpoint(E, G)
I == line_intersection(f, j)

Need to prove:
collinear(I, H, C)

Proof:
