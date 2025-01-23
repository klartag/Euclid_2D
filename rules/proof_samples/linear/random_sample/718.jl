Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e)
f == Line(B, C)
g == Line(C, A)
D == projection(B, g)
E == midpoint(B, A)
c == Circle(C, E, D)
F in f, c
d == Circle(B, F, E)
e == Circle(C, A, B)
G in e, c
H == center(d)

Need to prove:
concyclic(B, E, G, H)

Proof:
