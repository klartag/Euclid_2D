Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == Line(C, A)
E == midpoint(B, D)
F in j
G == midpoint(E, F)

Need to prove:
collinear(G, C, E)

Proof:
