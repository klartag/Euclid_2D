Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(C, A)
D == midpoint(B, A)
c == Circle(C, A, B)
E == center(c)
d == Circle(D, C, E)
F in d, c
h == Line(F, A)
G in f, d
i == parallel_line(G, g)
H == line_intersection(i, h)

Need to prove:
concyclic(C, D, G, H)

Proof:
