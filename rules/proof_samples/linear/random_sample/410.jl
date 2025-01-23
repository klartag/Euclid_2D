Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
g == Line(C, A)
D == midpoint(B, A)
E == projection(A, f)
h == parallel_line(D, g)
F == midpoint(C, A)
G == line_intersection(h, f)

Need to prove:
concyclic(D, E, F, G)

Proof:
