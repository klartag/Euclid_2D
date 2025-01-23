Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(B, A)
d == Circle(D, C, A)
F == midpoint(C, A)
G == midpoint(E, D)
h == Line(E, D)
H in h, d
e == Circle(G, B, H)
I in f, e

Need to prove:
concyclic(E, F, G, I)

Proof:
