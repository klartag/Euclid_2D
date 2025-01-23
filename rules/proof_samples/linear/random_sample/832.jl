Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d, e)
f == Line(B, C)
c == Circle(C, A, B)
D == midpoint(C, A)
d == Circle(B, C, D)
E == center(d)
g == parallel_line(E, f)
F == center(c)
e == Circle(E, D, B)
G in g, e

Need to prove:
collinear(F, D, G)

Proof:
