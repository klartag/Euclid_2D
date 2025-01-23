Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
E == projection(D, f)
d == Circle(D, B, A)
F == center(d)
G == midpoint(D, E)
H == midpoint(G, D)

Need to prove:
collinear(H, F, E)

Proof:
