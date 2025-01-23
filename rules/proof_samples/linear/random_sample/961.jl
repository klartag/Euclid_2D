Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
F == midpoint(E, B)
G == midpoint(D, F)
H == midpoint(E, G)

Need to prove:
collinear(H, B, E)

Proof:
