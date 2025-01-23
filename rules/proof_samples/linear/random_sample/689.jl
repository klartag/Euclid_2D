Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, C)
g == parallel_line(A, f)
D == projection(C, g)
E == midpoint(B, C)
F == projection(E, g)
c == Circle(D, F, E)
G == center(c)

Need to prove:
collinear(C, G, F)

Proof:
