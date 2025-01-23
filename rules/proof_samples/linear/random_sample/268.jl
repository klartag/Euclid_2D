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
j == Line(B, D)
E == projection(A, g)
k == Line(E, A)
l == Line(C, A)
F == line_intersection(l, j)
G == midpoint(D, C)
H == projection(F, k)

Need to prove:
collinear(H, F, G)

Proof:
