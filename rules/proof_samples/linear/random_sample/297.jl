Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
f == Line(B, A)
g == Line(C, A)
D == projection(B, g)
E == midpoint(C, A)
c == Circle(D, B, A)
F == midpoint(E, C)
G == midpoint(F, B)
h == Line(F, B)
H == projection(F, f)
I in h, c

Need to prove:
concyclic(D, G, H, I)

Proof:
