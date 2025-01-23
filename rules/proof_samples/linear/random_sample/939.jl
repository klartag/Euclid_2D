Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(B, C)
F == center(c)
d == Circle(F, D, A)
e == Circle(E, F, B)
G in d, e

Need to prove:
collinear(E, G, A)

Proof:
