Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, A)
D == projection(C, f)
E == midpoint(B, A)
c == Circle(D, E, C)
g == parallel_line(C, f)
F == midpoint(C, E)
G in g, c

Need to prove:
collinear(D, F, G)

Proof:
