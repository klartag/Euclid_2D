Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(C, A)
g == parallel_line(B, f)
D == projection(A, g)
E == midpoint(B, C)
F == midpoint(B, A)
c == Circle(A, D, F)
G == center(c)

Need to prove:
collinear(F, G, E)

Proof:
