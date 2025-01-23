Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == Line(C, A)
D == midpoint(B, A)
c == Circle(A, C, D)
E == center(c)
d == Circle(D, C, E)
F in f, d
G == projection(E, g)

Need to prove:
collinear(F, G, E)

Proof:
