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
E == midpoint(B, D)
F == midpoint(C, E)
c == Circle(A, F, B)
d == Circle(C, B, E)
G == midpoint(D, C)
H in d, c

Need to prove:
concyclic(C, F, G, H)

Proof:
