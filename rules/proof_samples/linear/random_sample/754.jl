Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, C)
g == parallel_line(A, f)
D == midpoint(B, C)
E == projection(D, g)
c == Circle(B, C, E)
F == midpoint(D, E)
G == center(c)

Need to prove:
collinear(E, G, F)

Proof:
