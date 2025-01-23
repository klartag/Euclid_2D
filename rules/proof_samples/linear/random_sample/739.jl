Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, A)
g == Line(B, C)
c == Circle(C, A, B)
D == midpoint(B, A)
E == center(c)
F == projection(E, g)
G == midpoint(D, C)
h == parallel_line(G, f)

Need to prove:
F in h

Proof:
