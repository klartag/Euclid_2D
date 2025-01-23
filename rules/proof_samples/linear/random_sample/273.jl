Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, A)
D == midpoint(B, A)
g == parallel_line(C, f)
E == midpoint(D, A)
c == Circle(C, D, A)
F == center(c)
G == projection(F, g)
h == Line(F, G)

Need to prove:
E in h

Proof:
