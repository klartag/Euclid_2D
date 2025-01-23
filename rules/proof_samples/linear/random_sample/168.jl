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
E == projection(B, h)
F == projection(C, f)
G == midpoint(D, A)
H == midpoint(C, F)
c == Circle(H, E, C)
I in g, c

Need to prove:
concyclic(D, E, G, I)

Proof:
