Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(A, D)
j == Line(C, E)
F == line_intersection(j, f)
G == midpoint(D, F)
H == midpoint(B, G)

Need to prove:
collinear(C, A, H)

Proof:
