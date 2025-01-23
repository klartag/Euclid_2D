Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
c == Circle(C, A, B)
D == projection(C, f)
g == Line(C, D)
E == midpoint(C, A)
F == projection(E, g)
h == Line(F, A)
G in h, c
H == midpoint(B, C)

Need to prove:
concyclic(C, F, G, H)

Proof:
