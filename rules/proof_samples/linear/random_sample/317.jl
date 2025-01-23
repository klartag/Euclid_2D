Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, A, B)
E in h, c
F == midpoint(E, B)
d == Circle(E, F, D)
G in d, c
H == center(d)

Need to prove:
concyclic(A, F, G, H)

Proof:
