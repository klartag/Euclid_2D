Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == midpoint(C, A)
c == Circle(E, D, B)
F in h, c
G == midpoint(B, C)
H == projection(C, f)
I == midpoint(F, C)

Need to prove:
concyclic(D, G, H, I)

Proof:
