Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
F == midpoint(D, E)
c == Circle(C, A, B)
G == center(c)
h == Line(G, C)
H == projection(F, h)

Need to prove:
collinear(E, F, H)

Proof:
