Assumptions:
A, B, C, D, E, F, G, H: Point
f: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(c, d)
f == Line(B, A)
D == projection(C, f)
E == midpoint(B, C)
c == Circle(C, D, A)
F == center(c)
G == midpoint(B, A)
d == Circle(G, E, F)
H in d, c

Need to prove:
collinear(H, C, E)

Proof:
