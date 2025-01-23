Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
d == Circle(D, C, A)
E == center(d)
F == projection(E, g)
e == Circle(A, E, F)
G == midpoint(B, C)
H in h, e

Need to prove:
collinear(H, F, G)

Proof:
