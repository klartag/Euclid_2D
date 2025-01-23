Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(A, g)
c == Circle(C, A, B)
D == midpoint(B, A)
E in h, c
d == Circle(C, D, B)
e == Circle(E, A, D)
F == center(d)
i == Line(C, E)
G in e, d
H == line_intersection(f, i)

Need to prove:
concyclic(B, F, G, H)

Proof:
