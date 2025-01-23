Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(C, A)
D == midpoint(C, A)
g == parallel_line(B, f)
c == Circle(C, A, B)
E in g, c
F == midpoint(B, C)
G == midpoint(A, E)
h == Line(A, E)
d == Circle(F, D, G)
H in h, d

Need to prove:
concyclic(C, D, E, H)

Proof:
