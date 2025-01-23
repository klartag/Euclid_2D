Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
c == Circle(D, C, E)
d == Circle(A, B, E)
G == center(d)
i == Line(F, D)
H in i, c
e == Circle(G, B, C)
I in c, e

Need to prove:
concyclic(A, B, H, I)

Proof:
