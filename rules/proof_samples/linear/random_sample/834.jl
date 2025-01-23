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
E == midpoint(C, A)
c == Circle(D, C, A)
F == midpoint(B, A)
G in g, c
d == Circle(C, E, F)
H in c, d

Need to prove:
concyclic(B, F, G, H)

Proof:
