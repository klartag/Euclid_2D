Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(D, C)
c == Circle(C, A, B)
F == projection(D, f)
G in h, c
H == midpoint(G, C)

Need to prove:
concyclic(B, E, F, H)

Proof:
