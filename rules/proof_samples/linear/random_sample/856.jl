Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == Line(C, A)
D == midpoint(B, A)
c == Circle(A, C, D)
E == projection(D, g)
F in c
G == projection(C, f)
d == Circle(F, D, G)
h == Line(E, G)
H in h, d

Need to prove:
collinear(F, H, A)

Proof:
