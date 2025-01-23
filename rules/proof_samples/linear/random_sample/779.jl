Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
d == Circle(E, C, A)
F == midpoint(D, B)
G == midpoint(B, A)
e == Circle(F, G, E)
H in d, e

Need to prove:
collinear(A, F, H)

Proof:
