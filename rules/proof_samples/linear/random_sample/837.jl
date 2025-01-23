Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
g == parallel_line(A, f)
D == midpoint(C, A)
h == parallel_line(D, g)
E == midpoint(B, A)
F in h
G == midpoint(F, D)

Need to prove:
collinear(F, E, G)

Proof:
