Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d, e, k)
f == Line(B, C)
g == Line(C, A)
D == projection(B, g)
h == Line(D, B)
c == Circle(B, C, D)
d == Circle(D, B, A)
E in f, d
e == Circle(C, D, E)
F in h, e
k == Circle(E, F, B)
G in k, c
H == center(d)
I == midpoint(D, A)

Need to prove:
concyclic(C, G, H, I)

Proof:
