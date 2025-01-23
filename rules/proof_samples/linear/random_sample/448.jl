Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
g == Line(B, C)
D == projection(A, g)
E == projection(C, f)
h == Line(E, C)
c == Circle(C, A, B)
F in h, c
G == midpoint(F, D)
H == projection(G, g)

Need to prove:
collinear(G, E, H)

Proof:
