Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E in g
c == Circle(C, D, B)
F == midpoint(D, C)
d == Circle(E, B, F)
G in h, d
e == Circle(G, D, E)
H in i, c
I in g, e

Need to prove:
concyclic(A, C, H, I)

Proof:
