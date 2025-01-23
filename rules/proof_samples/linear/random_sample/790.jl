Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D == midpoint(C, A)
E == center(c)
d == Circle(B, D, A)
F == projection(B, g)
h == Line(F, B)
G in h, d

Need to prove:
collinear(D, E, G)

Proof:
