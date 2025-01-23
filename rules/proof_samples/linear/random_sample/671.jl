Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d)
f == Line(C, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(B, C, D)
E == midpoint(B, A)
F == midpoint(D, A)
g == Line(D, A)
G in g, d
H == projection(D, f)
h == Line(H, D)
I in h, d

Need to prove:
concyclic(E, F, G, I)

Proof:
