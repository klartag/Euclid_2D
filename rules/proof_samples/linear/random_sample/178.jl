Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == midpoint(B, A)
c == Circle(A, C, D)
d == Circle(C, A, B)
h == parallel_line(D, g)
E == line_intersection(f, h)
F == center(d)
G in h, c

Need to prove:
concyclic(C, E, F, G)

Proof:
