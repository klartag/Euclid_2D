Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
F == midpoint(B, A)
d == Circle(C, F, D)
e == Circle(F, E, B)
G in h, d
H == midpoint(E, A)
i == Line(E, A)
I in i, e

Need to prove:
concyclic(D, G, H, I)

Proof:
