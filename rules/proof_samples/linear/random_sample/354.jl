Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == parallel_line(A, f)
c == Circle(C, A, B)
D == midpoint(B, C)
E in h, c
d == Circle(D, E, B)
F == midpoint(B, A)
G == projection(F, g)
H == center(d)

Need to prove:
collinear(G, H, F)

Proof:
