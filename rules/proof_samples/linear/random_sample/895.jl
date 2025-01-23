Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
F in f
j == Line(D, F)
k == parallel_line(B, j)
G == line_intersection(k, h)
H == midpoint(G, E)

Need to prove:
collinear(F, E, H)

Proof:
