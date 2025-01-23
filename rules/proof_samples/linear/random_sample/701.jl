Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e, h: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e, h)
c == Circle(C, A, B)
D == midpoint(C, A)
f == Line(C, A)
E == center(c)
d == Circle(D, E, B)
g == Line(E, D)
F in c, d
e == Circle(C, D, F)
G in g, e
H in f, d
h == Circle(G, A, B)
I in e, h

Need to prove:
concyclic(B, C, H, I)

Proof:
