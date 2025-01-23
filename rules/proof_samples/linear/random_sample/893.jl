Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
f == Line(B, C)
D == midpoint(B, A)
E == midpoint(C, A)
F == projection(E, f)
G == midpoint(E, F)
c == Circle(D, E, G)
H == center(c)

Need to prove:
collinear(G, D, H)

Proof:
