Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(C, A)
D == projection(B, g)
h == Line(D, B)
E == midpoint(C, D)
F == projection(C, f)
c == Circle(B, F, D)
d == Circle(D, B, A)
G == center(c)
e == Circle(E, D, G)
H == projection(F, h)
i == Line(H, F)
I in d, e
J in i, c

Need to prove:
concyclic(B, G, I, J)

Proof:
