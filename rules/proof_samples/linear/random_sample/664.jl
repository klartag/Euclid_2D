Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D == midpoint(B, A)
d == Circle(D, C, A)
E in g, c
F in g, d
G == midpoint(E, D)

Need to prove:
collinear(B, F, G)

Proof:
