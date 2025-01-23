Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == projection(B, i)
E == projection(B, h)
c == Circle(D, E, B)
F == center(c)
d == Circle(C, E, F)
G in c, d

Need to prove:
concyclic(A, D, F, G)

Proof:
