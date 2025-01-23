Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == midpoint(B, C)
E == midpoint(D, B)
F == midpoint(D, A)
h == Line(D, A)
i == parallel_line(F, f)
j == parallel_line(E, h)
G == line_intersection(i, g)
H == projection(G, j)

Need to prove:
concyclic(D, E, F, H)

Proof:
