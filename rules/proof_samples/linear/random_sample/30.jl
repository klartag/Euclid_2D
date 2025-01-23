Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, C)
c == Circle(C, A, B)
D == midpoint(B, A)
g == parallel_line(D, f)
E == center(c)
F == midpoint(D, B)
G == projection(E, g)
h == Line(E, G)
d == Circle(E, C, A)
H in h, d

Need to prove:
collinear(H, F, D)

Proof:
