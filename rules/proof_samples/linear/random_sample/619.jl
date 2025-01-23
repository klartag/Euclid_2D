Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
g == parallel_line(A, f)
D == midpoint(C, A)
E == midpoint(B, A)
h == Line(E, C)
c == Circle(E, A, D)
F == line_intersection(h, g)
G in h, c
H == midpoint(C, G)

Need to prove:
concyclic(A, D, F, H)

Proof:
