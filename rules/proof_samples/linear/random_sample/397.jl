Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(C, A)
D == midpoint(B, A)
E == midpoint(B, C)
g == Line(E, D)
F == midpoint(C, A)
c == Circle(D, E, F)
G in f, c
H == projection(G, g)

Need to prove:
collinear(B, H, G)

Proof:
