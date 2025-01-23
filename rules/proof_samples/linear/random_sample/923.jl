Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
F == midpoint(C, A)
i == parallel_line(E, h)
j == Line(F, D)
G == line_intersection(i, j)

Need to prove:
concyclic(A, B, E, G)

Proof:
