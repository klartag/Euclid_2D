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
E == projection(A, h)
c == Circle(C, A, E)
F == center(c)
d == Circle(F, D, C)
G in f, c
H in c, d

Need to prove:
concyclic(B, D, G, H)

Proof:
