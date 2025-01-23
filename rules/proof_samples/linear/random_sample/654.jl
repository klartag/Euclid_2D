Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(C, A)
D == midpoint(B, A)
g == parallel_line(D, f)
E == midpoint(B, C)
F == projection(C, g)
G == projection(B, f)
h == Line(G, B)
H == projection(E, h)

Need to prove:
concyclic(C, F, G, H)

Proof:
