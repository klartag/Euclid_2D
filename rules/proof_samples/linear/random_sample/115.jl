Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, B)
E == midpoint(D, A)
F == midpoint(B, A)
G == center(c)
d == Circle(E, F, G)
H == midpoint(B, G)
i == Line(B, G)
I in i, d
e == Circle(C, F, D)
J in h, e

Need to prove:
concyclic(D, H, I, J)

Proof:
