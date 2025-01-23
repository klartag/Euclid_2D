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
E == midpoint(B, A)
F == projection(C, i)
c == Circle(F, B, C)
G in i, c
H == midpoint(D, C)

Need to prove:
concyclic(D, E, G, H)

Proof:
