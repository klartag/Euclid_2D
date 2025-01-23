Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == center(c)
F == midpoint(D, B)
i == Line(D, B)
d == Circle(F, A, C)
G in i, d
e == Circle(A, F, B)
H in h, e

Need to prove:
concyclic(E, F, G, H)

Proof:
