Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(B, D)
F == midpoint(E, A)
G == midpoint(F, A)
H == midpoint(E, G)
I == midpoint(C, E)

Need to prove:
collinear(I, F, H)

Proof:
