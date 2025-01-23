Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
f == Line(C, A)
D == midpoint(B, A)
E == midpoint(D, C)
g == Line(D, C)
F == midpoint(B, C)
G == midpoint(B, D)
h == parallel_line(F, g)
H == midpoint(G, A)
I == line_intersection(h, f)

Need to prove:
collinear(I, E, H)

Proof:
