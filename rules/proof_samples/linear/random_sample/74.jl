Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(A, g)
D == projection(B, h)
c == Circle(B, C, D)
E in h, c
d == Circle(C, A, E)
F in f, d
G in g, d
H == midpoint(B, A)
I == center(d)

Need to prove:
concyclic(F, G, H, I)

Proof:
