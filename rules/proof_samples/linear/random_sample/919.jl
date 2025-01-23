Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == midpoint(C, A)
E == projection(B, g)
h == Line(D, B)
c == Circle(B, E, D)
F in f, c
d == Circle(C, D, F)
G in h, d

Need to prove:
concyclic(B, C, E, G)

Proof:
