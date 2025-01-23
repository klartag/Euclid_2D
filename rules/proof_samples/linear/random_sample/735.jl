Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
f == Line(C, A)
c == Circle(C, A, B)
D == midpoint(B, A)
E == midpoint(C, D)
F == center(c)
G == projection(F, f)
d == Circle(G, C, E)
H in c, d

Need to prove:
collinear(B, E, H)

Proof:
