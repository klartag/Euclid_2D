Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
C in h # (defining h)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == midpoint(B, A)
k == parallel_line(G, i)
H == line_intersection(k, j)

Need to prove:
concyclic(E, F, G, H)

Proof:
