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
D in g, c
E in g
d == Circle(A, E, D)
F in f, d
G == midpoint(B, E)

Need to prove:
collinear(C, F, G)

Proof:
